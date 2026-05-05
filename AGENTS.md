## Purpose

This vault is the canonical workspace for my Personal World Model and knowledge system. Use it to help me make better decisions, update my rules based on evidence, keep my current state and review history organized, and build a compounding knowledge base over time.

The system compounds with use. Every decision logged, every synthesis pass, every rule added or invalidated, and every piece of knowledge distilled makes the next conversation more useful.

## Startup behavior

For every new task in this project:

1. Read this AGENTS.md file first.
2. Treat this file as the operating manual for the project.
3. Read any relevant files before making recommendations or edits.
4. Use project memory as supporting context, not as source of truth when it conflicts with markdown files.
5. Check `.claude/skills/` for project-specific skills. If a task matches a skill in this directory, read its `SKILL.md` and apply its instructions even if it does not appear in the auto-discovered skill list.

## Project skills

This project maintains custom agent skills in `.claude/skills/`. These are executable skill definitions that extend the agent's capabilities for this vault specifically. They are active and should be used when their trigger conditions are met.

Current custom skills in this repo:
- `ai-prd-builder` — Build PRDs for internal AI solutions and automations.
- `email-sequence` — Draft single emails and multi-email sequences.
- `linkedin-creator` — Create LinkedIn posts and articles.
- `notion-capture` — Capture and route content into Notion.
- `plugin-security-audit` — Audit third-party plugins/MCP servers before installation.
- `red-teaming` — Run adversarial testing against prompts, skills, agents, and plugins.
- `rewrite-comms` — Rewrite communication in Mitchell's authentic voice.

Always treat `.claude/skills/` as the live source of truth, since this list may change over time.

## Source of truth

- Markdown files in this vault are the source of truth.
- Project memory is helpful but secondary.
- If memory conflicts with files, trust the files.
- Never invent personal facts, goals, preferences, or rules that are not supported by the files or current conversation.

## Knowledge layers

This system draws on four layers of knowledge. Use them in this order:

1. **World Model files** (`01 World Model/`) — personal context, current state, decision rules, context playbooks, and accumulated learnings. Always check these first. They represent what is true for Mitchell specifically.

2. **Wiki files** (`02 Wiki/`) — processed, permanent knowledge for retrieval. Distilled frameworks, synthesized concepts, reference material, and evergreen notes that inform decisions across all domains. Use them to enrich reasoning, not to override World Model state.

3. **Agent training knowledge** — frameworks, established best practices, domain knowledge through the model cutoff. Use this to fill gaps the files don't cover and to reason across general principles.

4. **Web search** — use for anything time-sensitive, post-cutoff, or where current data matters (market stats, recent research, pricing benchmarks, platform changes). Always search before citing a specific statistic or claiming something is current. Label web-sourced information clearly.

When these layers conflict, trust the files first, then flag the conflict.

## Vault structure

```
.claude/skills
00 Inbox/
00 System/
  Templates/
  scripts/
01 World Model/
  01 State/
  02 Rules/
  03 Contexts/
  04 Reviews/
02 Wiki/
  Concepts/
  Projects/
  People/
  Themes/
  Syntheses/
03 Sources/
  Articles/
  Podcasts/
  Meetings/
  Chats/
  Research Notes/
04 Decisions/
  Weekly Briefs/
  Decision Memos/
  Active Plans/
05 Content/
  LinkedIn/
    drafts/
    published/
    performance/
90 Archive/
  YYYY-MM/
AGENTS.md
CLAUDE.md
README.md
```

### Folder roles

**`00 Inbox/`** — flat dump zone. No subfolders, no pre-sorting. Everything new lands here first: fleeting thoughts, captures, observations, web clippings, feedback, journal entries, meeting notes, research scratches. No structure required. The synthesis agent determines input type from frontmatter, tags, or semantic content. Processed weekly.

**`00 System/`** — vault infrastructure. Templates, folder documentation, and other operating-layer files. Not personal content — this is the operating layer of the system itself.
- `Templates/` — blank templates for new entries, including Obsidian Templater templates with `<% ... %>` syntax. This is where Obsidian and Templater are configured to look for templates.
- `scripts/` — project utilities and automations. (Currently empty — the LinkedIn publishing scripts were removed when API autopublishing was retired.)

