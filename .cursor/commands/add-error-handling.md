---
name: add-error-handling
version: 2
description: Add consistent error handling to the targeted code
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/add-error-handling/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Add consistent error handling to the targeted code. Full workflow: `.cursor/skills/add-error-handling/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/add-error-handling/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Never swallow an error silently.** Trigger: catching an exception you cannot fully handle. Wrong: an empty catch block, or one that hides the failure with no log or rethrow. Correct: handle it meaningfully, or log and rethrow so the failure stays visible. Reason: swallowed errors turn real failures into silent data loss and undebuggable behavior.
- **Do not wrap everything in try/catch.** Trigger: deciding where to add error handling. Wrong: blanket try/catch on every call and layer regardless of risk. Correct: handle errors at meaningful boundaries where you can recover or report. Reason: excessive handling buries the happy path and masks where failures truly originate.

## Examples

- `/add-error-handling`

## Maintainers

Behavioral eval: `.cursor/skills/add-error-handling/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
