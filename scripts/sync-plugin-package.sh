#!/usr/bin/env bash
# Materialize plugin/ for Cursor folder installs (avoids copying .git sockets).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLUGIN_ROOT="$REPO_ROOT/plugin"
CHECK_ONLY=0

usage() {
  cat <<'EOF'
Usage: sync-plugin-package.sh [--check]

Copy catalog commands/skills into plugin/ for Cursor marketplace folder installs.
Without --check, updates plugin/.cursor/ and plugin/.cursor-plugin/plugin.json.
With --check, exits non-zero when plugin/ is out of sync.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --check) CHECK_ONLY=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage >&2; exit 1 ;;
  esac
done

sync_tree() {
  local src="$1"
  local dest="$2"
  if [[ "$CHECK_ONLY" -eq 1 ]]; then
    rsync -a --delete --dry-run --itemize-changes "$src" "$dest" | grep -q '^[<>ch]' && return 1
    return 0
  fi
  mkdir -p "$(dirname "$dest")"
  rsync -a --delete "$src" "$dest"
}

mkdir -p "$PLUGIN_ROOT/.cursor-plugin"

if [[ "$CHECK_ONLY" -eq 1 ]]; then
  failed=0
  sync_tree "$REPO_ROOT/.cursor/commands/" "$PLUGIN_ROOT/.cursor/commands/" || failed=1
  sync_tree "$REPO_ROOT/.cursor/skills/" "$PLUGIN_ROOT/.cursor/skills/" || failed=1
  if ! cmp -s "$REPO_ROOT/.cursor-plugin/plugin.json" "$PLUGIN_ROOT/.cursor-plugin/plugin.json" 2>/dev/null; then
    failed=1
  fi
  if [[ "$failed" -ne 0 ]]; then
    echo "ERROR: plugin/ package is out of sync; run ./scripts/sync-plugin-package.sh" >&2
    exit 1
  fi
  echo "OK: plugin package in sync"
  exit 0
fi

sync_tree "$REPO_ROOT/.cursor/commands/" "$PLUGIN_ROOT/.cursor/commands/"
sync_tree "$REPO_ROOT/.cursor/skills/" "$PLUGIN_ROOT/.cursor/skills/"
cp "$REPO_ROOT/.cursor-plugin/plugin.json" "$PLUGIN_ROOT/.cursor-plugin/plugin.json"
echo "Synced plugin package to $PLUGIN_ROOT"
