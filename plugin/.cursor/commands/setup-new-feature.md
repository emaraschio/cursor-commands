---
name: setup-new-feature
version: 2
description: Scaffold a new feature across layers
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/setup-new-feature/eval/cases.md
  ship_gate: [A]
---

## Overview

Scaffold a new feature across layers. Full workflow: `.cursor/skills/setup-new-feature/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/setup-new-feature/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Do not over-engineer the scaffold.** Trigger: standing up the structure for a new feature. Wrong: adding layers, abstractions, or files the feature does not yet need. Correct: scaffold the minimum the feature requires and grow it as real needs appear. Reason: speculative structure is dead weight every later change has to carry.
- **Match the existing project structure.** Trigger: deciding where new files and modules belong. Wrong: inventing a new layout or convention beside the established one. Correct: mirror the repository's existing structure, naming, and conventions. Reason: a divergent layout fragments the codebase and slows everyone who navigates it.

## Examples

- `/setup-new-feature`

## Maintainers

Behavioral eval: `.cursor/skills/setup-new-feature/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
