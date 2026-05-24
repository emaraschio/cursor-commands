#!/usr/bin/env bash
# Symlink commands and skills into ~/.cursor (or $CURSOR_HOME).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CURSOR_HOME="${CURSOR_HOME:-$HOME/.cursor}"
EXPECTED_COMMANDS=32
EXPECTED_SKILLS=34

mkdir -p "$CURSOR_HOME/commands" "$CURSOR_HOME/skills"

command_count=0
for src in "$REPO_ROOT/.cursor/commands/"*.md; do
  [[ -f "$src" ]] || continue
  name="$(basename "$src")"
  ln -sfn "$(cd "$(dirname "$src")" && pwd)/$name" "$CURSOR_HOME/commands/$name"
  command_count=$((command_count + 1))
done

skill_count=0
for src in "$REPO_ROOT/.cursor/skills/"*/; do
  [[ -d "$src" ]] || continue
  name="$(basename "$src")"
  ln -sfn "$(cd "$src" && pwd)" "$CURSOR_HOME/skills/$name"
  skill_count=$((skill_count + 1))
done

errors=0
if [[ "$command_count" -ne "$EXPECTED_COMMANDS" ]]; then
  echo "ERROR: expected $EXPECTED_COMMANDS command symlinks, got $command_count" >&2
  errors=1
fi
if [[ "$skill_count" -ne "$EXPECTED_SKILLS" ]]; then
  echo "ERROR: expected $EXPECTED_SKILLS skill symlinks, got $skill_count" >&2
  errors=1
fi

for link in "$CURSOR_HOME/commands/"*.md; do
  [[ -L "$link" ]] || continue
  if ! test -e "$link"; then
    echo "ERROR: broken command symlink: $link" >&2
    errors=1
  fi
done

for link in "$CURSOR_HOME/skills/"*/; do
  [[ -d "$link" ]] || continue
  if ! test -e "$link"; then
    echo "ERROR: broken skill symlink: $link" >&2
    errors=1
  fi
done

if ! test -f "$CURSOR_HOME/skills/merge-open-prs/SKILL.md"; then
  echo "ERROR: merge-open-prs skill not reachable at $CURSOR_HOME/skills/merge-open-prs/SKILL.md" >&2
  errors=1
fi

if ! python3 "$REPO_ROOT/scripts/validate-cursor-commands.py"; then
  errors=1
fi

if [[ "$errors" -ne 0 ]]; then
  exit 1
fi

echo "Installed $command_count commands and $skill_count skills into $CURSOR_HOME"
echo "Manual Cursor check: docs/VERIFICATION.md"
