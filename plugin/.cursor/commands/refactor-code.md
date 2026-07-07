---
name: refactor-code
version: 2
description: Refactor for clarity without behavior change
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/refactor-code/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Refactor for clarity without behavior change. Full workflow: `.cursor/skill-contracts/refactor-code/SKILL.md` (user install: `~/.cursor/skill-contracts/refactor-code/SKILL.md`).

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/refactor-code/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/refactor-code/SKILL.md`.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Preserve behavior.** Trigger: restructuring a unit of code. Wrong: altering observable behavior or output while refactoring. Correct: keep behavior identical and lean on existing tests to confirm. Reason: a refactor that changes behavior is a hidden functional change reviewers will not expect.
- **Stay within the refactor target.** Trigger: noticing other improvable code nearby. Wrong: expanding the refactor into unrelated files or features. Correct: limit changes to the agreed target and note the rest separately. Reason: scope creep makes the diff hard to review and risks unrelated regressions.

## Examples

- `/refactor-code`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/refactor-code/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
