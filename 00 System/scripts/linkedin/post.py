#!/usr/bin/env python3
"""
Publish or schedule LinkedIn posts from vault drafts.

Usage:
    post.py <name>                                 # publish one draft immediately (partial name ok)
    post.py --all                                  # publish all drafts immediately
    post.py --all --schedule                       # schedule all drafts via launchd (Mon/Tue/Thu/Fri 8 AM MT)
    post.py --all --schedule --start 2026-05-12    # start cadence from a specific date
    post.py <name> --schedule [--start DATE]       # schedule one draft via launchd
    post.py <name> --unschedule                    # remove launchd job, revert draft to status: draft
    post.py --all --unschedule                     # unschedule all scheduled drafts
    post.py <name> --dry-run                       # preview without posting or writing plists
    post.py <name> --hook A                        # prepend Hook A from the draft

Scheduling writes a launchd plist to ~/Library/LaunchAgents/ and registers it
via `launchctl bootstrap`. When the job fires, it calls this script with the
draft path to publish immediately. LinkedIn's REST API does not support
member-account post scheduling (lifecycleState "SCHEDULED" is rejected with 422);
launchd is the local workaround.

Scheduling spaces drafts Mon/Tue/Thu/Fri at 8:00 AM Mountain Time, ordered by
`priority` frontmatter (lowest number first), then by filename.

Images: add `image: filename.png` to frontmatter. Place the file in
`05 Content/LinkedIn/assets/`. The script uploads it and attaches it to the post.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import zoneinfo
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent.parent.parent
ENV_PATH = SCRIPT_DIR / ".env"

DRAFTS_DIR = VAULT_ROOT / "05 Content" / "LinkedIn" / "drafts"
PUBLISHED_DIR = VAULT_ROOT / "05 Content" / "LinkedIn" / "published"
ASSETS_DIR = VAULT_ROOT / "05 Content" / "LinkedIn" / "assets"
LOGS_DIR = SCRIPT_DIR / "logs"

LAUNCH_AGENTS_DIR = Path.home() / "Library" / "LaunchAgents"
LABEL_PREFIX = "com.mitchell.linkedin"

POSTS_API = "https://api.linkedin.com/rest/posts"
IMAGES_API = "https://api.linkedin.com/rest/images"
LINKEDIN_VERSION = "202503"

MOUNTAIN = zoneinfo.ZoneInfo("America/Denver")
POST_DAYS = {0, 1, 3, 4}  # Mon, Tue, Thu, Fri
POST_HOUR = 8              # 8:00 AM Mountain


# ---------------------------------------------------------------------------
# Scheduling helpers
# ---------------------------------------------------------------------------

def schedule_slots(start: dt.date):
    """Yield 8 AM MT datetimes on Mon/Tue/Thu/Fri starting from start."""
    d = start
    while True:
        if d.weekday() in POST_DAYS:
            yield dt.datetime(d.year, d.month, d.day, POST_HOUR, 0, 0,
                              tzinfo=MOUNTAIN)
        d += dt.timedelta(days=1)


def next_monday(from_date: dt.date | None = None) -> dt.date:
    d = from_date or dt.date.today()
    days_ahead = (7 - d.weekday()) % 7
    return d + dt.timedelta(days=days_ahead or 7)


def sort_key(path: Path, fm: dict) -> tuple[int, str]:
    """Sort by priority (lowest first), then filename. Unprioritised drafts go last."""
    raw = fm.get("priority", "")
    try:
        p = int(raw)
    except (ValueError, TypeError):
        p = 9999
    return (p, path.name)


# ---------------------------------------------------------------------------
# Env / token
# ---------------------------------------------------------------------------

def load_env() -> dict:
    if not ENV_PATH.exists():
        sys.exit(f"Missing {ENV_PATH}. Run auth.py first.")
    env = {}
    for line in ENV_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


def check_token(env: dict) -> None:
    expires_at = int(env.get("LINKEDIN_TOKEN_EXPIRES_AT", "0") or 0)
    if expires_at and time.time() > expires_at:
        sys.exit("Access token expired. Run `python3 auth.py --refresh`.")
    if not env.get("LINKEDIN_ACCESS_TOKEN") or not env.get("LINKEDIN_AUTHOR_URN"):
        sys.exit("Missing access token or author URN. Run auth.py.")


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")
    fm = {}
    for line in fm_block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, body


def serialize_frontmatter(fm: dict, body: str) -> str:
    lines = ["---"]
    for k, v in fm.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n" + body


# ---------------------------------------------------------------------------
# Post text extraction
# ---------------------------------------------------------------------------

def extract_section(body: str, heading: str) -> str | None:
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if lines[j].startswith("## ") or lines[j].strip() == "---":
            end = j
            break
    return "\n".join(lines[start:end]).strip()


def extract_hook(body: str, letter: str) -> str | None:
    section = extract_section(body, "Hook Options")
    if not section:
        return None
    pattern = rf"^-\s*{letter}:\s*\"?(.*?)\"?\s*$"
    for line in section.splitlines():
        m = re.match(pattern, line)
        if m:
            return m.group(1).strip()
    return None


def build_post_text(body: str, hook_letter: str | None) -> str:
    final = extract_section(body, "Final Post")
    if final:
        return final
    post_body = extract_section(body, "Post Body") or extract_section(body, "Article Body")
    if not post_body:
        sys.exit("Could not find `## Final Post`, `## Post Body`, or `## Article Body` in the draft.")
    if hook_letter:
        hook = extract_hook(body, hook_letter)
        if hook:
            return f"{hook}\n\n{post_body}"
    return post_body


# ---------------------------------------------------------------------------
# Image upload
# ---------------------------------------------------------------------------

def upload_image(env: dict, image_path: Path) -> str:
    """Upload an image to LinkedIn and return its URN."""
    token = env["LINKEDIN_ACCESS_TOKEN"]
    owner = env["LINKEDIN_AUTHOR_URN"]

    # Step 1: initialize upload
    init_payload = json.dumps({
        "initializeUploadRequest": {"owner": owner}
    }).encode()
    req = urllib.request.Request(
        f"{IMAGES_API}?action=initializeUpload",
        data=init_payload,
        method="POST",
    )
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("LinkedIn-Version", LINKEDIN_VERSION)
    req.add_header("X-Restli-Protocol-Version", "2.0.0")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            init_data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"Image upload init failed: HTTP {e.code}\n{e.read().decode()}")

    upload_url = init_data["value"]["uploadUrl"]
    image_urn = init_data["value"]["image"]

    # Step 2: upload binary
    image_bytes = image_path.read_bytes()
    put_req = urllib.request.Request(upload_url, data=image_bytes, method="PUT")
    put_req.add_header("Content-Type", "application/octet-stream")
    try:
        urllib.request.urlopen(put_req)
    except urllib.error.HTTPError as e:
        sys.exit(f"Image binary upload failed: HTTP {e.code}\n{e.read().decode()}")

    return image_urn


# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------

def call_api(env: dict, payload: dict) -> tuple[int, dict, str]:
    req = urllib.request.Request(
        POSTS_API,
        data=json.dumps(payload).encode(),
        method="POST",
    )
    req.add_header("Authorization", f"Bearer {env['LINKEDIN_ACCESS_TOKEN']}")
    req.add_header("LinkedIn-Version", LINKEDIN_VERSION)
    req.add_header("X-Restli-Protocol-Version", "2.0.0")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, dict(resp.headers), resp.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read().decode()


def build_payload(env: dict, text: str, image_urn: str | None = None) -> dict:
    # LinkedIn's REST API (202503) does not support member-account post scheduling.
    # lifecycleState "SCHEDULED" and scheduledAt are rejected with HTTP 422.
    # Scheduling is handled via launchd; this function always builds an immediate-publish payload.
    payload: dict = {
        "author": env["LINKEDIN_AUTHOR_URN"],
        "commentary": text,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": [],
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False,
    }
    if image_urn:
        payload["content"] = {"media": {"id": image_urn}}
    return payload


# ---------------------------------------------------------------------------
# launchd scheduling
# ---------------------------------------------------------------------------

def make_label(draft_path: Path) -> str:
    """Derive a stable, reproducible launchd label from the draft filename."""
    slug = draft_path.stem.lower()
    slug = re.sub(r"[\s.]+", "-", slug)
    return f"{LABEL_PREFIX}.{slug}"


def make_plist_xml(label: str, draft_path: Path, slot: dt.datetime) -> str:
    log = LOGS_DIR / f"{label}.log"
    err = LOGS_DIR / f"{label}.err"
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>{label}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>{SCRIPT_DIR / "post.py"}</string>
        <string>{draft_path}</string>
    </array>
    <key>WorkingDirectory</key>
    <string>{SCRIPT_DIR}</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Month</key>
        <integer>{slot.month}</integer>
        <key>Day</key>
        <integer>{slot.day}</integer>
        <key>Hour</key>
        <integer>{slot.hour}</integer>
        <key>Minute</key>
        <integer>{slot.minute}</integer>
    </dict>
    <key>RunAtLoad</key>
    <false/>
    <key>StandardOutPath</key>
    <string>{log}</string>
    <key>StandardErrorPath</key>
    <string>{err}</string>
</dict>
</plist>
"""


