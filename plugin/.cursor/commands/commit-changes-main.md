---
name: commit-changes-main
version: 2
description: Commit directly on main/master when explicitly allowed
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/commit-changes-main/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Commit directly on main/master when explicitly allowed. Full workflow: `.cursor/skill-contracts/commit-changes-main/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/commit-changes-main/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Commit to main only with explicit consent.** Trigger: changes are ready while the current branch is main or master. Wrong: committing or pushing to the shared default branch without being asked. Correct: confirm explicit consent first, otherwise move the work to a separate branch. Reason: commits to a shared default branch land for everyone immediately and are disruptive to undo.
- **Never force-push main.** Reason: a force-push to a shared branch rewrites published history teammates have already pulled, which can erase their work.

## Examples

- `/commit-changes-main`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/commit-changes-main/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
