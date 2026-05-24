---
name: add-error-handling
version: 1
description: Add consistent error handling to the targeted code
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/add-error-handling/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Add consistent error handling to the targeted code. Full workflow: `.cursor/skills/add-error-handling/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/add-error-handling/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not swallow errors silently
- Do not add excessive try/catch layers

## Examples

- `/add-error-handling`

## Maintainers

Behavioral eval: `.cursor/skills/add-error-handling/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
