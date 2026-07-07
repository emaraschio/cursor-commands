---
name: commit-same-branch
version: 2
description: Commit on the current branch with conventional message
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/commit-same-branch/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Commit on the current branch with conventional message. Full workflow: `.cursor/skill-contracts/commit-same-branch/SKILL.md` (user install: `~/.cursor/skill-contracts/commit-same-branch/SKILL.md`).

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/commit-same-branch/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/commit-same-branch/SKILL.md`.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Commit only when asked.** Trigger: a chunk of work is finished on the current branch. Wrong: committing automatically without being asked. Correct: commit only on an explicit request from the user. Reason: unrequested commits clutter history and surprise the user.
- **Push only when asked.** Trigger: a commit has just been made on the branch. Wrong: pushing to the remote without being asked. Correct: keep the commit local until the user requests a push. Reason: an unrequested push publishes work the user may not be ready to share.

## Examples

- `/commit-same-branch`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/commit-same-branch/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
