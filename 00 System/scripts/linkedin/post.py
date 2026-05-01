#!/usr/bin/env python3
"""
Publish a LinkedIn post from a draft file in the vault.

Reads a markdown file from `05 Content/LinkedIn/drafts/`, extracts the post
body, posts to LinkedIn via the REST API, then updates frontmatter and moves
the file to `05 Content/LinkedIn/published/`.

Usage:
    python3 post.py <path-to-draft.md>           # publishes immediately
    python3 post.py <path-to-draft.md> --dry-run # prints what would post, doesn't fire
    python3 post.py <path-to-draft.md> --hook A  # short-form: use Hook A (default uses ## Final Post if present)

The draft file should contain a `## Final Post` section with the exact text to
publish. If absent, the script falls back to `## Post Body` and (for short-form)
prepends the chosen hook.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
VAULT_ROOT = SCRIPT_DIR.parent.parent.parent
ENV_PATH = SCRIPT_DIR / ".env"

DRAFTS_DIR = VAULT_ROOT / "05 Content" / "LinkedIn" / "drafts"
PUBLISHED_DIR = VAULT_ROOT / "05 Content" / "LinkedIn" / "published"

POSTS_API = "https://api.linkedin.com/rest/posts"
LINKEDIN_VERSION = "202504"


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


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 4 :].lstrip("\n")
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


def post_to_linkedin(env: dict, text: str) -> tuple[int, dict, str]:
    payload = {
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


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)

    file_arg = args[0]
    dry_run = "--dry-run" in args
    hook_letter = None
    if "--hook" in args:
        idx = args.index("--hook")
        hook_letter = args[idx + 1].upper()

    file_path = Path(file_arg)
    if not file_path.is_absolute():
        file_path = (Path.cwd() / file_arg).resolve()
    if not file_path.exists():
        sys.exit(f"File not found: {file_path}")

    env = load_env()
    check_token(env)

    raw = file_path.read_text()
    fm, body = parse_frontmatter(raw)
    text = build_post_text(body, hook_letter)

    if len(text) > 3000:
        sys.exit(f"Post text is {len(text)} characters; LinkedIn limit is 3000.")

    print("=" * 60)
    print(f"Posting from: {file_path.name}")
    print(f"Length: {len(text)} characters")
    print("-" * 60)
    print(text)
    print("=" * 60)

    if dry_run:
        print("\n[--dry-run] Not posting.")
        return

    confirm = input("\nPost to LinkedIn? [y/N]: ").strip().lower()
    if confirm != "y":
        print("Aborted.")
        return

    status, headers, body_resp = post_to_linkedin(env, text)
    if status != 201:
        print(f"\nFailed: HTTP {status}")
        print(body_resp)
        sys.exit(1)

    post_urn = headers.get("x-restli-id") or headers.get("X-RestLi-Id") or ""
    post_id = post_urn.split(":")[-1] if post_urn else ""
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

    print(f"\nPublished. URN: {post_urn}")
    if linkedin_url:
        print(f"URL: {linkedin_url}")
    print(f"File moved to: {new_path}")


if __name__ == "__main__":
    main()
