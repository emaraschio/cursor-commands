---
name: update-memory-bank
version: 2
description: Sync memory bank with repository state
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/update-memory-bank/eval/cases.md
  ship_gate: [A]
---

## Overview

Sync memory bank with repository state. Full workflow: `.cursor/skills/update-memory-bank/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/update-memory-bank/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Record only verified state.** Trigger: writing memory bank entries. Wrong: inventing commits, files, or statistics. Correct: confirm commit hashes and descriptions against git log before recording them. Reason: fabricated history makes the memory bank untrustworthy.
- **Update only what changed.** Trigger: choosing which memory bank files to edit. Wrong: rewriting files whose domain did not change. Correct: update only the files whose domain actually changed. Reason: needless edits create churn and hide real updates.

## Examples

- `/update-memory-bank`

## Maintainers

Behavioral eval: `.cursor/skills/update-memory-bank/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
