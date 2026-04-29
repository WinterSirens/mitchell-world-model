# Phase 2: Data Understanding

## Key Questions

### Data Sources
- What data is needed for this solution?
- Where will data come from (systems, APIs, teams)?
- Who owns each data source?
- Can we use pre-trained models to reduce data needs?

### Data Description (4 V's)
- **Volume**: How much data? (rows, documents, tokens)
- **Variety**: What types? (text, structured, logs, images)
- **Velocity**: How fast does it change? Refresh cadence needed?
- **Veracity**: Known quality concerns? (gaps, bias, drift)

### Data Quality
- Current quality assessment (completeness, accuracy, consistency)
- Labeling or annotation requirements
- Estimated preparation effort
- Privacy and security handling needs

### Data Access
- Access mechanisms and approvals needed
- Data residency requirements
- Anonymization or masking needed

## Sensitive Data Considerations

For any solution handling customer, financial, or proprietary data (internal or external):
- Data classification level (public/internal/confidential/restricted)
- PII handling requirements (what personal data, how protected)
- Retention and deletion policies
- Access control requirements
- Audit trail requirements

Flag for compliance/security team review when uncertain about specific requirements.

## Go/No-Go Criteria

**Go to next phase if:**
- Data inventory complete, no critical gaps
- Volume sufficient for MVP
- Quality issues understood with remediation plan
- Access approvals in progress or secured

**No-Go if:**
- Critical data gaps with no acquisition path
- Quality too poor to remediate in timeline
- Compliance blockers unresolved

## Section Template

```markdown
## Data Requirements

### Data Sources
| Source | Type | Owner | Access Status |
|--------|------|-------|---------------|
| [e.g., Support tickets] | [Text] | [CS Team] | [Available] |

### Data Characteristics
- Volume: [estimated size/count]
- Freshness: [how often updated, staleness tolerance]
- Quality: [known issues, cleanliness assessment]

### Data Gaps
| Gap | Impact | Mitigation |
|-----|--------|------------|
| [Missing data type] | [Effect on solution] | [How to address] |

### Privacy & Compliance
- Classification: [public/internal/confidential/restricted]
- PII present: [yes/no, types]
- Handling requirements: [anonymization, encryption, access controls]
- Approvals needed: [list required sign-offs]
```
