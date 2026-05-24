---
name: refactor-code
version: 1
description: Refactor for clarity without behavior change
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/refactor-code/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Refactor for clarity without behavior change. Full workflow: `.cursor/skills/refactor-code/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/refactor-code/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not change behavior
- Do not expand scope beyond refactor target

## Examples

- `/refactor-code`

## Maintainers

Behavioral eval: `.cursor/skills/refactor-code/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