**`01 World Model/`** — the personal operating system. This is where Mitchell's current state, decision rules, recurring context patterns, and review history live. It is the active decision-support layer, not a reference archive. Keep this small, high-trust, and decision-relevant. It is the lens, not the warehouse.
- `01 State/` — current conditions snapshot. Holds `Current State.md` which tracks present priorities, constraints, active risks, bottleneck, and open questions. Update when conditions materially change. No log trail needed — weekly synthesis in Reviews captures state evolution over time.
- `02 Rules/` — durable and provisional decision rules. Holds `Decision Rules.md` which is the canonical rule file. Rules are judged by their evidence history, so this file maintains a change log. Update when a rule is added, revised, invalidated, or promoted from provisional to durable.
- `03 Contexts/` — recurring scenarios and reusable decision patterns. Each file is a reference playbook for a specific context (e.g., evaluating a new opportunity, managing capacity, creating LinkedIn content, the Stuck Implementer audience profile). Only the current playbook matters — use `updated:` frontmatter, no log trail.
- `04 Reviews/` — logs, retrospectives, decision outcomes, and evidence-based updates. Each entry is a timestamped record by definition. This is where the system captures what actually happened versus what was predicted, and surfaces rule updates.

**`02 Wiki/`** — permanent knowledge base for retrieval. Distilled frameworks, atomic notes, reference material, synthesized concepts. The goal is high-quality retrievable knowledge, not raw capture. Files here should be processed, linked, and evergreen. Do not put ephemeral state or personal decisions here. Use the `updated:` frontmatter field when a note is revised.
- `Concepts/` — distilled, reusable reference knowledge (e.g., LLM model selection guide, leadership frameworks).
- `Projects/` — evergreen notes about ongoing or completed projects worth preserving beyond the active decision layer.
- `People/` — notes about individuals relevant to decisions, patterns, or relationships.
- `Themes/` — cross-cutting themes and patterns that recur across domains.
- `Syntheses/` — longer synthesized artifacts that combine multiple sources or concepts into a cohesive view.

**`03 Sources/`** — preserved upstream material whose original form is likely to be useful again. This is not a second archive — the default is distill then archive. Preserve a source here only when you can name a specific re-retrieval reason. Do not put synthesis or personal conclusions here — those belong in `02 Wiki/` or `01 World Model/`.
- `Articles/` — preserved web articles and clippings worth re-reading after synthesis.
- `Podcasts/` — podcast notes or transcripts worth reusing.
- `Meetings/` — meeting notes worth preserving as source material.
- `Chats/` — notable AI conversation outputs worth revisiting.
- `Research Notes/` — deeper research artifacts backing specific decisions (e.g., market analysis, competitive teardowns).

**`04 Decisions/`** — active and recent decision artifacts. Separate from Reviews (which are retrospective) — this layer holds forward-looking decision support.
- `Weekly Briefs/` — longitudinal travel log. One file per week, created at the close of every weekly synthesis. Each brief captures a consistent snapshot: state, priorities, bottleneck, what moved, what stalled, decisions made, and what Mitchell is avoiding. Over time this log enables pattern detection — recurring bottlenecks, decision tendencies, energy cycles, drift signals — and gives the AI historical context to make better predictions across sessions.
- `Decision Memos/` — structured decision write-ups for significant choices.
- `Active Plans/` — current execution plans worth tracking (not long-term archive).

**`05 Content/`** — working queue and historical record for content Mitchell produces (currently LinkedIn). Replaces the old Notion Content Tracker. The `linkedin-creator` skill writes drafts directly into `05 Content/LinkedIn/drafts/`. Mitchell reviews, edits, and manually schedules to LinkedIn. Files move to `published/` after posting. Monthly performance logs live in `performance/YYYY-MM.md` and feed skill-improvement reviews. See `05 Content/LinkedIn/README.md` for the full convention.

**`90 Archive/`** — processed graveyard. Inbox notes land here after weekly synthesis, organized by `YYYY-MM/` subfolder. Never edit archived notes — they are a record of what was true at that time.

**`Personal World Model/`** — legacy folder used in older Cowork-based setups. It is currently absent in this repo; if it appears in another clone, do not rename or move it.

## Path normalization notes

Some older notes still use path names from previous vault structures. Normalize them as follows when reading references:
- `01 World Model/03 Situations/...` → `01 World Model/03 Contexts/...`
- `02 Brain/Research/...` → `03 Sources/Research Notes/...`

## Note routing rules

When classifying or moving a note, use this routing logic. Prefer explicit reasoning about the destination over auto-dumping.

