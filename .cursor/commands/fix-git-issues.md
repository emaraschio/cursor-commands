---
name: fix-git-issues
version: 1
description: Diagnose and fix git state problems
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/fix-git-issues/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Diagnose and fix git state problems. Full workflow: `.cursor/skills/fix-git-issues/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/fix-git-issues/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not run destructive git without consent
- Do not force-push main

## Examples

- `/fix-git-issues`

## Maintainers

Behavioral eval: `.cursor/skills/fix-git-issues/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
