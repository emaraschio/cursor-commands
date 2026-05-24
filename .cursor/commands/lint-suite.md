---
name: lint-suite
version: 1
description: Run project linters and fix findings repo-wide
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/lint-suite/eval/cases.md
  ship_gate: [A]
---

## Overview

Run project linters and fix findings repo-wide. Full workflow: `.cursor/skills/lint-suite/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/lint-suite/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not disable rules to pass
- Re-run linter to verify zero issues

## Examples

- `/lint-suite`

## Maintainers

Behavioral eval: `.cursor/skills/lint-suite/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
