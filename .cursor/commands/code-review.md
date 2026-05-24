---
name: code-review
version: 1
description: Thorough PR code review before approval
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/code-review/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Thorough PR code review before approval. Full workflow: `.cursor/skills/code-review/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/code-review/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not approve without checking security and tests
- Do not nitpick style over substance

## Examples

- `/code-review`

## Maintainers

Behavioral eval: `.cursor/skills/code-review/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
