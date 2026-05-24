---
name: generate-pr-description
version: 1
description: Generate PR title and description from branch diff
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/generate-pr-description/eval/cases.md
  ship_gate: [A]
---

## Overview

Generate PR title and description from branch diff. Full workflow: `.cursor/skills/generate-pr-description/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/generate-pr-description/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not omit test plan
- Use conventional commit style for title when appropriate

## Examples

- `/generate-pr-description`

## Maintainers

Behavioral eval: `.cursor/skills/generate-pr-description/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
