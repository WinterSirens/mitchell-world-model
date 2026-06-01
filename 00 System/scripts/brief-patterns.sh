#!/bin/bash
# brief-patterns.sh — Longitudinal pattern analyzer for Weekly Briefs
#
# Reads all weekly briefs and extracts:
#   1. Energy / focus / stress trend over time
#   2. Bottleneck history (is it shifting or stuck?)
#   3. Avoidance tracking (what keeps showing up?)
#   4. Persistent open questions (carried across 3+ briefs)
#   5. Recurring patterns (candidates for durable rules or theme notes)
#   6. Prediction accuracy (once prediction tracking is active)
#   7. Planned vs actual (next-week outlook → what actually moved)
#
# Usage:
#   ./brief-patterns.sh              # analyze all briefs
#   ./brief-patterns.sh --last 4     # analyze only the 4 most recent briefs
#
# Best run during monthly synthesis or whenever you need the longitudinal view.

set -o pipefail

VAULT_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
BRIEFS_DIR="$VAULT_DIR/04 Decisions/Weekly Briefs"

# --- Parse args ---
LIMIT=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --last) LIMIT="$2"; shift 2 ;;
    -h|--help)
      echo "Usage: $0 [--last N]"
      echo "  --last N   Only analyze the N most recent briefs (default: all)"
      exit 0
      ;;
    *) echo "Unknown option: $1. Use --help for usage."; exit 1 ;;
  esac
done

# --- Collect briefs ---
if [[ ! -d "$BRIEFS_DIR" ]]; then
  echo "No Weekly Briefs directory found at: $BRIEFS_DIR"
  exit 1
fi

ALL_BRIEFS=$(find "$BRIEFS_DIR" -name "*.md" -not -name ".*" | sort)

if [[ -z "$ALL_BRIEFS" ]]; then
  echo "No weekly briefs found in $BRIEFS_DIR"
  exit 1
fi

if [[ "$LIMIT" -gt 0 ]]; then
  BRIEFS=$(echo "$ALL_BRIEFS" | tail -n "$LIMIT")
else
  BRIEFS="$ALL_BRIEFS"
fi

BRIEF_COUNT=$(echo "$BRIEFS" | wc -l | tr -d ' ')

# --- Helper: extract section content between two ## headers ---
extract_section() {
  local file="$1"
  local header="$2"
  awk -v h="$header" '
    $0 ~ "^## " h { found=1; next }
    found && /^## / { found=0 }
    found { print }
  ' "$file" | sed '/^$/d'
}

# --- Header ---
echo ""
echo "══════════════════════════════════════════════════════"
echo "  WEEKLY BRIEF PATTERN ANALYSIS"
echo "  $BRIEF_COUNT briefs analyzed"
echo "══════════════════════════════════════════════════════"
echo ""

# ─────────────────────────────────────────────────────────
# 1. ENERGY / FOCUS / STRESS TIMELINE
# ─────────────────────────────────────────────────────────
echo "┌─────────────────────────────────────────────────────┐"
echo "│  1. ENERGY / FOCUS / STRESS TIMELINE                │"
echo "└─────────────────────────────────────────────────────┘"
echo ""

while IFS= read -r brief; do
  week=$(grep -m1 "^week:" "$brief" | sed 's/week: *//')
  date=$(basename "$brief" | sed 's/ Weekly Brief.md//')
  energy=$(grep -m1 '\*\*Energy:\*\*' "$brief" | sed 's/.*\*\*Energy:\*\* *//')
  focus=$(grep -m1 '\*\*Focus:\*\*' "$brief" | sed 's/.*\*\*Focus:\*\* *//')
  stress=$(grep -m1 '\*\*Stress:\*\*' "$brief" | sed 's/.*\*\*Stress:\*\* *//')
  trend=$(grep -m1 'Energy trend:' "$brief" | sed 's/.*Energy trend: *//')

  printf "  %-12s %-10s\n" "$date" "($week)"
  printf "    Energy:  %s\n" "$energy"
  printf "    Focus:   %s\n" "$focus"
  printf "    Stress:  %s\n" "$stress"
  printf "    Trend:   %s\n" "$trend"
  echo ""
done <<< "$BRIEFS"

# ─────────────────────────────────────────────────────────
# 2. BOTTLENECK HISTORY
# ─────────────────────────────────────────────────────────
echo "┌─────────────────────────────────────────────────────┐"
echo "│  2. BOTTLENECK HISTORY                              │"
echo "└─────────────────────────────────────────────────────┘"
echo ""

while IFS= read -r brief; do
  date=$(basename "$brief" | sed 's/ Weekly Brief.md//')
  echo "  $date"
  extract_section "$brief" "Bottleneck" | sed 's/^/    /'
  echo ""
done <<< "$BRIEFS"

# ─────────────────────────────────────────────────────────
# 3. AVOIDANCE TRACKING
# ─────────────────────────────────────────────────────────
echo "┌─────────────────────────────────────────────────────┐"
echo "│  3. AVOIDANCE TRACKING                              │"
echo "└─────────────────────────────────────────────────────┘"
echo ""

