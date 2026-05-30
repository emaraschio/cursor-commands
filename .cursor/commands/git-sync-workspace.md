---
name: git-sync-workspace
version: 1
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

- Do not `git reset --hard` or sync over a dirty working tree without explicit approval
- Do not force-push default branches
- Do not guess repo paths outside workspace discovery or user scope
- Do not confuse this with `fix-git-issues` for merge conflicts on a single repo

## Examples

- `/git-sync-workspace`
- `/git-sync-workspace` with "only sync repo1 and repo2"

## Maintainers

Behavioral eval: `.cursor/skills/git-sync-workspace/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
