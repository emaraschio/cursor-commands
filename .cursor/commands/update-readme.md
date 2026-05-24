---
name: update-readme
version: 1
description: Update project README for current state
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/update-readme/eval/cases.md
  ship_gate: [A]
---

## Overview

Update project README for current state. Full workflow: `.cursor/skills/update-readme/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/update-readme/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not remove required README sections
- Keep links valid

## Examples

- `/update-readme`

## Maintainers

Behavioral eval: `.cursor/skills/update-readme/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