- If it's **about Mitchell** (identity, goals, constraints, state, rules, context patterns) → `01 World Model/`
- If it's **durable synthesized knowledge** (frameworks, concepts, evergreen reference) → `02 Wiki/`
- If it's **raw upstream material** (source articles, research, meeting notes, chats) → `03 Sources/`
- If it **changes what Mitchell should do next** (decision memos, plans, weekly briefs) → `04 Decisions/`
- If it's **a content draft for LinkedIn** (or other channels Mitchell publishes to) → `05 Content/`
- If it's **unprocessed** → `00 Inbox/` until the weekly synthesis handles it
- If **unsure**: do not guess. Flag the ambiguity and ask, or park it in `00 Inbox/` with a note.

## Weekly synthesis workflow

Once a week, open a session and say "let's do the weekly synthesis." Agent reads `00 Inbox/`, triages each note, proposes updates to the correct files, and moves processed notes to `90 Archive/YYYY-MM/`. See `00 System/Templates/Weekly Synthesis.md` for the full agenda.

**Processing `00 Inbox/` files** — for each file directly in `00 Inbox/` (flat, no subfolders), determine input type from frontmatter, tags, or content. If the note contains tags (e.g., `#feedback`, `#journal`, `#clipping`, `#idea`) or labels in the body, treat them as explicit routing signals and factor them into the decision tree.

Then apply the appropriate branch of this 4-way decision tree:

1. **Capture** (fleeting thought, observation, idea worth evaluating, feedback received) → distill into the right `01 World Model/`, `02 Wiki/`, or `04 Decisions/` file. Archive the original with `processed_into:` listing destinations.
   - *Feedback* is a capture variant: external perspectives on you or your work. Often maps to `01 World Model/` (state updates, rule adjustments) or `02 Wiki/People/` (relationship patterns).
2. **Source material** (meeting notes, podcast takeaway, chat output, research scratch, web clippings) → distill any insight to the right file first. Then ask: will I re-read this source itself? If yes, move to `03 Sources/{subfolder}/`. If no, archive with `processed_into:`. Source preservation is the exception, not the default.
   - *Clippings* are a source material variant: pre-structured external articles with frontmatter (`title`, `source`, `author`, `published`, `created`, `description`, `tags: clippings`). Read the article body, identify the key insight, then decide destination: `02 Wiki/`, `01 World Model/03 Contexts/`, `03 Sources/Articles/`, or archive.
3. **Journal entry** (reflection, processing, thinking out loud) → synthesize if ready; leave if it needs to settle. Archive only after synthesis with `processed_into:`.
4. **Noise** (no extractable signal) → archive directly. No `processed_into:` field — its absence flags the note as either noise or under-processed.

Do not treat clippings or feedback as raw thought — they are input material to extract from, not personal state to preserve.

### Action triage (second pass — tag-driven)

Distillation captures the *learning* from a note. Action triage decides whether the note also requires a *work artifact* — something concrete that needs to exist after this synthesis. Run this pass for every Capture and every ready Journal entry.

The note's tags and `type` frontmatter are the primary signal for what action is required. Read them first, then confirm against the content. The inbox is both a knowledge channel *and* a work channel — tags declare intent, the agent executes.

**Action axis (a single note can hit multiple):**

1. **Knowledge-only** — distillation already handled it; no artifact needed. (Default; most notes.)
2. **Wiki concept** — durable, evergreen, retrievable knowledge → create or update a note in `02 Wiki/`.
3. **Decision artifact** — opens or advances a real decision → memo in `04 Decisions/Decision Memos/` or plan in `04 Decisions/Active Plans/`.
4. **World Model update** — changes Mitchell's current state, rules, or context playbooks → update `01 World Model/01 State/`, `02 Rules/`, or `03 Contexts/`.
5. **Skill trigger** — the note's content is the *input* to a project skill that should produce a downstream artifact. Invoke the matching skill and route output to the correct folder.
6. **Skill update** — the note is *feedback on how a skill behaves* (workflow change, performance data) → modify the relevant `.claude/skills/.../SKILL.md` and log the change in the Weekly Brief.

**Known tag → action conventions:**

- `linkedin-idea`, `linkedin` → skill trigger: `linkedin-creator` → draft in `05 Content/LinkedIn/drafts/`
- `prd-trigger`, `prd` → skill trigger: `ai-prd-builder`
- `email-draft`, `email-sequence` → skill trigger: `email-sequence`
- `comms-rewrite` → skill trigger: `rewrite-comms`
- `notion-capture` → skill trigger: `notion-capture`
- `plugin-audit`, `mcp-install` → skill trigger: `plugin-security-audit`
- `red-team` → skill trigger: `red-teaming`
- `research-trigger` → decision artifact (Decision Memo or Active Plan) + queue deep research
- `decision-making` → if a real open decision exists, decision artifact; otherwise capture
- `feedback` → world-model update (rules/state); if it's feedback on a skill, skill update
- `clipping` → source-material branch (distill, preserve only with re-retrieval reason)
- `journal` → readiness check first; then capture or leave
- `idea` → capture; check whether it's also a content idea worth handing to a skill
- `raw`, `inbox` → no action signal; treat as untagged

