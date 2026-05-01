---
type: readme
updated: 2026-04-30
---

## What this folder is

Monthly performance logs for LinkedIn posts. Each file is a record of which posts ran in a given month, how they performed, and what patterns emerged. These files are the input for periodic synthesis sessions that propose updates to the `linkedin-creator` skill.

## File naming

`YYYY-MM.md` — one file per month.

## Template

```markdown
---
type: linkedin-performance-log
month: 2026-05
created: 2026-05-31
---

## Posts published this month

| Date | File | Pillar | Impressions | Comments | Saves | Reactions | Notes |
|---|---|---|---|---|---|---|---|
| 2026-05-04 | 2026-05-04-pillar3-cut-recap-emails | 3 | 4,200 | 18 | 31 | 89 | High save rate — mini-win format works |
| 2026-05-06 | 2026-05-06-pillar2-prompts-arent-the-problem | 2 | 1,100 | 3 | 4 | 22 | Reframe didn't land — too abstract |

## What worked

- [Specific patterns from posts that overperformed]

## What didn't

- [Specific patterns from posts that underperformed]

## Proposed skill updates

- [Specific edits to suggest for `.claude/skills/linkedin-creator/SKILL.md`]

## Open questions

- [Hypotheses to test next month]
```

## How to fill this in

After a post has been live for ~7 days, LinkedIn shows its analytics. Pull the four numbers (impressions, comments, saves, reactions) and add the row.

At the end of the month, write the synthesis sections. The "Proposed skill updates" section is the bridge — those edits get applied to the skill file in a focused review session.
