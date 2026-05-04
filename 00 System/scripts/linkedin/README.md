---
type: readme
updated: 2026-05-04
---

## What this is

Scripts that publish LinkedIn posts from vault draft files via the LinkedIn REST API. Two pieces:

- `auth.py` — one-time OAuth setup; refreshes tokens when they expire
- `post.py` — reads a draft file, posts it to LinkedIn (or schedules it via launchd)

Both read credentials from `.env` (gitignored). See `.env.example` for the schema.

## Files

| File | Purpose |
|---|---|
| `auth.py` | OAuth 2.0 helper. Captures access + refresh tokens, fetches author URN. |
| `post.py` | Publishes a single draft immediately, or schedules it via a launchd job. |
| `.env.example` | Template for credentials. Copy to `.env` and fill in. |
| `.env` | Real credentials (gitignored). Created by you + `auth.py`. |
| `logs/` | stdout/stderr logs from launchd-fired jobs. Gitignored. |

## Setup (first time)

1. **Create a LinkedIn Developer App** at https://developer.linkedin.com/
   - Add the "Sign In with LinkedIn using OpenID Connect" product
   - Add the "Share on LinkedIn" product (gives `w_member_social` scope)
   - Under Auth → Authorized redirect URLs, add: `http://localhost:8000/callback`
   - Copy the Client ID and Client Secret

2. **Configure `.env`:**
   ```bash
   cd "00 System/scripts/linkedin"
   cp .env.example .env
   # Edit .env — fill in LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET
   ```

3. **Run the OAuth flow:**
   ```bash
   python3 auth.py
   ```
   This opens your browser to LinkedIn, captures the auth code on a localhost callback, exchanges it for tokens, fetches your author URN, and writes everything back to `.env`.

4. **Test with a dry run:**
   ```bash
   python3 post.py "../../../05 Content/LinkedIn/drafts/SOME-FILE.md" --dry-run
   ```

## Posting immediately

After you've reviewed and finalized a draft in `05 Content/LinkedIn/drafts/`:

```bash
cd "00 System/scripts/linkedin"
python3 post.py "../../../05 Content/LinkedIn/drafts/2026-05-04-my-post.md"
```

The script:
1. Reads frontmatter and body
2. Extracts post text (looks for `## Final Post`, falls back to `## Post Body`)
3. Prints the post for review
4. Fires the LinkedIn API call
5. On 201 success: updates frontmatter (`status: published`, `published`, `linkedin_url`) and moves the file to `published/`

## Scheduling a post

```bash
# Schedule all unscheduled drafts (Mon/Tue/Thu/Fri at 8 AM MT)
python3 post.py --all --schedule

# Start from a specific date instead of the next Monday
python3 post.py --all --schedule --start 2026-05-12

# Schedule a single draft
python3 post.py "my-draft.md" --schedule --start 2026-05-07
```

Scheduling does **not** use LinkedIn's API. Instead, the script:
1. Picks a slot from the Mon/Tue/Thu/Fri 8 AM MT cadence
2. Writes a launchd plist to `~/Library/LaunchAgents/com.mitchell.linkedin.<slug>.plist`
3. Registers it with `launchctl bootstrap`
4. Updates the draft's frontmatter: `status: scheduled`, `scheduled_for`, `launchd_label`

When the job fires at the scheduled time, it calls `post.py` directly to publish immediately.

Dry-run with `--dry-run` previews the slot, label, plist path, and post text without writing anything.

## Unscheduling a post

```bash
# Unschedule a specific draft
python3 post.py "my-draft.md" --unschedule

# Unschedule all scheduled drafts
python3 post.py --all --unschedule
```

Unscheduling:
1. Runs `launchctl bootout` to deregister the job
2. Deletes the plist from `~/Library/LaunchAgents/`
3. Reverts the draft's frontmatter to `status: draft`, removing `scheduled_for` and `launchd_label`

## Choosing which hook to use (short-form posts)

Drafts produced by the `linkedin-creator` skill have two hook options. Pick one of these workflows:

**Option A — add a Final Post section:** Add a `## Final Post` section with the exact text you want posted (chosen hook + body merged). The script publishes that.

**Option B — pass a hook flag:**
```bash
python3 post.py path/to/draft.md --hook A
```
Concatenates Hook A with the Post Body section.

Long-form articles use `## Article Body` and don't need a hook flag.

## Token refresh

LinkedIn access tokens expire (~60 days). When `post.py` errors with "token expired":

```bash
python3 auth.py --refresh
```

Uses the stored refresh token to get a new access token without going through the browser flow. If the refresh token has also expired, run `python3 auth.py` for the full flow.

## Safety notes

- `.env` is in `.gitignore` at the vault root — never commit it
- The script enforces LinkedIn's 3000-character limit before posting
- `--dry-run` always previews without posting or writing plists; use it any time you're unsure
- Posts go live immediately on success — launchd fires the immediate-publish path at the scheduled time
- LinkedIn's REST API does not support member-account post scheduling; `--schedule` uses launchd as the local workaround

## Troubleshooting

- **HTTP 401 on `post.py`** → token expired; run `auth.py --refresh`
- **HTTP 403 on `post.py`** → app missing `w_member_social` scope; reauthorize after adding the product in LinkedIn Developer console, then re-run `auth.py`
- **OAuth redirect mismatch** → make sure `LINKEDIN_REDIRECT_URI` in `.env` matches exactly what's registered in the LinkedIn app's Auth tab
- **Author URN missing** → re-run `auth.py`; the userinfo call may have failed
- **launchd job didn't fire** → check `logs/<label>.err`; also confirm the Mac was awake at fire time (launchd fires missed calendar-interval jobs on next wake if the system was asleep)
- **`launchctl bootstrap` fails** → a job with that label may already be registered; run `--unschedule` first, then reschedule
