---
type: readme
updated: 2026-04-30
---

## What this folder is

The working queue and historical record for LinkedIn content. Replaces the previous Notion Content Tracker. This is the source of truth for every LinkedIn post Mitchell drafts, publishes, and learns from.

The `linkedin-creator` skill writes drafts here automatically. Mitchell reviews, edits, and manually schedules in LinkedIn. Performance data flows back into this folder once a month.

## Folder roles

- **`drafts/`** — New posts produced by the `linkedin-creator` skill. Mitchell reviews these and edits before posting. A draft stays here until it has been posted in LinkedIn.
- **`published/`** — Posts that have been published in LinkedIn. Move the file here from `drafts/` after posting and update frontmatter with `published` date and the LinkedIn post URL.
- **`performance/`** — Monthly performance logs. One file per month (`YYYY-MM.md`) with engagement data per post and synthesis observations that feed skill improvements.

## File naming convention

`YYYY-MM-DD-pillar{N}-{kebab-case-slug}.md`

Examples:
- `2026-05-04-pillar3-cut-recap-emails.md`
- `2026-05-06-pillar2-prompts-arent-the-problem.md`

Long-form articles use `article` instead of `pillar{N}`:
- `2026-05-08-article-name-the-pain.md`

The date is the **drafted date**, not the published date. Once published, the `published` field in frontmatter records the actual post date.

## Frontmatter

Every post file uses this frontmatter:

```yaml
---
type: linkedin-post
content_type: short-form          # short-form | long-form-article
pillar: 3                          # 1-6 for short-form, omit for articles
status: draft                      # draft | published
created: 2026-05-04
published: null                    # YYYY-MM-DD when posted
linkedin_url: null                 # URL of the live post
---
```

After publishing, update:
- `status: published`
- `published: YYYY-MM-DD`
- `linkedin_url: https://...`

## Body structure

Short-form posts contain three sections (produced by the skill):
- `## Hook Options` — A and B variants
- `## Post Body` — the actual post copy
- `## Post Notes` — pillar, pain points, CTA type, visual recommendation, quality gate confirmations

Long-form articles use:
- `## Headline Options`
- `## Article Body`
- `## Article Notes`

## Performance loop

Once per month, create a new file in `performance/YYYY-MM.md` that logs the engagement numbers for each post published that month and any patterns worth feeding back into the skill. See `performance/README.md` for the template.
