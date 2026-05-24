---
name: write-unit-tests
version: 1
description: Write meaningful unit tests for target code
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/write-unit-tests/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Write meaningful unit tests for target code. Full workflow: `.cursor/skills/write-unit-tests/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/write-unit-tests/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not test implementation trivia
- Do not mock everything

## Examples

- `/write-unit-tests`

## Maintainers

Behavioral eval: `.cursor/skills/write-unit-tests/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
