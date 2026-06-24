---
name: fix-compile-errors
version: 2
description: Fix compilation/type errors with minimal diff
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/fix-compile-errors/eval/cases.md
  ship_gate: [A]
---

## Overview

Fix compilation/type errors with minimal diff. Full workflow: `.cursor/skills/fix-compile-errors/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/fix-compile-errors/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Fix the error, do not disable the check.** Trigger: a type or compile check is failing. Wrong: suppressing the error, loosening types to any, or turning the check off to force a green build. Correct: address the real type or compile mismatch with the smallest correct change. Reason: silencing the check ships the broken code it was built to catch.
- **Stay minimal; do not refactor while fixing.** Trigger: noticing messy code near the compile error. Wrong: refactoring or reorganizing in the same pass as the fix. Correct: make the minimal diff that compiles and note refactors separately. Reason: mixing refactors with the fix bloats the diff and hides what actually resolved the error.

## Examples

- `/fix-compile-errors`

## Maintainers

Behavioral eval: `.cursor/skills/fix-compile-errors/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
