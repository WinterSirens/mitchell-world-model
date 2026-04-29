---
type: template
use: Weekly synthesis session — open this and say "let's do the weekly synthesis" to start
---
## How to use this template
Open a new Claude session in this project and say: "let's do the weekly synthesis."
Claude will read the inbox, triage each note, propose file updates, and move processed notes to the archive.
You approve, adjust, or skip each item. The whole pass should take 20-30 minutes.

---

## Weekly Synthesis Agenda

### 1. Inbox triage (Claude reads 00 Inbox/)
Claude reads every file in the inbox, then for each one asks:

**Step A — Mode check:** "Is this a capture or a journal entry?"
- Captures are ready to process immediately
- Journal entries get Step B first

**Step B — Readiness check (journal entries only):** "Is this ready for synthesis, or do you want to let it sit longer?"
- If ready: process it now
- If not ready: leave it in the inbox untouched, revisit next week

**Step C — Triage (captures + ready journal entries):** For each item ready to process, Claude proposes one of:
- **→ Rule**: Add or update a rule in `02 Rules/Decision Rules.md`
- **→ Situation**: Add to or create a file in `03 Situations/`
- **→ State update**: Update `01 State/Current State.md`
- **→ Review log**: Add a decision or reflection to `04 Reviews/`
- **→ Archive only**: No durable learning, just move it out

### 2. State check
Answer these to update Current State.md:
- What is the current email subscriber count?
- What is the biggest single bottleneck this week?
- Did anything shift in priorities, constraints, or risks?
- What did I say yes to this week — was it right?

### 3. Rules audit (brief)
- Did any rule prove wrong or outdated this week?
- Did anything happen that should graduate a provisional rule to durable?

### 4. Open questions
- Are there decisions coming up that the World Model isn't ready to support yet?
- What situation file is missing that keeps coming up?

### 5. Close
- Claude archives processed inbox notes to `06 Archive/YYYY-MM/`
- Replace the `inbox` label with `Archived`tag from the `tags` field property from each note archived
- Claude proposes any CLAUDE.md updates if the system itself needs to change
- Note what got smarter this week

---

## Signals the synthesis is working
- Inbox empties weekly
- Rules feel sharper and more specific over time
- Situations files get used in real decisions
- You trust the system enough to actually open it when a decision comes up

## Signals it's drifting
- Inbox is growing faster than it's being processed
- You're writing rules based on one bad week
- Synthesis sessions are taking over an hour (too much in the inbox)
- Files are growing without decisions improving
