---
name: commit
version: 2
description: Commit on a new branch with conventional message
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/commit/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Commit on a new branch with conventional message. Full workflow: `.cursor/skill-contracts/commit/SKILL.md` (user install: `~/.cursor/skill-contracts/commit/SKILL.md`).

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/commit/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/commit/SKILL.md`.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Commit only when asked.** Trigger: finishing a chunk of work. Wrong: committing or pushing without being asked. Correct: commit only on explicit request, then push the branch. Reason: surprise commits and pushes are hard to undo and disrupt the user's flow.
- **Use Conventional Commits.** Trigger: writing the commit message. Wrong: a vague or non-conventional subject. Correct: a Conventional Commits subject within the length limit. Reason: the squashed message becomes the PR title.
- **Never skip hooks or amend a failed commit.** Trigger: a pre-commit hook fails. Wrong: re-running with hooks skipped or amending the failed commit. Correct: fix the issue and make a new commit. Reason: skipped hooks hide failures and amending a failed commit loses the trail.

## Examples

- `/commit`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/commit/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
