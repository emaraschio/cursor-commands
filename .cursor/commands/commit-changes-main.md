---
name: commit-changes-main
version: 1
description: Commit directly on main/master when explicitly allowed
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/commit-changes-main/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Commit directly on main/master when explicitly allowed. Full workflow: `.cursor/skills/commit-changes-main/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/commit-changes-main/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not commit to main without explicit user consent
- Do not force-push main

## Examples

- `/commit-changes-main`

## Maintainers

Behavioral eval: `.cursor/skills/commit-changes-main/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
