---
type: readme
updated: 2026-04-30
---

## What this is

Scripts that publish LinkedIn posts from vault draft files via the LinkedIn REST API. Two pieces:

- `auth.py` — one-time OAuth setup; refreshes tokens when they expire
- `post.py` — reads a draft file, posts it to LinkedIn, moves the file to `published/`

Both read credentials from `.env` (gitignored). See `.env.example` for the schema.

## Files

| File | Purpose |
|---|---|
| `auth.py` | OAuth 2.0 helper. Captures access + refresh tokens, fetches author URN. |
| `post.py` | Publishes a single draft. Updates frontmatter, moves to `published/`. |
| `.env.example` | Template for credentials. Copy to `.env` and fill in. |
| `.env` | Real credentials (gitignored). Created by you + `auth.py`. |

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

## Daily use

After you've reviewed and finalized a draft in `05 Content/LinkedIn/drafts/`:

```bash
cd "00 System/scripts/linkedin"
python3 post.py "../../../05 Content/LinkedIn/drafts/2026-05-04-pillar3-cut-recap-emails.md"
```

The script:
1. Reads frontmatter and body
2. Extracts post text (looks for `## Final Post`, falls back to `## Post Body`)
3. Prints the post for you to review
4. Asks `Post to LinkedIn? [y/N]`
5. On `y`: fires the API call
6. On 201 success: updates frontmatter (`status: published`, `published`, `linkedin_url`) and moves the file to `published/`

## Choosing which hook to use (short-form posts)

Drafts produced by the `linkedin-creator` skill have two hook options. Pick one of these workflows:

**Option A — edit the file:** Add a `## Final Post` section with the exact text you want posted (chosen hook + body merged). The script publishes that.

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
- `--dry-run` always runs without firing the API; use it any time you're unsure
- Posts go live immediately on success — no scheduling, no draft state in LinkedIn

## Troubleshooting

- **HTTP 401 on `post.py`** → token expired; run `auth.py --refresh`
- **HTTP 403 on `post.py`** → app missing `w_member_social` scope; reauthorize after adding the product in LinkedIn Developer console, then re-run `auth.py`
- **OAuth redirect mismatch** → make sure `LINKEDIN_REDIRECT_URI` in `.env` matches exactly what's registered in the LinkedIn app's Auth tab
- **Author URN missing** → re-run `auth.py`; the userinfo call may have failed
