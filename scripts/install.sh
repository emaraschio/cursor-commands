#!/usr/bin/env bash
# Symlink commands and skills into ~/.cursor (or $CURSOR_HOME).
# Default: merge (preserve foreign files and host overlays). Use --replace to wipe trees.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CURSOR_HOME="${CURSOR_HOME:-$HOME/.cursor}"
EXPECTED_COMMANDS=38
EXPECTED_SKILLS=38

MODE_MERGE=1
MODE_REPLACE=0
DO_PRUNE=0
VERBOSE=0

usage() {
  cat <<'EOF'
Usage: install.sh [OPTIONS]

Symlink cursor-commands catalog into $CURSOR_HOME (default ~/.cursor).

Options:
  (default)     Merge mode — mkdir -p and link catalog entries only; keep other files
  --replace     Remove commands/ and skills/ trees first (legacy full reset)
  --prune       Remove stale symlinks that point into this repo but left the catalog
  -v, --verbose List pruned entry names
  -h, --help    Show this help

Host overlays (e.g. org-specific commands) should install after generic merge, or
re-run the host install script; merge mode does not delete non-catalog symlinks.
EOF
}

resolve_path() {
  local path="$1"
  if command -v realpath >/dev/null 2>&1; then
    realpath "$path" 2>/dev/null || return 1
  else
    python3 -c "import os, sys; print(os.path.realpath(sys.argv[1]))" "$path" 2>/dev/null || return 1
  fi
}

prepare_target_dir() {
  local target="$1"
  local replace="$2"

  if [[ "$replace" -eq 1 ]]; then
    if [[ -e "$target" ]] || [[ -L "$target" ]]; then
      rm -rf "$target"
    fi
    mkdir -p "$target"
    return
  fi

  if [[ -L "$target" ]]; then
    rm -f "$target"
  fi
  mkdir -p "$target"
}

link_catalog() {
  local command_count=0
  local skill_count=0

  for src in "$REPO_ROOT/.cursor/commands/"*.md; do
    [[ -f "$src" ]] || continue
    name="$(basename "$src")"
    ln -sfn "$(cd "$(dirname "$src")" && pwd)/$name" "$CURSOR_HOME/commands/$name"
    command_count=$((command_count + 1))
  done

  for src in "$REPO_ROOT/.cursor/skills/"*/; do
    [[ -d "$src" ]] || continue
    name="$(basename "$src")"
    ln -sfn "$(cd "$src" && pwd)" "$CURSOR_HOME/skills/$name"
    skill_count=$((skill_count + 1))
  done

  echo "$command_count $skill_count"
}

catalog_has_command() {
  local name="$1"
  [[ -f "$REPO_ROOT/.cursor/commands/$name" ]]
}

catalog_has_skill() {
  local name="$1"
  [[ -d "$REPO_ROOT/.cursor/skills/$name" ]]
}

is_repo_managed_symlink() {
  local link="$1"
  local kind="$2"
  local repo_base="$REPO_ROOT/.cursor/$kind"
  local resolved

  [[ -L "$link" ]] || return 1
  resolved="$(resolve_path "$link")" || return 1
  case "$resolved" in
    "$repo_base"/*) return 0 ;;
    *) return 1 ;;
  esac
}

prune_stale() {
  local pruned=0
  local name
  local link

  shopt -s nullglob
  for link in "$CURSOR_HOME/commands/"*.md; do
    [[ -e "$link" || -L "$link" ]] || continue
    name="$(basename "$link")"
    if is_repo_managed_symlink "$link" commands && ! catalog_has_command "$name"; then
      rm -f "$link"
      pruned=$((pruned + 1))
      if [[ "$VERBOSE" -eq 1 ]]; then
        echo "  pruned command: $name"
      fi
    fi
  done

  for link in "$CURSOR_HOME/skills/"*/; do
    [[ -e "$link" || -L "$link" ]] || continue
    name="$(basename "${link%/}")"
    if is_repo_managed_symlink "$link" skills && ! catalog_has_skill "$name"; then
      rm -f "$link"
      pruned=$((pruned + 1))
      if [[ "$VERBOSE" -eq 1 ]]; then
        echo "  pruned skill: $name"
      fi
    fi
  done
  shopt -u nullglob

  echo "$pruned"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --replace)
      MODE_MERGE=0
      MODE_REPLACE=1
      shift
      ;;
    --prune)
      DO_PRUNE=1
      shift
      ;;
    -v | --verbose)
      VERBOSE=1
      shift
      ;;
    -h | --help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown option: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

prepare_target_dir "$CURSOR_HOME/commands" "$MODE_REPLACE"
prepare_target_dir "$CURSOR_HOME/skills" "$MODE_REPLACE"

read -r command_count skill_count <<<"$(link_catalog)"

if [[ "$DO_PRUNE" -eq 1 ]]; then
  pruned="$(prune_stale)"
  if [[ "$pruned" -gt 0 ]]; then
    echo "Pruned $pruned stale catalog symlink(s)"
  fi
fi

errors=0
if [[ "$command_count" -ne "$EXPECTED_COMMANDS" ]]; then
  echo "ERROR: expected $EXPECTED_COMMANDS command symlinks, got $command_count" >&2
  errors=1
fi
if [[ "$skill_count" -ne "$EXPECTED_SKILLS" ]]; then
  echo "ERROR: expected $EXPECTED_SKILLS skill symlinks, got $skill_count" >&2
  errors=1
fi

for src in "$REPO_ROOT/.cursor/commands/"*.md; do
  [[ -f "$src" ]] || continue
  name="$(basename "$src")"
  link="$CURSOR_HOME/commands/$name"
  if [[ -L "$link" ]] && ! test -e "$link"; then
    echo "ERROR: broken catalog command symlink: $link" >&2
    errors=1
  fi
done

for src in "$REPO_ROOT/.cursor/skills/"*/; do
  [[ -d "$src" ]] || continue
  name="$(basename "$src")"
  link="$CURSOR_HOME/skills/$name"
  if [[ -L "$link" ]] && ! test -e "$link"; then
    echo "ERROR: broken catalog skill symlink: $link" >&2
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

if [[ "$MODE_REPLACE" -eq 1 ]]; then
  mode_label="replace"
else
  mode_label="merge"
fi

echo "Installed ($mode_label) $command_count commands and $skill_count skills into $CURSOR_HOME"
echo "Manual Cursor check: docs/VERIFICATION.md"
