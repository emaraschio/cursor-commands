---
name: update-readme
version: 2
description: Update project README for current state
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/update-readme/eval/cases.md
  ship_gate: [A]
---

## Overview

Update project README for current state. Full workflow: `.cursor/skills/update-readme/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/update-readme/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Preserve required README sections.** Trigger: updating the README. Wrong: deleting required sections such as Installation, Usage, Configuration, or Troubleshooting. Correct: update drifted content while keeping required sections intact. Reason: removing required sections strips setup steps users depend on.
- **Keep internal links valid.** Trigger: editing or moving content. Wrong: leaving broken or stale internal links. Correct: validate internal links and fix broken paths. Reason: broken links send readers to dead ends.

## Examples

- `/update-readme`

## Maintainers

Behavioral eval: `.cursor/skills/update-readme/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
