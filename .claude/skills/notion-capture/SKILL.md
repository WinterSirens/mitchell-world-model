---
name: notion-capture
description: Capture and save content to Notion with intelligent workspace placement. Use this skill whenever the user wants to add, save, or capture anything to Notion (notes, tool lists, resources, research, reference pages, summaries, or any other content). Triggers on phrases like "add this to Notion", "save this to Notion", "put this in Notion", "capture this", or any time the user provides content and wants it stored. Always analyze the existing workspace structure before creating anything. Never drop content at the workspace root without first understanding where it belongs.
---

# Notion Capture Skill

The workspace follows the **PARA method** (by Tiago Forte). Every piece of content belongs in one of four buckets. Understanding PARA is the primary routing tool — workspace search is used to find the right sub-page within a bucket, not to determine which bucket.

---

## The PARA Framework

**Projects** — Work with a defined outcome and deadline. If the content is tied to something actively being worked toward right now, it goes here.

**Areas** — Ongoing responsibilities with no end date. Life domains like work, health, finances, creative work, faith. If the content is about maintaining a standard in one of these domains, it goes here.

**Resources** — Reference material on topics of interest. If the content is something to learn from or refer back to (tools, research, notes, guides, articles), it goes here. This is the most common destination for captured content.

**Archive** — Completed projects, inactive areas, or outdated resources. If the user is explicitly archiving something, it goes here.

When in doubt between Resources and Areas: ask whether the content is reference material (Resources) or operational context for an active responsibility (Areas).

---

## Workflow

### Step 1: Identify the PARA Bucket

Read the content and determine which of the four buckets it belongs in. This is usually obvious:

- Curated tool lists, research, guides, articles, notes = **Resources**
- Context for an active work or life domain = **Areas**
- Something tied to a specific active project = **Projects**
- Explicitly completed or inactive = **Archive**

Don't ask the user unless the content is genuinely ambiguous between two buckets.

### Step 2: Search Within That Bucket

Run 1-2 targeted searches to find the right sub-page. Use `notion-search` with `query_type: internal` and short, specific queries (3-5 words) focused on the content's topic or domain.

You're looking for the most specific existing home, not just a plausible one. A sub-page that already holds similar content is better than dropping directly under the bucket root.

### Step 3: Fetch and Inspect Candidates

For each strong candidate, use `notion-fetch` to:
- See its child pages and structure
- Confirm it's the right conceptual fit
- Check if there's an even more specific sub-page inside it

The goal is depth: if "Resources > AI (Cognitive Technology)" already exists and holds AI reference material, that's the right parent, not "Resources" root.

### Step 4: Create the Page Directly in the Right Location

Create the page with `notion-create-pages` pointing to the correct parent from the start:

- Clear, descriptive title
- Appropriate emoji icon if the content warrants one
- Clean Markdown formatting (headers, bullet lists, links)
- Don't repeat the title inside the content body

Avoid the create-then-move pattern when possible. Place it correctly the first time.

### Step 5: Confirm Placement

After creating, tell the user:
- The full path (e.g., Resources > AI (Cognitive Technology) > Page Title)
- One sentence on why that location made sense
- A direct link to the page

---

## Placement Examples

**Curated AI tool list**
Bucket: Resources. Search for existing AI or tech reference pages. Place inside the most specific match (e.g., an AI or cognitive tech sub-page).

**Notes from a PM course**
Bucket: Resources (reference material) or Areas > Product if it directly supports active work. Search for a learning or course notes section first.

**A recipe**
Bucket: Resources. Search for an existing recipes or food section within Resources.

**Active project brief with deliverables and deadline**
Bucket: Projects. Search for the relevant project page or create a new one under Projects.

**A standard operating procedure for a work process**
Bucket: Areas > MX (or the relevant work area). It's operational context, not reference material.

**A finished project retrospective**
Bucket: Archive.

---

## Edge Cases

**No specific sub-page exists**: Place directly under the bucket root (e.g., Resources) and note it. Mention the user may want to create a sub-section if this topic grows.

**Genuinely ambiguous between two buckets**: State what you found and ask one clear question. Don't guess on bucket placement.

**User specifies a location**: Skip analysis entirely and place it where they said.

**Large content**: Break into logical sections with Markdown headers. Don't dump a wall of text.
