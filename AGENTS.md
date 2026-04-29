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

Current skills:
- `linkedin-creator` — Create LinkedIn posts and articles. Triggers on mentions of "LinkedIn post", "LinkedIn article", "write for LinkedIn", or similar.

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
  Clippings/
00 System/
  Templates/
  Readmes/
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
90 Archive/
  YYYY-MM/
|Personal World Model/
|AGENTS.md
|CLAUDE.md
```

### Folder roles

**`00 Inbox/`** — raw dump zone. Unprocessed thoughts, captures, observations. No structure required. Processed weekly. Everything new lands here first. Contains two types of input:
- **Raw captures** — fleeting thoughts, things noticed, ideas to evaluate, journal entries, pattern observations. Written freely, especially from mobile via Obsidian. No format required.
- `Clippings/` — web articles saved via Obsidian's web clipper. Files are pre-structured with frontmatter (`title`, `source`, `author`, `published`, `created`, `description`, `tags: clippings`) and contain the full article body. Clippings are a distinct input type from raw captures — they require different processing during synthesis.

**`00 System/`** — vault infrastructure. Templates, folder documentation, and other operating-layer files. Not personal content — this is the operating layer of the system itself.
- `Templates/` — blank templates for new entries, including Obsidian Templater templates with `<% ... %>` syntax. This is where Obsidian and Templater are configured to look for templates.
- `Readmes/` — documentation about the vault structure, note flow, and folder purposes.

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

**`03 Sources/`** — upstream inputs and raw research. This is where external material lives before or after it's been extracted from. Do not put synthesis or personal conclusions here — those belong in `02 Wiki/` or `01 World Model/`.
- `Articles/` — processed web articles and clippings after synthesis (moved from `00 Inbox/Clippings/`).
- `Podcasts/` — notes from podcast episodes.
- `Meetings/` — notes from meetings, calls, and conversations.
- `Chats/` — notable AI conversation outputs worth preserving.
- `Research Notes/` — deeper research artifacts that back specific decisions (e.g., market analysis, competitive teardowns).

**`04 Decisions/`** — active and recent decision artifacts. Separate from Reviews (which are retrospective) — this layer holds forward-looking decision support.
- `Weekly Briefs/` — weekly decision briefs and priority snapshots.
- `Decision Memos/` — structured decision write-ups for significant choices.
- `Active Plans/` — current execution plans worth tracking (not long-term archive).

**`90 Archive/`** — processed graveyard. Inbox notes land here after weekly synthesis, organized by `YYYY-MM/` subfolder. Never edit archived notes — they are a record of what was true at that time.

**`Personal World Model/`** — required by Cowork (Obsidian plugin) for project context. Do not move or rename this folder.

## Note routing rules

When classifying or moving a note, use this routing logic. Prefer explicit reasoning about the destination over auto-dumping.

- If it's **about Mitchell** (identity, goals, constraints, state, rules, context patterns) → `01 World Model/`
- If it's **durable synthesized knowledge** (frameworks, concepts, evergreen reference) → `02 Wiki/`
- If it's **raw upstream material** (source articles, research, meeting notes, chats) → `03 Sources/`
- If it **changes what Mitchell should do next** (decision memos, plans, weekly briefs) → `04 Decisions/`
- If it's **unprocessed** → `00 Inbox/` until the weekly synthesis handles it
- If **unsure**: do not guess. Flag the ambiguity and ask, or park it in `00 Inbox/` with a note.

## Weekly synthesis workflow

Once a week, open a session and say "let's do the weekly synthesis." Agent reads `00 Inbox/`, triages each note, proposes updates to the correct files, and moves processed notes to `90 Archive/YYYY-MM/`. See `00 System/Templates/Weekly Synthesis.md` for the full agenda.

**Processing raw inbox notes** — for each file directly in `00 Inbox/`, apply this 4-way decision tree:

1. **Capture** (fleeting thought, observation, idea worth evaluating) → distill into the right `01 World Model/`, `02 Wiki/`, or `04 Decisions/` file. Archive the original with `processed_into:` listing destinations.
2. **Source material** (meeting notes, podcast takeaway, chat output, research scratch) → distill any insight to the right file first. Then ask: will I re-read this source itself? If yes, move to `03 Sources/{subfolder}/`. If no, archive with `processed_into:`. Source preservation is the exception, not the default.
3. **Journal entry** (reflection, processing, thinking out loud) → synthesize if ready; leave if it needs to settle. Archive only after synthesis with `processed_into:`.
4. **Noise** (no extractable signal) → archive directly. No `processed_into:` field — its absence flags the note as either noise or under-processed.

**Processing clippings** (`00 Inbox/Clippings/`) — clippings are pre-structured external content, not personal captures. Process each one by:
1. Reading the article and identifying the key insight or pattern.
2. Deciding the destination: `02 Wiki/` if it's a distillable, evergreen concept worth keeping; a `01 World Model/03 Contexts/` update if it maps to a recurring decision pattern; `03 Sources/Articles/` if the article itself is worth archiving; or just archive if it was useful context but adds nothing permanent.
3. Proposing the update (or noting there's nothing to extract), then moving the file to `90 Archive/YYYY-MM/`.

Do not treat clippings as raw thought — they are input material to extract from, not personal state to preserve.

The synthesis is the mechanism that makes the system compound. Without it, the inbox fills and the World Model goes stale.

## Core workflow

When helping with a decision:

1. Read the relevant files — usually `01 World Model/01 State/Current State.md`, `01 World Model/02 Rules/Decision Rules.md`, and any relevant note in `01 World Model/03 Contexts/` or `01 World Model/04 Reviews/`.
2. Summarize the current state briefly.
3. Identify the rules that apply.
4. Simulate the main options, usually YES / NO / WAIT.
5. Recommend one action.
6. Give the strongest counterargument.
7. If durable learning occurred, propose the correct file update.

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
