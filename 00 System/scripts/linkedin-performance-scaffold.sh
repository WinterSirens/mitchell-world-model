#!/bin/bash
# linkedin-performance-scaffold.sh — LinkedIn performance log management
#
# Two modes:
#
#   1. Scaffold mode (default):
#      Creates the monthly performance log with published post data pre-populated.
#      Usage: ./linkedin-performance-scaffold.sh [YYYY-MM]
#      Defaults to current month if no argument given.
#
#   2. Analyze mode:
#      Reads all existing performance logs and outputs a consolidated report
#      with per-pillar metrics, trends, and proposed skill updates.
#      Usage: ./linkedin-performance-scaffold.sh --analyze
#
# The analyze output is designed to be read during monthly synthesis,
# where the agent applies proposed updates to the linkedin-creator skill.

set -o pipefail

VAULT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
CONTENT_DIR="$VAULT_DIR/05 Content/LinkedIn"
PERF_DIR="$CONTENT_DIR/performance"
PUBLISHED_DIR="$CONTENT_DIR/published"
SKILL_FILE="$VAULT_DIR/.claude/skills/linkedin-creator/SKILL.md"

# ─────────────────────────────────────────────────────────
# SCAFFOLD MODE
# ─────────────────────────────────────────────────────────
scaffold_month() {
  local MONTH="${1:-$(date +%Y-%m)}"
  local OUTFILE="$PERF_DIR/$MONTH.md"

  if [[ -f "$OUTFILE" ]]; then
    echo "Performance log already exists: $OUTFILE"
    echo "Edit the existing file or remove it to re-scaffold."
    exit 1
  fi

  # Find published posts from this month
  local YEAR_MONTH="$MONTH"
  local POSTS=""
  if [[ -d "$PUBLISHED_DIR" ]]; then
    POSTS=$(find "$PUBLISHED_DIR" -name "${YEAR_MONTH}*.md" -not -name ".*" | sort)
  fi

  # Build table rows from published post frontmatter
  local TABLE_ROWS=""
  if [[ -n "$POSTS" ]]; then
    while IFS= read -r post; do
      local fname=$(basename "$post" .md)
      local pub_date=$(grep -m1 "^published:" "$post" | sed 's/published: *//' | tr -d ' ')
      local pillar=$(grep -m1 "^pillar:" "$post" | sed 's/pillar: *//' | tr -d ' ')

      # Use published date if available, otherwise extract from filename
      if [[ -z "$pub_date" || "$pub_date" == "null" ]]; then
        pub_date=$(echo "$fname" | grep -oE '^[0-9]{4}-[0-9]{2}-[0-9]{2}')
      fi

      # Default pillar to "—" if not found
      [[ -z "$pillar" || "$pillar" == "null" ]] && pillar="—"

      TABLE_ROWS="${TABLE_ROWS}| ${pub_date} | ${fname} | ${pillar} |  |  |  |  |  |  |  |  |  |  |\n"
    done <<< "$POSTS"
  fi

  # Also check for posts published this month but filed with earlier draft dates
  if [[ -d "$PUBLISHED_DIR" ]]; then
    local OTHER_POSTS=$(grep -rl "^published: ${YEAR_MONTH}" "$PUBLISHED_DIR" 2>/dev/null \
      | while read -r f; do
          fname=$(basename "$f")
          # Skip if already caught by filename match
          echo "$fname" | grep -q "^${YEAR_MONTH}" && continue
          echo "$f"
        done)

    if [[ -n "$OTHER_POSTS" ]]; then
      while IFS= read -r post; do
        local fname=$(basename "$post" .md)
        local pub_date=$(grep -m1 "^published:" "$post" | sed 's/published: *//' | tr -d ' ')
        local pillar=$(grep -m1 "^pillar:" "$post" | sed 's/pillar: *//' | tr -d ' ')
        [[ -z "$pillar" || "$pillar" == "null" ]] && pillar="—"
        TABLE_ROWS="${TABLE_ROWS}| ${pub_date} | ${fname} | ${pillar} |  |  |  |  |  |  |  |  |  |  |\n"
      done <<< "$OTHER_POSTS"
    fi
  fi

  # Count posts found
  local POST_COUNT=0
  if [[ -n "$TABLE_ROWS" ]]; then
    POST_COUNT=$(echo -e "$TABLE_ROWS" | grep -c '^|')
  fi

  # Write the scaffold file
  cat > "$OUTFILE" << TEMPLATE
---
type: linkedin-performance-log
month: $MONTH
created: $(date +%Y-%m-%d)
---

## Posts published this month

| Date | File | Pillar | Impressions | Members reached | Comments | Saves | Reactions | Reposts | Sends | Profile viewers | Followers gained | Notes |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
$(echo -e "$TABLE_ROWS")

## What worked

- 

## What didn't

- 

## Proposed skill updates

_These proposed updates will be reviewed during monthly synthesis and applied to \`.claude/skills/linkedin-creator/SKILL.md\`._

- 

## Open questions

_Hypotheses to test next month._

- 
TEMPLATE

  echo "Created: $OUTFILE"
  echo "Pre-populated with $POST_COUNT published post(s) from $MONTH."
  echo ""
  echo "Next steps:"
  echo "  1. Fill in engagement metrics as posts mature (~7 days each)"
  echo "  2. Write the synthesis sections at month end"
  echo "  3. Run: ./linkedin-performance-scaffold.sh --analyze"
  echo "     to generate the cross-month report and skill update recommendations"
}

# ─────────────────────────────────────────────────────────
# ANALYZE MODE
# ─────────────────────────────────────────────────────────
analyze_performance() {
  echo ""
  echo "══════════════════════════════════════════════════════"
  echo "  LINKEDIN PERFORMANCE ANALYSIS"
  echo "══════════════════════════════════════════════════════"
  echo ""

  local PERF_FILES=$(find "$PERF_DIR" -name "????-??.md" -not -name "README*" | sort)

  if [[ -z "$PERF_FILES" ]]; then
    echo "No performance logs found in $PERF_DIR"
    exit 1
  fi

  local FILE_COUNT=$(echo "$PERF_FILES" | wc -l | tr -d ' ')
  echo "  Analyzing $FILE_COUNT month(s) of performance data."
  echo ""

  # --- Per-month summary ---
  echo "┌─────────────────────────────────────────────────────┐"
  echo "│  MONTHLY OVERVIEW                                   │"
  echo "└─────────────────────────────────────────────────────┘"
  echo ""

  while IFS= read -r perf_file; do
    local month=$(basename "$perf_file" .md)
    local post_count=0
    local total_impressions=0
    local total_comments=0
    local total_reactions=0
    local total_saves=0

    # Parse table rows (skip header and separator)
    while IFS='|' read -r _ date file pillar impressions rest; do
      # Skip non-data rows
      [[ "$date" =~ ^[[:space:]]*--- ]] && continue
      [[ "$date" =~ ^[[:space:]]*Date ]] && continue
      [[ -z "$impressions" ]] && continue

      local imp=$(echo "$impressions" | tr -d ' ,')
      [[ "$imp" =~ ^[0-9]+$ ]] || continue

      post_count=$((post_count + 1))
      total_impressions=$((total_impressions + imp))

      local comm=$(echo "$rest" | awk -F'|' '{print $2}' | tr -d ' ,')
      local sav=$(echo "$rest" | awk -F'|' '{print $3}' | tr -d ' ,')
      local react=$(echo "$rest" | awk -F'|' '{print $4}' | tr -d ' ,')

      [[ "$comm" =~ ^[0-9]+$ ]] && total_comments=$((total_comments + comm))
      [[ "$sav" =~ ^[0-9]+$ ]] && total_saves=$((total_saves + sav))
      [[ "$react" =~ ^[0-9]+$ ]] && total_reactions=$((total_reactions + react))
    done < <(grep '^|' "$perf_file" | tail -n +3)

    local avg_impressions=0
    [[ $post_count -gt 0 ]] && avg_impressions=$((total_impressions / post_count))

    printf "  %s: %d posts, %d total impressions (avg %d/post), %d comments, %d saves, %d reactions\n" \
      "$month" "$post_count" "$total_impressions" "$avg_impressions" \
      "$total_comments" "$total_saves" "$total_reactions"
  done <<< "$PERF_FILES"
  echo ""

  # --- Per-pillar breakdown ---
  echo "┌─────────────────────────────────────────────────────┐"
  echo "│  PER-PILLAR PERFORMANCE (all months combined)       │"
  echo "└─────────────────────────────────────────────────────┘"
  echo ""

  # Collect per-pillar data across all files
  local PILLAR_TEMP=$(mktemp)

  while IFS= read -r perf_file; do
    while IFS='|' read -r _ date file pillar impressions rest; do
      [[ "$date" =~ ^[[:space:]]*--- ]] && continue
      [[ "$date" =~ ^[[:space:]]*Date ]] && continue
      local p=$(echo "$pillar" | tr -d ' ')
      local imp=$(echo "$impressions" | tr -d ' ,')
      [[ "$imp" =~ ^[0-9]+$ ]] || continue
      [[ -z "$p" || "$p" == "—" ]] && p="other"

      local comm=$(echo "$rest" | awk -F'|' '{print $2}' | tr -d ' ,')
      local sav=$(echo "$rest" | awk -F'|' '{print $3}' | tr -d ' ,')
      local react=$(echo "$rest" | awk -F'|' '{print $4}' | tr -d ' ,')
      [[ ! "$comm" =~ ^[0-9]+$ ]] && comm=0
      [[ ! "$sav" =~ ^[0-9]+$ ]] && sav=0
      [[ ! "$react" =~ ^[0-9]+$ ]] && react=0

      echo "$p $imp $comm $sav $react"
    done < <(grep '^|' "$perf_file" | tail -n +3)
  done <<< "$PERF_FILES" > "$PILLAR_TEMP"

  if [[ -s "$PILLAR_TEMP" ]]; then
    # Aggregate per pillar
    awk '{
      pillar=$1; imp=$2; comm=$3; sav=$4; react=$5
      count[pillar]++
      impressions[pillar]+=imp
      comments[pillar]+=comm
      saves[pillar]+=sav
      reactions[pillar]+=react
    }
    END {
      for (p in count) {
        avg=int(impressions[p]/count[p])
        printf "  Pillar %-6s %2d posts | avg %4d impressions | %2d comments | %2d saves | %2d reactions\n", \
          p":", count[p], avg, comments[p], saves[p], reactions[p]
      }
    }' "$PILLAR_TEMP" | sort
  fi
  rm -f "$PILLAR_TEMP"
  echo ""

  # --- Extract "What worked" / "What didn't" across months ---
  echo "┌─────────────────────────────────────────────────────┐"
  echo "│  CROSS-MONTH LEARNINGS                              │"
  echo "└─────────────────────────────────────────────────────┘"
  echo ""

  echo "  WHAT WORKED:"
  while IFS= read -r perf_file; do
    local month=$(basename "$perf_file" .md)
    awk '/^## What worked/{flag=1; next} /^## /{flag=0} flag && /^-/' "$perf_file" \
      | while IFS= read -r line; do
          echo "    [$month] $line"
        done
  done <<< "$PERF_FILES"
  echo ""

  echo "  WHAT DIDN'T:"
  while IFS= read -r perf_file; do
    local month=$(basename "$perf_file" .md)
    awk "/^## What didn't/{flag=1; next} /^## /{flag=0} flag && /^-/" "$perf_file" \
      | while IFS= read -r line; do
          echo "    [$month] $line"
        done
  done <<< "$PERF_FILES"
  echo ""

  # --- Extract proposed skill updates ---
  echo "┌─────────────────────────────────────────────────────┐"
  echo "│  PROPOSED SKILL UPDATES (pending application)       │"
  echo "└─────────────────────────────────────────────────────┘"
  echo ""

  local HAS_UPDATES=false
  while IFS= read -r perf_file; do
    local month=$(basename "$perf_file" .md)
    local updates=$(awk '/^## Proposed skill updates/{flag=1; next} /^## /{flag=0} flag && /^-/' "$perf_file")
    if [[ -n "$updates" ]]; then
      HAS_UPDATES=true
      echo "  [$month]"
      echo "$updates" | sed 's/^/    /'
      echo ""
    fi
  done <<< "$PERF_FILES"

  if [[ "$HAS_UPDATES" == false ]]; then
    echo "  No proposed updates found in performance logs."
  fi
  echo ""

  # --- Open questions ---
  echo "┌─────────────────────────────────────────────────────┐"
  echo "│  OPEN QUESTIONS (carried forward)                   │"
  echo "└─────────────────────────────────────────────────────┘"
  echo ""

  while IFS= read -r perf_file; do
    local month=$(basename "$perf_file" .md)
    local questions=$(awk '/^## Open questions/{flag=1; next} /^## /{flag=0} flag && /^-/' "$perf_file")
    if [[ -n "$questions" ]]; then
      echo "  [$month]"
      echo "$questions" | sed 's/^/    /'
      echo ""
    fi
  done <<< "$PERF_FILES"

  # --- Skill file check ---
  echo "┌─────────────────────────────────────────────────────┐"
  echo "│  CURRENT SKILL STATUS                               │"
  echo "└─────────────────────────────────────────────────────┘"
  echo ""

  if [[ -f "$SKILL_FILE" ]]; then
    local skill_lines=$(wc -l < "$SKILL_FILE" | tr -d ' ')
    local perf_section=$(grep -c "Current Performance Lessons" "$SKILL_FILE")
    echo "  Skill file: $SKILL_FILE"
    echo "  Lines: $skill_lines"
    if [[ "$perf_section" -gt 0 ]]; then
      echo "  Has 'Current Performance Lessons' section: yes"
      echo ""
      echo "  Current performance lessons in skill:"
      awk '/^### Current Performance Lessons/{flag=1; next} /^### |^---/{flag=0} flag && /^-/' "$SKILL_FILE" \
        | sed 's/^/    /'
    else
      echo "  Has 'Current Performance Lessons' section: no (should be added)"
    fi
  else
    echo "  WARNING: Skill file not found at $SKILL_FILE"
  fi

  echo ""
  echo "══════════════════════════════════════════════════════"
  echo "  Review the proposed skill updates above."
  echo "  During monthly synthesis, the agent reads this output"
  echo "  and applies confirmed updates to the linkedin-creator skill."
  echo "══════════════════════════════════════════════════════"
  echo ""
}

# ─────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────
case "${1:-}" in
  --analyze)
    analyze_performance
    ;;
  -h|--help)
    echo "Usage:"
    echo "  $0 [YYYY-MM]    Scaffold a new monthly performance log (default: current month)"
    echo "  $0 --analyze    Analyze all performance data and output skill update recommendations"
    echo "  $0 --help       Show this help"
    ;;
  *)
    scaffold_month "$1"
    ;;
esac