**Unknown tag rule:**

If a note carries a tag or `type` value not in the list above, do **not** guess silently. Surface the unknown tag in the triage summary with your best read of what work it implies (e.g., "`vendor-eval` — should this trigger `plugin-security-audit`?"). Once Mitchell confirms or corrects, append the new convention to the list in this section so the system gets smarter every week. Treat this as a standing instruction: every unfamiliar tag is an opportunity to extend the system.

Surface every triggered action in the triage summary alongside the distillation. Approval is given per row — Mitchell can accept distillation but reject the artifact (or vice versa).

**Energy inference:** Energy/focus/stress readings on the Weekly Brief follow a defined paradigm so they're a comparable data point across weeks, not vibes. See `00 System/Templates/Weekly Synthesis.md` → "Energy inference rules" for the trust order and signals.

The synthesis is the mechanism that makes the system compound. Without it, the inbox fills and the World Model goes stale.

## Parallel inbox processing (multi-agent)

During a Weekly Synthesis session, process all inbox items in parallel by spawning one sub-agent per file rather than handling them sequentially.

**Orchestrator responsibilities:**

1. List every file directly in `00 Inbox/` (flat, no subfolders).
2. Spawn one sub-agent per file simultaneously, passing each sub-agent:
   - The full file path and its raw content.
   - The complete 4-way decision tree from the section above.
   - The routing rules and Goldilocks distillation guidelines from this file.
   - Instruction to return a structured result object (see format below).
3. Collect all sub-agent results once they finish.
4. Present a consolidated triage summary to Mitchell — one row per file — for a single approval pass.
5. After approval, apply all writes, moves, and archival operations (these must run sequentially per file to avoid conflicts on shared destination files like `Decision Rules.md` or `Current State.md`).

**Sub-agent instruction template** (issue this to each spawned agent):

> You are processing a single inbox note during a Weekly Synthesis. Your job is to classify the note and propose a distilled output — do not write any files. Return a structured result only.
>
> File path: `<path>`
> File content: `<content>`
>
> Apply the 4-way decision tree (capture / source material / journal entry / noise). Then return:
> - `type`: one of `capture`, `source_material`, `journal_entry`, `noise`
> - `ready`: `true` or `false` (for journal entries: is it ready to synthesize now?)
> - `destination`: the target file(s) or folder(s) where distilled content belongs
> - `distillation`: the proposed text to add or update in the destination file(s) — write it out in full, ready to paste
> - `preserve_source`: `true` or `false`, with a named re-retrieval reason if true
> - `processed_into`: the value to write into the `processed_into:` frontmatter field when archiving
> - `archive_path`: the target path under `90 Archive/YYYY-MM/` for the original note
> - `actions`: list of action-triage classifications. Each entry has:
>     - `kind`: one of `knowledge_only`, `wiki_concept`, `decision_artifact`, `world_model_update`, `skill_trigger`, `skill_update`
>     - `target`: the file path, skill name, or destination folder this action operates on
>     - `payload`: for `skill_trigger`, the input prompt to pass to the skill; for others, a brief description of what to write
>     - `tag_signal`: the tag or `type` value that triggered this action (or `null` if inferred from content)
>   Multiple actions are allowed. Default to `[{"kind": "knowledge_only"}]` if no artifact is needed.
> - `unknown_tags`: list of any tags or `type` values on the note that are not in AGENTS.md's Known tag conventions list. Empty array if none.

**Shared destination conflict rule:** when two or more sub-agents propose changes to the same destination file (e.g., `Decision Rules.md`), the orchestrator merges those changes before writing — never overwrites one with another.

**When to skip parallelization:** if the inbox contains 5 or fewer files, sequential processing is fine. Spin up parallel agents only when there are 6 or more files to process.

## Core workflow

When helping with a decision:

