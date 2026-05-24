---
name: fix-compile-errors
version: 1
description: Fix compilation/type errors with minimal diff
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/fix-compile-errors/eval/cases.md
  ship_gate: [A]
---

## Overview

Fix compilation/type errors with minimal diff. Full workflow: `.cursor/skills/fix-compile-errors/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/fix-compile-errors/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not disable checks to green-build
- Do not refactor while fixing compile errors

## Examples

- `/fix-compile-errors`

## Maintainers

Behavioral eval: `.cursor/skills/fix-compile-errors/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
