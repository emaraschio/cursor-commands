---
name: run-all-tests-and-fix
version: 1
description: Run full test suite and fix failures
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/run-all-tests-and-fix/eval/cases.md
  ship_gate: [A]
---

## Overview

Run full test suite and fix failures. Full workflow: `.cursor/skills/run-all-tests-and-fix/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/run-all-tests-and-fix/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not delete tests to pass
- Do not skip failing tests without reporting

## Examples

- `/run-all-tests-and-fix`

## Maintainers

Behavioral eval: `.cursor/skills/run-all-tests-and-fix/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
