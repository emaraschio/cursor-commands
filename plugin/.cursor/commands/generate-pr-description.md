---
name: generate-pr-description
version: 2
description: Generate PR title and description from branch diff
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/generate-pr-description/eval/cases.md
  ship_gate: [A]
---

## Overview

Generate PR title and description from branch diff. Full workflow: `.cursor/skills/generate-pr-description/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/generate-pr-description/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Always include a test plan.** Trigger: writing the PR description. Wrong: omitting how the change was tested. Correct: include a test plan describing how the changes were verified. Reason: reviewers cannot judge risk without knowing what was tested.
- **Use a Conventional Commits title.** Trigger: writing the PR title. Wrong: a vague title that ignores the convention. Correct: use Conventional Commits style for the title when appropriate. Reason: the title feeds the squash-merge commit and the changelog.

## Examples

- `/generate-pr-description`

## Maintainers

Behavioral eval: `.cursor/skills/generate-pr-description/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
