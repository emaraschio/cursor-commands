---
name: light-review-existing-diffs
version: 2
description: Quick review of existing diffs without full PR context
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/light-review-existing-diffs/eval/cases.md
  ship_gate: [A]
---

## Overview

Quick review of existing diffs without full PR context. Full workflow: `.cursor/skill-contracts/light-review-existing-diffs/SKILL.md` (user install: `~/.cursor/skill-contracts/light-review-existing-diffs/SKILL.md`).

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/light-review-existing-diffs/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/light-review-existing-diffs/SKILL.md`.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Do not block on nitpicks.** Trigger: a quick pass that surfaces minor style or preference issues. Wrong: holding up the change over cosmetic nits. Correct: note nits as optional and let the change proceed. Reason: a light review is meant to be fast, so blocking on cosmetics defeats its purpose.
- **Flag security issues even in a light review.** Trigger: spotting a security risk during a quick pass. Wrong: skipping it because the review is meant to be light. Correct: surface the security concern regardless of review depth. Reason: a missed vulnerability is costly no matter how quick the pass was.

## Examples

- `/light-review-existing-diffs`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/light-review-existing-diffs/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
