---
name: debug-issue
version: 2
description: Systematically debug a reported issue
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/debug-issue/eval/cases.md
  ship_gate: [A]
---

## Overview

Systematically debug a reported issue. Full workflow: `.cursor/skills/debug-issue/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/debug-issue/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Diagnose from evidence, not guesses.** Trigger: an error with no obvious cause. Wrong: patching a likely-looking line before reproducing. Correct: reproduce, trace the failing path, then change the smallest thing. Reason: speculative fixes mask the real fault and add churn.
- **Stay inside the reported fault.** Trigger: spotting unrelated smells mid-debug. Wrong: refactoring adjacent code in the same pass. Correct: note it separately and fix only the bug. Reason: mixed diffs hide the regression and are unreviewable.

## Examples

- `/debug-issue`

## Maintainers

Behavioral eval: `.cursor/skills/debug-issue/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
