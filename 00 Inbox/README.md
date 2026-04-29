---
type: inbox
---
## What this folder is
The raw dump zone. No structure required. Write anything here — fleeting thoughts, things you noticed, article takeaways, decisions you made informally, ideas you want to evaluate, frustrations, questions, observations.

## Three modes of writing — all belong here

**Captures** — quick observations, things you noticed, ideas to evaluate, articles that changed your thinking. Usually short. Often a sentence or a few bullets. Ready to process as soon as you write them.

**Journal entries** — reflections, processing, thinking out loud about a decision, a week, a feeling, a friction point. Usually longer. These benefit from sitting a few days before synthesis — a thought written Monday often looks different by Friday.

**Source material** — article clippings, meeting notes, podcast takeaways, chat outputs, research scratch, or anything upstream that may contain reusable signal.

Tags are optional but helpful. Add them when you know the type: `#capture`, `#journal`, `#source`, `#feedback`, `#idea`, `#clipping`. The weekly synthesis uses these as routing signals. No tag is also fine — the agent will infer from content.

## What belongs here
- A thought you had in the shower that felt important
- A principle you intuited but haven't verified yet
- A decision you made without a clear rule to back it up
- Something you read that changed how you think about a problem
- A pattern you noticed in your work or behavior
- A journal entry about how a week went, a decision you're processing, or something that's sitting with you

## What does NOT belong here
- Completed decisions with known outcomes (those go in `01 World Model/04 Reviews/`)
- Things you're certain about and already act on (those go in `01 World Model/02 Rules/`)
- Recurring scenarios you've already mapped (those go in `01 World Model/03 Contexts/`)

## How it works
1. Write anything here, any time, any format — especially from your phone via Obsidian mobile
2. Once a week, open a Claude session and say "let's do the weekly synthesis"
3. Claude reads everything in the inbox and applies the routing question: capture, journal entry, source material, or noise?
4. The first-class output is a Goldilocks distillation into `01 World Model/`, `02 Wiki/`, or `04 Decisions/` — not preservation for its own sake.
5. Source material moves to `03 Sources/` only when the original is likely to be re-read. Otherwise, the distilled learning goes to the right file and the source is archived.
6. Processed notes move to `90 Archive/YYYY-MM/` with `processed_into:` frontmatter listing the destination files.
7. Unready journal entries stay in the inbox untouched.
8. The World Model gets smarter without bloating.

## Format
No format required. Title files by date or topic — whatever you'll actually do on your phone.
`YYYY-MM-DD Topic.md` works well if you want order, but anything is fine.

Tags are optional but make routing faster: `#capture`, `#journal`, `#source`, `#feedback`, `#idea`, `#clipping`
