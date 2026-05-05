---
type: template
use: Weekly synthesis session — open this and say "let's do the weekly synthesis" to start
---
## How to use this template
Open a new Claude session in this project and say: "let's do the weekly synthesis."
Claude will read the inbox, triage each note, propose Goldilocks distillations, and move processed notes to the archive unless a source truly deserves preservation.
You approve, adjust, or skip each item. The whole pass should take 20-30 minutes.

---

## Weekly Synthesis Agenda

### 1. Inbox triage (Claude reads 00 Inbox/)
Claude reads every file in the inbox, then for each one asks:

**Step A — Mode check:** "Is this a capture, journal entry, source material, or noise?"
- Captures are ready to process immediately
- Journal entries get Step B first
- Source material gets distilled first; preserve the original only with a named re-retrieval reason
- Noise can archive directly

**Step B — Readiness check (journal entries only):** "Is this ready for synthesis, or do you want to let it sit longer?"
- If ready: process it now
- If not ready: leave it in the inbox untouched, revisit next week

**Step C — Triage (captures + ready journal entries + source material):** For each item ready to process, Claude proposes one of:
- **→ Rule**: Add or update a rule in `01 World Model/02 Rules/Decision Rules.md`
- **→ Context**: Add to or create a file in `01 World Model/03 Contexts/`
- **→ State update**: Update `01 World Model/01 State/Current State.md`
- **→ Review log**: Add a decision or reflection to `01 World Model/04 Reviews/`
- **→ Wiki concept**: Add or update a distilled evergreen note in `02 Wiki/`
- **→ Active decision artifact**: Add or update a memo, plan, or brief in `04 Decisions/`
- **→ Source preservation**: Move to `03 Sources/` only if the original will likely be re-read
- **→ Archive only**: No durable learning, just move it out

Every archived processed note gets `processed_into:` frontmatter listing the destination file(s). Missing `processed_into:` means either noise or possible under-processing.

### 2. State check
Answer these to update Current State.md:
- What is the current email subscriber count?
- What is the biggest single bottleneck this week?
- Did anything shift in priorities, constraints, or risks?
- What did I say yes to this week — was it right?

#### Energy inference rules
The Weekly Brief's energy/focus/stress readings are not vibes — they follow a defined paradigm so every synthesis produces a comparable data point. Over time these readings reveal patterns in how Mitchell's energy correlates with decision quality and execution speed.

Apply these signals in trust order. Higher-numbered signals only break ties when lower-numbered signals are silent or ambiguous.

1. **Direct answer trumps inferred.** If Mitchell states energy/focus/stress directly during the session, use that and stop.
2. **Inbox frontmatter aggregation.** Across this week's processed notes, average the `energy:` field where present. `High` = +1, `Low` = −1, blank = 0. A clear positive or negative average sets the baseline.
3. **Movement vs. Stalled ratio.** From Step 1's triage results plus Step 2's answers: count Movement items vs. Stalled items. ≥2:1 in favor of movement = energy holds or rises. Reverse ratio = energy lower than baseline.
4. **Avoidance signal.** If the "What I'm avoiding" answer names "activation energy," "fear," "don't want to," or similar phrasing, focus drops by 1 step and stress rises by 1 step.
5. **Surprise polarity.** Net-positive surprises bias energy up; net-negative surprises bias it down. A surprise income event reads positive; a missed deadline reads negative.
6. **Capture velocity.** Count of inbox notes processed this week. Significantly above or below the rolling baseline is a focus signal worth flagging — high volume can mean either active engagement or scattered attention; weigh against signals 1–5.

**When signals conflict, surface both in the brief instead of averaging silently.** Example: "Energy reads medium from direct answer, but movement ratio was 3:2 stalled — worth watching whether the felt energy is overstating actual capacity."

**Improving the rules:** If a brief's reading doesn't match how the week actually felt, the rule that misfired is what gets updated. Note the mismatch in the next brief's "Patterns I notice" section so the paradigm sharpens over time.

### 3. Rules audit (brief)
- Did any rule prove wrong or outdated this week?
- Did anything happen that should graduate a provisional rule to durable?

### 4. Open questions
- Are there decisions coming up that the World Model isn't ready to support yet?
- What situation file is missing that keeps coming up?

### 5. Close
- Claude archives processed inbox notes to `90 Archive/YYYY-MM/`
- Replace the `inbox` tag with `archived` in each archived note
- Claude proposes any `AGENTS.md` updates if the system itself needs to change
- Note what got smarter this week

### 6. Weekly Brief (mandatory)
Every synthesis session ends with a Weekly Brief. This is the longitudinal travel log — the record the AI reads across sessions to detect patterns, flag drift, and make better predictions over time.

Claude creates a new file at `04 Decisions/Weekly Briefs/YYYY-MM-DD Weekly Brief.md` using the template at `00 System/Templates/Weekly Brief.md`.

Most fields can be filled from answers already given during this session:
- State snapshot → from Step 2 (State check) and Current State.md
- Priorities → from Step 2
- Bottleneck → from Step 2
- Decisions → from Step 1 (Inbox triage) and Step 3 (Rules audit)
- Open questions → from Step 4

Ask Mitchell these additional questions to complete the brief:
1. **What actually moved this week?** (1-3 things that advanced)
2. **What stalled?** (was on the list, didn't happen)
3. **What are you avoiding right now?** (the honest answer, not the diplomatic one)
4. **What surprised you this week?** (good or bad)

Then write the file. Do not ask for approval on individual fields — draft the whole brief and present it for a single pass of edits before saving.

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
