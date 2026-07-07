---
name: fix-git-issues
version: 2
description: Diagnose and fix git state problems
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/fix-git-issues/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Diagnose and fix git state problems. Full workflow: `.cursor/skill-contracts/fix-git-issues/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/fix-git-issues/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Get consent before destructive git commands.** Trigger: a fix needs reset, rebase, or a history rewrite. Wrong: running the destructive command without asking. Correct: explain the effect and get explicit consent first. Reason: reset and rebase can discard committed work that cannot be recovered.
- **Never force-push a shared branch.** Trigger: a rebase or amend leaves the local branch behind the remote. Wrong: force-pushing main to make it line up. Correct: prefer a safe reconcile, and never force-push a shared branch without an explicit request. Reason: a force-push to main rewrites history others have pulled and can erase their work.

## Examples

- `/fix-git-issues`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/fix-git-issues/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
