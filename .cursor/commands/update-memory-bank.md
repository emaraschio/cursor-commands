---
name: update-memory-bank
version: 1
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

- Do not invent commits or files
- Update only files that changed

## Examples

- `/update-memory-bank`

## Maintainers

Behavioral eval: `.cursor/skills/update-memory-bank/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
