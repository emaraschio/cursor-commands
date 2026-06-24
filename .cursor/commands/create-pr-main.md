---
name: create-pr-main
version: 2
description: Create a pull request targeting main
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/create-pr-main/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Create a pull request targeting main. Full workflow: `.cursor/skills/create-pr-main/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/create-pr-main/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Push only when asked.** Trigger: the branch is ready to open a pull request. Wrong: pushing to the remote without being asked. Correct: push only on an explicit request before opening the PR. Reason: an unrequested push publishes work the user may not want shared yet.
- **Do not open empty PRs.** Trigger: the branch has no commits ahead of the base. Wrong: opening a pull request with no diff to review. Correct: confirm there are real changes first, otherwise hold off. Reason: an empty PR wastes reviewer time and clutters the review queue.

## Examples

- `/create-pr-main`

## Maintainers

Behavioral eval: `.cursor/skills/create-pr-main/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
