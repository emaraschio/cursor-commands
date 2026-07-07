#!/usr/bin/env bash
# CI tests for install.sh merge / replace / prune behavior.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INSTALL="$REPO_ROOT/scripts/install.sh"
failures=0

assert() {
  if ! "$@"; then
    echo "FAIL: $*" >&2
    failures=$((failures + 1))
  fi
}

test_merge_preserves_foreign() {
  local home
  home="$(mktemp -d)"
  mkdir -p "$home/commands" "$home/skills"
  echo "foreign" >"$home/commands/foreign-command.md"
  mkdir -p "$home/skills/foreign-skill"
  echo "skill" >"$home/skills/foreign-skill/SKILL.md"
  ln -sfn /tmp/cm-overlay-dummy "$home/commands/cm-overlay.md"

  CURSOR_HOME="$home" "$INSTALL"

  assert test -f "$home/commands/foreign-command.md"
  assert test -d "$home/skills/foreign-skill"
  assert test -L "$home/commands/cm-overlay.md"
  assert test -f "$home/commands/code-review.md"
  assert test -f "$home/skill-contracts/merge-open-prs/SKILL.md"

  rm -rf "$home"
  echo "OK: merge preserves foreign and overlay symlinks"
}

test_replace_wipes_foreign() {
  local home
  home="$(mktemp -d)"
  mkdir -p "$home/commands" "$home/skills"
  echo "foreign" >"$home/commands/foreign-command.md"

  CURSOR_HOME="$home" "$INSTALL" --replace

  assert test ! -e "$home/commands/foreign-command.md"
  assert test -f "$home/commands/code-review.md"

  rm -rf "$home"
  echo "OK: replace removes foreign files"
}

test_prune_stale_repo_symlink() {
  local home
  home="$(mktemp -d)"
  mkdir -p "$home/commands" "$home/skills"

  ln -sfn "$REPO_ROOT/.cursor/commands/commit.md" "$home/commands/retired-command.md"
  assert test -L "$home/commands/retired-command.md"

  CURSOR_HOME="$home" "$INSTALL" --prune

  assert test ! -e "$home/commands/retired-command.md"
  assert test -f "$home/commands/commit.md"

  rm -rf "$home"
  echo "OK: prune removes stale repo-managed symlink only"
}

test_prune_keeps_overlay_symlink() {
  local home
  home="$(mktemp -d)"
  mkdir -p "$home/commands"
  ln -sfn /tmp/cm-overlay-dummy "$home/commands/cm-overlay.md"

  CURSOR_HOME="$home" "$INSTALL" --prune

  assert test -L "$home/commands/cm-overlay.md"

  rm -rf "$home"
  echo "OK: prune keeps non-repo symlinks"
}

test_uninstall_removes_catalog_keeps_foreign() {
  local home
  home="$(mktemp -d)"
  mkdir -p "$home/commands" "$home/skills"
  echo "foreign" >"$home/commands/foreign-command.md"
  mkdir -p "$home/skills/foreign-skill"
  echo "skill" >"$home/skills/foreign-skill/SKILL.md"
  ln -sfn /tmp/cm-overlay-dummy "$home/commands/cm-overlay.md"

  CURSOR_HOME="$home" "$INSTALL"
  assert test -f "$home/commands/code-review.md"

  CURSOR_HOME="$home" "$INSTALL" --uninstall

  assert test ! -e "$home/commands/code-review.md"
  assert test ! -e "$home/skill-contracts/code-review"
  assert test -f "$home/commands/foreign-command.md"
  assert test -d "$home/skills/foreign-skill"
  assert test -L "$home/commands/cm-overlay.md"

  rm -rf "$home"
  echo "OK: uninstall removes catalog symlinks only"
}

chmod +x "$INSTALL"
test_merge_preserves_foreign
test_replace_wipes_foreign
test_prune_stale_repo_symlink
test_prune_keeps_overlay_symlink
test_uninstall_removes_catalog_keeps_foreign

if [[ "$failures" -ne 0 ]]; then
  echo "ERROR: $failures test assertion(s) failed" >&2
  exit 1
fi

echo "OK: all install tests passed"
