---
name: commit-same-branch
version: 1
description: Commit on the current branch with conventional message
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/commit-same-branch/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Commit on the current branch with conventional message. Full workflow: `.cursor/skills/commit-same-branch/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/commit-same-branch/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not commit without user request
- Do not push unless asked

## Examples

- `/commit-same-branch`

## Maintainers

Behavioral eval: `.cursor/skills/commit-same-branch/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
