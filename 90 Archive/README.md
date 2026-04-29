---
type: archive
---
## What this folder is
The processed graveyard. Raw inbox notes land here after the weekly synthesis pass, organized by month. The durable learning should live in `01 World Model/`, `02 Wiki/`, or `04 Decisions/`; the archive keeps the original record.

## Structure
```
90 Archive/
  2026-04/
    2026-04-19 Example Note.md
  2026-05/
    ...
```

## Rules
- Never edit archived notes. They are a record of what you were thinking at that time.
- Processed archived notes should include `processed_into:` frontmatter pointing to the files that received the distillation.
- Missing `processed_into:` means either the note was noise or it may be under-processed and should be re-examined during synthesis.
- If an archived note turns out to be relevant to a current decision, pull it into the conversation — don't move it back to the inbox.
- Archive folders older than 12 months can be compressed or deleted if the vault gets heavy. The World Model files hold the durable learnings.
