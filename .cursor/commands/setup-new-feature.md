---
name: setup-new-feature
version: 1
description: Scaffold a new feature across layers
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/setup-new-feature/eval/cases.md
  ship_gate: [A]
---

## Overview

Scaffold a new feature across layers. Full workflow: `.cursor/skills/setup-new-feature/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/setup-new-feature/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not over-engineer scaffold
- Follow existing project structure

## Examples

- `/setup-new-feature`

## Maintainers

Behavioral eval: `.cursor/skills/setup-new-feature/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
