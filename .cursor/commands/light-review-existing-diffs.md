---
name: light-review-existing-diffs
version: 1
description: Quick review of existing diffs without full PR context
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/light-review-existing-diffs/eval/cases.md
  ship_gate: [A]
---

## Overview

Quick review of existing diffs without full PR context. Full workflow: `.cursor/skills/light-review-existing-diffs/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/light-review-existing-diffs/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not block on nitpicks
- Flag security issues even in light review

## Examples

- `/light-review-existing-diffs`

## Maintainers

Behavioral eval: `.cursor/skills/light-review-existing-diffs/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
