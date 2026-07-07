---
name: lint-fix
version: 2
description: Fix lint issues in the current file
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/lint-fix/eval/cases.md
  ship_gate: [A]
---

## Overview

Fix lint issues in the current file. Full workflow: `.cursor/skill-contracts/lint-fix/SKILL.md` (user install: `~/.cursor/skill-contracts/lint-fix/SKILL.md`).

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/lint-fix/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/lint-fix/SKILL.md`.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Do not change behavior while fixing style.** Trigger: a lint fix that tempts a logic tweak. Wrong: altering runtime behavior under cover of a style fix. Correct: limit edits to formatting and style, leaving behavior unchanged. Reason: behavior changes hidden in a lint pass bypass review and can introduce regressions.
- **Use the project linter config.** Trigger: the repo ships its own linter configuration. Wrong: applying personal rules or a different formatter. Correct: run the project's configured linter and follow its rules. Reason: ad hoc rules create churn and conflict with the agreed project style.

## Examples

- `/lint-fix`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/lint-fix/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
