---
type: active-plan
created: 2026-04-30
status: in-progress
owner: Mitchell
---

## Purpose

Wire up direct LinkedIn publishing from the vault. Mitchell drafts posts in `05 Content/LinkedIn/drafts/` (via the `linkedin-creator` skill, manually or via Claude dispatch). When a draft is ready, he runs a local script that posts it to LinkedIn via the REST API, then moves the file to `published/`. No browser automation, no Notion intermediary.

This plan is the handoff document for a fresh Claude Code session that will finish setup once Mitchell has the API credentials.

## Why this approach

Earlier in this thread we ruled out:
- **Chrome MCP for LinkedIn drafting** — the Claude Code Chrome extension is policy-blocked from interacting with LinkedIn
- **Computer use against LinkedIn** — browsers are read-only at the OS level by design
- **Buffer/Taplio as middleware** — adds another tool when the LinkedIn API does the job directly

The LinkedIn REST `/rest/posts` endpoint with `w_member_social` scope publishes posts directly. Mitchell explicitly chose: no scheduling automation yet — he wants to manually trigger publish via Claude Code until he has a stable cadence.

## What's already built (in this session)

- **Folder structure:** `05 Content/LinkedIn/{drafts,published,performance}/` with READMEs documenting filename + frontmatter conventions
- **`linkedin-creator` skill** updated to write drafts to `05 Content/LinkedIn/drafts/` instead of Notion (both short-form and long-form sections updated)
- **`AGENTS.md`** updated to include `05 Content/` in the vault structure, folder roles, and routing rules
- **Posting infrastructure** in `00 System/scripts/linkedin/`:
  - `auth.py` — OAuth 2.0 helper (full flow + `--refresh` mode); writes tokens and author URN to `.env`
  - `post.py` — reads a draft file, extracts the post body, prints it for review, asks for confirmation, fires the API, updates frontmatter, moves file to `published/`. Supports `--dry-run` and `--hook A|B`
  - `.env.example` — credential template
  - `README.md` — full setup and usage docs
- **`.gitignore`** updated to exclude `.env`, token files, and Python bytecode

## What the next session needs to do

The work in this plan is **dependent on Mitchell having LinkedIn API credentials.** Steps below assume credentials exist or are being set up alongside the next session.

### Step 1 — LinkedIn Developer App (Mitchell does this; ~15 minutes)

1. Go to https://developer.linkedin.com/ → create a new app
2. Associate it with a LinkedIn Page (LinkedIn requires this; can be a personal placeholder page)
3. Under **Products**, add:
   - "Sign In with LinkedIn using OpenID Connect" (gives `openid profile` scopes)
   - "Share on LinkedIn" (gives `w_member_social` scope) — this one may require submitting a use-case description; it's typically auto-approved within minutes for personal use, but can take 1-3 days
4. Under **Auth** tab:
   - Add `http://localhost:8000/callback` to Authorized redirect URLs
   - Copy Client ID and Client Secret
5. Wait for `w_member_social` scope to appear under "OAuth 2.0 scopes"

### Step 2 — Local OAuth setup (next session helps Mitchell run this)

```bash
cd "00 System/scripts/linkedin"
cp .env.example .env
# Mitchell pastes Client ID and Client Secret into .env
python3 auth.py
```

This opens a browser for LinkedIn authorization, captures the redirect, exchanges the code for tokens, fetches the author URN, and writes everything to `.env`.

**Verify:**
- `.env` should now contain `LINKEDIN_ACCESS_TOKEN`, `LINKEDIN_REFRESH_TOKEN`, `LINKEDIN_TOKEN_EXPIRES_AT`, and `LINKEDIN_AUTHOR_URN` (formatted `urn:li:person:XXXXX`).

### Step 3 — End-to-end test (next session walks through this)

1. Make sure at least one draft exists in `05 Content/LinkedIn/drafts/`. If not, run the `linkedin-creator` skill to produce one.
2. Dry run:
   ```bash
   python3 post.py "../../../05 Content/LinkedIn/drafts/SOME-DRAFT.md" --dry-run
   ```
   Confirms the script can parse the file and extract the right body. Doesn't fire the API.
