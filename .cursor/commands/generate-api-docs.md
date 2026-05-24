---
name: generate-api-docs
version: 1
description: Generate API documentation from code
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/generate-api-docs/eval/cases.md
  ship_gate: [A]
---

## Overview

Generate API documentation from code. Full workflow: `.cursor/skills/generate-api-docs/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/generate-api-docs/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not invent endpoints not in code
- Do not expose secrets in examples

## Examples

- `/generate-api-docs`

## Maintainers

Behavioral eval: `.cursor/skills/generate-api-docs/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