while IFS= read -r brief; do
  date=$(basename "$brief" | sed 's/ Weekly Brief.md//')
  content=$(extract_section "$brief" "What I'm avoiding")
  echo "  $date"
  if [[ -n "$content" ]]; then
    echo "$content" | sed 's/^/    /'
  else
    echo "    (no avoidance noted)"
  fi
  echo ""
done <<< "$BRIEFS"

# ─────────────────────────────────────────────────────────
# 4. PERSISTENT OPEN QUESTIONS
# ─────────────────────────────────────────────────────────
echo "┌─────────────────────────────────────────────────────┐"
echo "│  4. OPEN QUESTIONS BY BRIEF                         │"
echo "└─────────────────────────────────────────────────────┘"
echo ""

# Collect open questions per brief, then show persistence
QUESTIONS_TEMP=$(mktemp)

while IFS= read -r brief; do
  date=$(basename "$brief" | sed 's/ Weekly Brief.md//')

  # Open/unresolved decisions
  awk '/What decisions are still open/{flag=1; next} /^## |^_[A-Z]/{if(flag) flag=0} flag' "$brief" \
    | grep -E '^-' | while IFS= read -r line; do
      echo "$date|$line"
    done

  # Uncertainty/anxiety heading into next week
  awk '/most uncertain or anxious/{flag=1; next} /^## |^$/{if(flag) flag=0} flag' "$brief" \
    | grep -E '^-' | while IFS= read -r line; do
      echo "$date|$line"
    done

done <<< "$BRIEFS" > "$QUESTIONS_TEMP"

if [[ -s "$QUESTIONS_TEMP" ]]; then
  while IFS='|' read -r date question; do
    printf "  [%s] %s\n" "$date" "$question"
  done < "$QUESTIONS_TEMP"
else
  echo "  (no open questions found)"
fi
rm -f "$QUESTIONS_TEMP"
echo ""

# ─────────────────────────────────────────────────────────
# 5. RECURRING PATTERNS
# ─────────────────────────────────────────────────────────
echo "┌─────────────────────────────────────────────────────┐"
echo "│  5. PATTERNS ACROSS BRIEFS                          │"
echo "└─────────────────────────────────────────────────────┘"
echo ""

while IFS= read -r brief; do
  date=$(basename "$brief" | sed 's/ Weekly Brief.md//')
  content=$(extract_section "$brief" "Patterns I notice")
  if [[ -n "$content" ]]; then
    echo "  $date"
    echo "$content" | sed 's/^/    /'
    echo ""
  fi
done <<< "$BRIEFS"

# ─────────────────────────────────────────────────────────
# 6. PREDICTION ACCURACY
# ─────────────────────────────────────────────────────────
echo "┌─────────────────────────────────────────────────────┐"
echo "│  6. PREDICTION ACCURACY                             │"
echo "└─────────────────────────────────────────────────────┘"
echo ""

HAS_PREDICTIONS=false
while IFS= read -r brief; do
  date=$(basename "$brief" | sed 's/ Weekly Brief.md//')
  content=$(extract_section "$brief" "Prediction scorecard")
  if [[ -n "$content" ]]; then
    HAS_PREDICTIONS=true
    echo "  $date"
    echo "$content" | sed 's/^/    /'
    echo ""
  fi
done <<< "$BRIEFS"

if [[ "$HAS_PREDICTIONS" == false ]]; then
  echo "  No prediction data yet. Predictions will appear once the"
  echo "  updated Weekly Brief template is used for 2+ consecutive weeks."
fi
echo ""

# ─────────────────────────────────────────────────────────
# 7. PLANNED VS ACTUAL
# ─────────────────────────────────────────────────────────
echo "┌─────────────────────────────────────────────────────┐"
echo "│  7. PLANNED vs ACTUAL                               │"
echo "│     (last week's outlook → this week's movement)    │"
echo "└─────────────────────────────────────────────────────┘"
echo ""

PREV_OUTLOOK=""
PREV_DATE=""

while IFS= read -r brief; do
  date=$(basename "$brief" | sed 's/ Weekly Brief.md//')

  if [[ -n "$PREV_OUTLOOK" ]]; then
    # Get what actually moved this week
    moved=$(awk '/What (actually moved|advanced)/{flag=1; next} /^$|^_What (stalled|surprised)/{if(flag) flag=0} flag' "$brief" \
      | grep -E '^-' | head -5)

    echo "  $PREV_DATE planned → $date actual:"
    echo "    PLANNED:"
    echo "$PREV_OUTLOOK" | sed 's/^/      /'
    echo "    MOVED:"
    if [[ -n "$moved" ]]; then
      echo "$moved" | sed 's/^/      /'
    else
      echo "      (no movement data extracted)"
    fi
    echo ""
  fi

  # Capture this brief's outlook for next iteration
  PREV_OUTLOOK=$(awk '/^## Next week outlook/{flag=1; next} /^_What|^## /{if(flag) flag=0} flag' "$brief" \
    | grep -E '^[0-9]+\.' | head -4)
  PREV_DATE="$date"

done <<< "$BRIEFS"

# ─────────────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────────────
echo "══════════════════════════════════════════════════════"
echo "  Run during monthly synthesis to feed pattern"
echo "  detection and rule graduation decisions."
echo "  Script: 00 System/scripts/brief-patterns.sh"
echo "══════════════════════════════════════════════════════"
echo ""
