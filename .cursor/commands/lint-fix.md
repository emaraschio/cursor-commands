---
name: lint-fix
version: 1
description: Fix lint issues in the current file
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/lint-fix/eval/cases.md
  ship_gate: [A]
---

## Overview

Fix lint issues in the current file. Full workflow: `.cursor/skills/lint-fix/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/lint-fix/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not change behavior while fixing style
- Use project linter config

## Examples

- `/lint-fix`

## Maintainers

Behavioral eval: `.cursor/skills/lint-fix/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
