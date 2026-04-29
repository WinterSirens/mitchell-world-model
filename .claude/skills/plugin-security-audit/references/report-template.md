# Risk Report Template

After completing the automated checks and manual assessment, produce a report following this structure. The report should be a markdown file saved to the outputs directory.

## Report Structure

```markdown
# Plugin Security Audit Report

**Plugin:** [name]
**Type:** [MCP Server / Custom Skill / Both]
**Publisher:** [name or "Unknown"]
**Source:** [URL or "Uploaded files"]
**Audit date:** [date]
**Source code available:** [Yes / Partial / No]

---

## Overall Risk Rating: [CRITICAL / HIGH / MEDIUM / LOW]

[One paragraph summary of the overall assessment. State the rating clearly, explain the primary drivers, and note any major caveats about the audit's scope.]

---

## Risk Summary

| Category | Rating | Key Finding |
|---|---|---|
| Prompt Injection | [rating] | [one-line summary] |
| Permission Scope | [rating] | [one-line summary] |
| Data Exfiltration | [rating] | [one-line summary] |
| Dependencies | [rating] | [one-line summary] |
| Publisher Trust | [rating] | [one-line summary] |
| Update Risk | [rating] | [one-line summary] |

The overall rating is driven by the highest individual category rating, not an average.

---

## Detailed Findings

### Prompt Injection Surface
[Findings from automated Check 1 and Manual Section 4]

### Permission Scope
[Findings from automated Check 2 and Manual Section 2]

### Data Flow & Exfiltration Risk
[Findings from automated Check 3 and Manual Section 3]

### Dependency Chain
[Findings from automated Check 4]

### Code Execution Risk
[Findings from automated Check 5]

### Credential Handling
[Findings from automated Check 6]

### Publisher & Maintenance
[Findings from Manual Sections 1, 5, and 6]

For each finding, include:
- **Severity:** CRITICAL / HIGH / MEDIUM / LOW / INFO
- **Evidence:** What was found and where (file:line for code, or description for manual findings)
- **Risk:** What could happen if this is exploited or goes wrong
- **Mitigation:** What the user or plugin author could do about it

---

## Recommendation

### Go / Conditional Go / No-Go

[Clear recommendation with reasoning]

**If Conditional Go, specify the conditions:**
- [ ] Condition 1
- [ ] Condition 2

**Mitigations if proceeding:**
- [Specific steps to reduce risk while using this plugin]

---

## Research Backlog

Items that require further investigation beyond what this audit could determine. These are things the user should look into before making a final decision, or should monitor ongoing.

| # | Item | Why It Matters | How to Investigate |
|---|---|---|---|
| 1 | [description] | [risk context] | [specific steps] |
| 2 | [description] | [risk context] | [specific steps] |

---

## Audit Limitations

[Be explicit about what this audit could and could not assess. Common limitations:]

- [ ] Source code was / was not available for review
- [ ] Dependency vulnerability scan was / was not possible (network access)
- [ ] Server-side behavior of MCP server could not be verified
- [ ] Runtime behavior was not tested (static analysis only)
- [ ] [Any other limitations specific to this audit]
```

## Severity Assignment Rules

The overall rating follows the **highest-severity finding** with this logic:

- Any CRITICAL finding → Overall CRITICAL (recommend No-Go)
- Any HIGH finding without adequate mitigation → Overall HIGH (recommend Conditional Go at best)
- Only MEDIUM and below → Overall MEDIUM or LOW (recommend Go with awareness)

Never average across categories. One critical finding in one area makes the whole plugin critical, even if everything else is clean.

## Tone Guidelines

- Be direct and specific. "This plugin sends conversation data to an undocumented endpoint" not "there may be some data concerns."
- Avoid false reassurance. "No issues found in the areas we checked" not "this plugin is safe."
- Credit good practices. If the plugin does something well (proper encryption, minimal permissions, good error handling), say so.
- The user is the decision-maker. Present evidence and risk clearly, but the go/no-go is their call.
- The research backlog is a feature, not a failure. Some things genuinely require more investigation than a single audit can provide.

## File Output

Save the report as a markdown file:
```
/mnt/user-data/outputs/plugin-audit-[plugin-name]-[date].md
```

If the automated checks produced specific artifacts (capability matrix, URL inventory, etc.), include them inline in the report rather than as separate files.