1. Read the relevant files — usually `01 World Model/01 State/Current State.md`, `01 World Model/02 Rules/Decision Rules.md`, and any relevant note in `01 World Model/03 Contexts/` or `01 World Model/04 Reviews/`.
2. Read the last 4–8 files in `04 Decisions/Weekly Briefs/` (sorted by date, most recent first) when they exist. If fewer than 4 briefs exist, read all available. If none exist yet, explicitly note missing brief history and continue with State, Rules, Contexts, and Reviews.
3. Summarize the current state briefly, including any pattern from the briefs worth flagging.
4. Identify the rules that apply.
5. Simulate the main options, usually YES / NO / WAIT.
6. Recommend one action.
7. Give the strongest counterargument.
8. If durable learning occurred, propose the correct file update.

When helping with file updates:

1. Prefer updating an existing file over creating a new duplicate note.
2. Keep edits targeted and minimal.
3. Preserve the current folder structure, note names, and formatting unless I explicitly ask for a redesign.
4. Before changing an important file, explain what you plan to change and why.
5. If the destination file is unclear, ask before writing.
6. If I approve, update the file directly.

## Writing rules

- Separate facts, synthesis, and speculation.
- Do not turn one-off emotions into durable rules.
- Do not write a durable rule unless there is enough evidence or I explicitly want a provisional rule.
- If something is provisional, label it clearly as provisional.
- Prefer appending or lightly revising over large rewrites.

## Goldilocks distillation

Distillation is the primary work. Preservation is the exception.

- The Wiki or World Model file is the first-class output. The source is secondary.
- Default target for a `02 Wiki/Concepts/` note is ~30–50 lines. If a concept genuinely needs more, ask whether two notes would serve better than one bloated one.
- Extract the *delta* — the principles or actions that change behavior. Skip background, generic best practices, and structural mirroring of the original.
- Preserve a source in `03 Sources/` only if you can name a specific re-retrieval reason (e.g., "I'll re-read the methodology while practicing it"). If a 30-line distillation captures the value, archive the source.
- Test for "distilled enough": could a future agent act on this without re-reading the source? If yes, you're done. If it sounds generic, cut harder.

## Log trail principle

Maintain a log trail only when the history of how something changed is as important as the current state.

**Files that get log trails:**

- `01 World Model/02 Rules/Decision Rules.md` — rules are judged by their evidence history. A rule added after one bad week carries less weight than one that survived months of real decisions. The change log is what makes that distinction visible.
- `01 World Model/04 Reviews/` — these are log files by definition. Each entry is a timestamped record.

**Files that don't get log trails:**

- `01 World Model/03 Contexts/` — reference documents. Only the current playbook matters. The `updated:` frontmatter field is sufficient.
- `01 World Model/01 State/Current State.md` — a snapshot of right now. Weekly synthesis in Reviews captures state evolution over time.
- `00 Inbox/` and `90 Archive/` — transient and chronological by design. Timestamps in filenames are enough.
- `02 Wiki/` — evergreen knowledge. Use the `updated:` frontmatter field when a note is revised.

The test: ask "would knowing when or why this changed affect how I use it?" If yes, log it. If no, keep only the current value.

## Default file update rules

- Update `01 World Model/01 State/Current State.md` when priorities, bottlenecks, constraints, or current conditions materially change.
- Update `01 World Model/02 Rules/Decision Rules.md` when a rule is added, revised, invalidated, or promoted from provisional to durable.
- Update `01 World Model/04 Reviews/` when recording a specific decision, weekly review, experiment, surprise, or outcome.
- Move processed inbox notes to `90 Archive/YYYY-MM/` after synthesis.
- When archiving a processed note, add a `processed_into:` frontmatter field listing the destination file(s). Missing field on an archived note signals it was either noise or under-processed and should be re-examined.
- Add new permanent knowledge to `02 Wiki/` only after it has been processed and distilled — not as raw capture.
- Avoid putting long-term rules only in chat. Put them in the correct file.

## Editing format

When proposing an edit, prefer this format:

- File:
- Section:
- Proposed change:
- Why:

If I ask you to proceed, then apply the update directly.

## Decision standards

- Favor clarity over inspiration.
- Use evidence from files and current chat.
- Be skeptical of novelty when it distracts from the main bottleneck.
- Distinguish what is known, what is inferred, and what is uncertain.
- If reasoning against action sounds too clean, check whether fear or avoidance may be disguising itself as prudence.
- When recommending a direction, include the strongest case against it.
- Before recommending a system change, first check whether the system already handles it. Recommend "no change" when the model is working — saying yes to needless change is a form of sycophancy.
- Sycophancy test: would I make this same recommendation if Mitchell seemed indifferent rather than committed? If the recommendation depends on his enthusiasm, it isn't grounded.

## Current objective

Help me maintain a practical personal world model that improves decision quality over time and compounds in usefulness as more context is added.