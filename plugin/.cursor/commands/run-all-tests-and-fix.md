---
name: run-all-tests-and-fix
version: 2
description: Run full test suite and fix failures
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/run-all-tests-and-fix/eval/cases.md
  ship_gate: [A]
---

## Overview

Run full test suite and fix failures. Full workflow: `.cursor/skill-contracts/run-all-tests-and-fix/SKILL.md` (user install: `~/.cursor/skill-contracts/run-all-tests-and-fix/SKILL.md`).

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/run-all-tests-and-fix/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/run-all-tests-and-fix/SKILL.md`.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Fix the cause, never delete a test to go green.** Trigger: a test fails and the fix is not obvious. Wrong: deleting, commenting out, or weakening the test so the suite passes. Correct: find the root cause and fix the code, or correct the test only if it asserts the wrong thing. Reason: deleting a failing test hides the very regression it was built to catch.
- **Never silently skip a failing test.** Trigger: a test is flaky or slow to fix. Wrong: marking it skipped or pending and moving on without telling anyone. Correct: report the failure and its reason, and track any deferred fix. Reason: silent skips rot into permanent blind spots in the suite.

## Examples

- `/run-all-tests-and-fix`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/run-all-tests-and-fix/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
