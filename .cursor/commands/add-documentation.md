---
name: add-documentation
version: 1
description: Add or improve code documentation for the current change
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/add-documentation/eval/cases.md
  ship_gate: [A]
---

## Overview

Add or improve code documentation for the current change. Full workflow: `.cursor/skills/add-documentation/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/add-documentation/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not document obvious one-liners
- Match project doc style

## Examples

- `/add-documentation`

## Maintainers

Behavioral eval: `.cursor/skills/add-documentation/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