3. Live test with a low-stakes post (e.g., a short note Mitchell is happy to delete from LinkedIn after):
   ```bash
   python3 post.py "../../../05 Content/LinkedIn/drafts/SOME-DRAFT.md"
   ```
   Confirm the post appears in Mitchell's LinkedIn feed and the file is moved to `published/` with updated frontmatter (`status: published`, `published: YYYY-MM-DD`, `linkedin_url: ...`).
4. If the test post is undesirable, delete it from LinkedIn manually. The vault file can stay in `published/` — it's a record that the workflow worked.

### Step 4 — Confirm the end-to-end loop works

After a successful test, the workflow is:
1. Mitchell triggers the `linkedin-creator` skill (locally or via dispatch) → draft lands in `05 Content/LinkedIn/drafts/`
2. Mitchell reviews and edits the draft directly in Obsidian. He either:
   - Adds a `## Final Post` section with the exact text he wants posted, or
   - Plans to use `--hook A` or `--hook B` to pick a hook automatically
3. Mitchell runs `python3 post.py path/to/draft.md` → confirms → posts go live → file moves to `published/`
4. Mitchell logs engagement numbers monthly in `05 Content/LinkedIn/performance/YYYY-MM.md`
5. Periodic synthesis: read performance log → propose updates to `.claude/skills/linkedin-creator/SKILL.md`

## Things to verify in the next session

- [ ] LinkedIn Developer App has both "Sign In with LinkedIn" and "Share on LinkedIn" products attached
- [ ] `w_member_social` scope is approved and visible in the app's Auth tab
- [ ] `auth.py` runs cleanly and `.env` is populated end-to-end (token, refresh token, expiry, author URN)
- [ ] `post.py --dry-run` parses a real draft file correctly and shows the expected post text
- [ ] A low-stakes test post lands in LinkedIn and the vault file is moved + frontmatter-updated correctly
- [ ] The `published/` URL in frontmatter actually works (paste in browser to confirm)

## Open questions / things to decide later

- **Token refresh cadence.** LinkedIn access tokens last ~60 days. Refresh tokens last ~365 days. Mitchell should decide if he wants a calendar reminder or a small launchd job to run `auth.py --refresh` periodically. Low priority until the manual workflow is stable.
- **Performance data ingestion.** LinkedIn doesn't expose personal-profile post analytics via API. Mitchell will manually log impressions/comments/saves into `performance/YYYY-MM.md` for now. If this becomes painful, evaluate Shield Analytics or screen-scraping via computer use.
- **Long-form articles.** The Posts API publishes regular feed posts, not LinkedIn Articles. If Mitchell wants to publish full articles via API, that requires a different endpoint (`/rest/articles` or the legacy Publishing API). Out of scope for this plan; long-form drafts in the vault can be copy-pasted into LinkedIn's article editor manually for now.
- **Future automation.** Once Mitchell has a stable cadence, a `scheduled/` folder + launchd job that polls every 15 min and posts when `scheduledAt < now` is a small addition. The current `post.py` is already standalone-callable, so cron just needs a tiny wrapper.

## Files touched in this session

- `05 Content/LinkedIn/README.md` (new)
- `05 Content/LinkedIn/drafts/.gitkeep` (new)
- `05 Content/LinkedIn/published/.gitkeep` (new)
- `05 Content/LinkedIn/performance/README.md` (new)
- `00 System/scripts/linkedin/auth.py` (new)
- `00 System/scripts/linkedin/post.py` (new)
- `00 System/scripts/linkedin/.env.example` (new)
- `00 System/scripts/linkedin/README.md` (new)
- `04 Decisions/Active Plans/LinkedIn API Integration Plan.md` (this file, new)
- `.claude/skills/linkedin-creator/SKILL.md` (modified — Notion save → vault save, both short-form and long-form sections; Tool Integration section)
- `AGENTS.md` (modified — added `05 Content/` to structure, folder roles, and routing rules)
- `.gitignore` (modified — added `.env`, token files, Python bytecode)

## Handoff prompt for the next session

Paste the following into a fresh Claude Code session in this repo:

> I'm picking up the LinkedIn API integration. The plan is in `04 Decisions/Active Plans/LinkedIn API Integration Plan.md`. Read it, confirm the infrastructure (`00 System/scripts/linkedin/`) exists as described, and walk me through Step 2 (OAuth setup) and Step 3 (end-to-end test). I have my LinkedIn Developer App credentials ready.
