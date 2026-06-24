---
name: add-documentation
version: 2
description: Add or improve code documentation for the current change
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/add-documentation/eval/cases.md
  ship_gate: [A]
---

## Overview

Add or improve code documentation for the current change. Full workflow: `.cursor/skills/add-documentation/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/add-documentation/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Document what the code cannot say.** Trigger: adding docs for a change. Wrong: annotating obvious one-liners with comments that restate the code. Correct: document intent, contracts, and edge cases the code does not convey. Reason: redundant comments add noise and drift out of date.
- **Match the project's documentation style.** Trigger: choosing how and where to document. Wrong: inventing a new format or location. Correct: follow the existing documentation style and place docs where the project keeps them. Reason: inconsistent docs are hard to find and maintain.

## Examples

- `/add-documentation`

## Maintainers

Behavioral eval: `.cursor/skills/add-documentation/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
