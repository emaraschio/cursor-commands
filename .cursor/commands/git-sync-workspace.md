---
name: git-sync-workspace
version: 2
description: Sync git repos in a Cursor workspace to remote default branch (fetch, checkout default, pull --ff-only); skip dirty repos
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/git-sync-workspace/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Discover git repos in a Cursor multi-root workspace, preflight each one, and sync clean repos to their remote default branch. Skips dirty or unsafe repos with a clear report. Full workflow: `.cursor/skills/git-sync-workspace/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Dirty repos | Skip and report (no writes) |
| Pull strategy | `--ff-only` |
| Fetch | `--all --prune` |
| Concurrency | ≤ 6 parallel fetches |

## Steps

1. **Read** `.cursor/skills/git-sync-workspace/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Discover → Preflight → Sync → Report); do not skip preflight or modify dirty repos.
3. **Report** the workspace summary (Synced / Skipped / Failed).

## Anti-patterns

- **Never sync over a dirty working tree.** Trigger: a repo has uncommitted changes. Wrong: checking out or pulling over the dirty tree, or running `git reset --hard` to force it. Correct: skip the repo, record `skipped_dirty`, and continue the others. Reason: overwriting a dirty tree can destroy uncommitted work that is not recoverable.
- **Do not force-push default branches.** Reason: force-pushing a shared default branch can erase teammates' commits and rewrite published history.
- **Do not guess repo paths.** Trigger: workspace discovery yields nothing. Wrong: scanning arbitrary directories like `~/code/*` without direction. Correct: ask the user which paths to include. Reason: syncing repos the user did not intend can disrupt unrelated work.

## Examples

- `/git-sync-workspace`
- `/git-sync-workspace` with "only sync repo1 and repo2"

## Maintainers

Behavioral eval: `.cursor/skills/git-sync-workspace/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
