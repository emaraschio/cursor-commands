---
name: debug-issue
version: 1
description: Systematically debug a reported issue
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/debug-issue/eval/cases.md
  ship_gate: [A]
---

## Overview

Systematically debug a reported issue. Full workflow: `.cursor/skills/debug-issue/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/debug-issue/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not guess without evidence
- Do not change unrelated code

## Examples

- `/debug-issue`

## Maintainers

Behavioral eval: `.cursor/skills/debug-issue/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
