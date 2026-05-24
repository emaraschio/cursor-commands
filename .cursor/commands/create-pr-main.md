---
name: create-pr-main
version: 1
description: Create a pull request targeting main
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/create-pr-main/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Create a pull request targeting main. Full workflow: `.cursor/skills/create-pr-main/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/create-pr-main/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not push without user request
- Do not create empty PRs

## Examples

- `/create-pr-main`

## Maintainers

Behavioral eval: `.cursor/skills/create-pr-main/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