def schedule_one(file_path: Path, slot: dt.datetime, hook_letter: str | None,
                 dry_run: bool) -> None:
    raw = file_path.read_text()
    fm, body = parse_frontmatter(raw)

    if fm.get("status", "").strip() == "scheduled":
        print(f"SKIP {file_path.name}: already scheduled "
              f"(label: {fm.get('launchd_label', 'unknown')}). "
              f"Run --unschedule first to reschedule.\n")
        return

    text = build_post_text(body, hook_letter)
    if len(text) > 3000:
        print(f"SKIP {file_path.name}: {len(text)} chars exceeds 3000 limit.")
        return

    label = make_label(file_path)
    plist_path = LAUNCH_AGENTS_DIR / f"{label}.plist"
    slot_str = slot.strftime("%Y-%m-%d %a %I:%M %p MT")

    print("=" * 60)
    print(f"Scheduling: {file_path.name}")
    print(f"Slot:       {slot_str}")
    print(f"Label:      {label}")
    print(f"Plist:      {plist_path}")
    print(f"Length:     {len(text)} characters")
    print("-" * 60)
    print(text)
    print("=" * 60)

    if dry_run:
        print("[--dry-run] Not writing plist or registering with launchd.\n")
        return

    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    LAUNCH_AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    plist_path.write_text(make_plist_xml(label, file_path.resolve(), slot))

    uid = str(os.getuid())
    result = subprocess.run(
        ["launchctl", "bootstrap", f"gui/{uid}", str(plist_path)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        plist_path.unlink(missing_ok=True)
        sys.exit(f"launchctl bootstrap failed:\n{result.stderr}")

    fm["status"] = "scheduled"
    fm["scheduled_for"] = slot_str
    fm["launchd_label"] = label
    file_path.write_text(serialize_frontmatter(fm, body))

    print(f"Scheduled. Plist: {plist_path}\n")


def unschedule_one(file_path: Path, dry_run: bool) -> None:
    raw = file_path.read_text()
    fm, body = parse_frontmatter(raw)

    label = fm.get("launchd_label", "").strip() or make_label(file_path)
    plist_path = LAUNCH_AGENTS_DIR / f"{label}.plist"
    uid = str(os.getuid())

    print(f"Unscheduling: {file_path.name}")
    print(f"Label:        {label}")
    print(f"Plist:        {plist_path}")

    if dry_run:
        print("[--dry-run] Not removing plist or running launchctl.\n")
        return

    result = subprocess.run(
        ["launchctl", "bootout", f"gui/{uid}/{label}"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"  Warning: launchctl bootout returned {result.returncode}: "
              f"{result.stderr.strip()}")
        print("  Continuing with plist removal and frontmatter revert.")

    if plist_path.exists():
        plist_path.unlink()
        print(f"  Deleted: {plist_path}")
    else:
        print(f"  Plist not found (already removed?): {plist_path}")

    for key in ("scheduled_for", "launchd_label"):
        fm.pop(key, None)
    fm["status"] = "draft"
    file_path.write_text(serialize_frontmatter(fm, body))
    print(f"  Reverted to status: draft\n")


# ---------------------------------------------------------------------------
# Resolve draft paths
# ---------------------------------------------------------------------------

def resolve_draft(file_arg: str) -> Path:
    p = Path(file_arg)
    if p.is_absolute() and p.exists():
        return p
    from_cwd = (Path.cwd() / file_arg).resolve()
    if from_cwd.exists():
        return from_cwd
    matches = list(DRAFTS_DIR.glob(f"*{file_arg}*"))
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        names = "\n  ".join(m.name for m in matches)
        sys.exit(f"Ambiguous match for '{file_arg}':\n  {names}\nBe more specific.")
    sys.exit(f"File not found: {file_arg}")


def resolve_image(fm: dict, draft_path: Path | None = None) -> Path | None:
    img = fm.get("image", "").strip()
    if img:
        p = ASSETS_DIR / img
        if not p.exists():
            sys.exit(f"Image not found: {p}\nDrop the file into 05 Content/LinkedIn/assets/")
        return p
    if not draft_path:
        return None
    image_exts = {".jpg", ".jpeg", ".png", ".gif"}
    candidates = [p for p in ASSETS_DIR.iterdir() if p.suffix.lower() in image_exts]
    for p in candidates:
        if p.stem.lower() == draft_path.stem.lower():
            return p
    draft_words = set(draft_path.stem.lower().split("-"))
    for p in candidates:
        image_words = set(re.split(r"[-_ ]+", p.stem.lower()))
        if image_words & draft_words:
            return p
    return None


# ---------------------------------------------------------------------------
# Publish (immediate)
# ---------------------------------------------------------------------------

def publish_one(file_path: Path, hook_letter: str | None, dry_run: bool, env: dict) -> None:
    raw = file_path.read_text()
    fm, body = parse_frontmatter(raw)
    text = build_post_text(body, hook_letter)

    if len(text) > 3000:
        print(f"SKIP {file_path.name}: {len(text)} chars exceeds 3000 limit.")
        return

    image_path = resolve_image(fm, file_path)

    print("=" * 60)
    print(f"Posting:  {file_path.name}")
    print(f"Length:   {len(text)} characters")
    if image_path:
        print(f"Image:    {image_path.name}")
    print("-" * 60)
    print(text)
    print("=" * 60)

    if dry_run:
        print("[--dry-run] Not posting.\n")
        return

    image_urn = upload_image(env, image_path) if image_path else None
    payload = build_payload(env, text, image_urn=image_urn)
    status, headers, body_resp = call_api(env, payload)
    if status != 201:
        print(f"Failed: HTTP {status}\n{body_resp}\n")
        return

    post_urn = headers.get("x-restli-id") or headers.get("X-RestLi-Id") or ""
    linkedin_url = f"https://www.linkedin.com/feed/update/{post_urn}/" if post_urn else ""

    fm["status"] = "published"
    fm["published"] = dt.date.today().isoformat()
    fm["linkedin_url"] = linkedin_url
    if post_urn:
        fm["linkedin_post_urn"] = post_urn

    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    new_path = PUBLISHED_DIR / file_path.name
    new_path.write_text(serialize_frontmatter(fm, body))
    if file_path.resolve() != new_path.resolve():
        file_path.unlink()

    print(f"Published. URN: {post_urn}")
    if linkedin_url:
        print(f"URL:      {linkedin_url}")
    print(f"File:     {new_path}\n")


# ---------------------------------------------------------------------------
# Draft loading
# ---------------------------------------------------------------------------

def load_drafts_ordered() -> list[Path]:
    """All drafts sorted by priority frontmatter, then filename."""
    drafts = []
    for p in DRAFTS_DIR.glob("*.md"):
        raw = p.read_text()
        fm, _ = parse_frontmatter(raw)
        drafts.append((p, fm))
    drafts.sort(key=lambda x: sort_key(x[0], x[1]))
    return [p for p, _ in drafts]


def load_scheduled_drafts() -> list[Path]:
    """All drafts in DRAFTS_DIR with status: scheduled."""
    result = []
    for p in DRAFTS_DIR.glob("*.md"):
        fm, _ = parse_frontmatter(p.read_text())
        if fm.get("status", "").strip() == "scheduled":
            result.append(p)
    return result


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)

    dry_run = "--dry-run" in args
    post_all = "--all" in args
    do_schedule = "--schedule" in args
    do_unschedule = "--unschedule" in args
    hook_letter = None
    if "--hook" in args:
        idx = args.index("--hook")
        hook_letter = args[idx + 1].upper()

    start_date = None
    if "--start" in args:
        idx = args.index("--start")
        start_date = dt.date.fromisoformat(args[idx + 1])

    env = load_env()

    # --- Unschedule path (no LinkedIn token needed) ---
    if do_unschedule:
        if post_all:
            drafts = load_scheduled_drafts()
            if not drafts:
                sys.exit("No scheduled drafts found.")
            for draft in drafts:
                unschedule_one(draft, dry_run)
        else:
            file_arg = next((a for a in args if not a.startswith("--")), None)
            if not file_arg:
                sys.exit("Provide a filename or --all.")
            unschedule_one(resolve_draft(file_arg), dry_run)
        return

    # --- Schedule path (no LinkedIn token needed) ---
    if do_schedule:
        if post_all:
            drafts = load_drafts_ordered()
            if not drafts:
                sys.exit("No drafts found in drafts folder.")
            print(f"Found {len(drafts)} draft(s).\n")
            anchor = start_date or next_monday()
            slots = schedule_slots(anchor)
            for draft in drafts:
                fm_check, _ = parse_frontmatter(draft.read_text())
                if fm_check.get("status", "").strip() == "scheduled":
                    print(f"SKIP {draft.name}: already scheduled.\n")
                    continue
                schedule_one(draft, next(slots), hook_letter, dry_run)
        else:
            file_arg = next((a for a in args if not a.startswith("--")), None)
            if not file_arg:
                sys.exit("Provide a filename or --all.")
            file_path = resolve_draft(file_arg)
            anchor = start_date or dt.date.today()
            slot = next(schedule_slots(anchor))
            schedule_one(file_path, slot, hook_letter, dry_run)
        return

    # --- Immediate publish path (LinkedIn token required) ---
    check_token(env)

    if post_all:
        drafts = load_drafts_ordered()
        if not drafts:
            sys.exit("No drafts found in drafts folder.")
        print(f"Found {len(drafts)} draft(s).\n")
        for draft in drafts:
            publish_one(draft, hook_letter, dry_run, env)
        return

    file_arg = next((a for a in args if not a.startswith("--")), None)
    if not file_arg:
        sys.exit("Provide a filename or --all.")
    publish_one(resolve_draft(file_arg), hook_letter, dry_run, env)


if __name__ == "__main__":
    main()
