---
name: address-github-pr-comments
version: 1
description: Address review comments on the current GitHub PR
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/address-github-pr-comments/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Address review comments on the current GitHub PR. Full workflow: `.cursor/skills/address-github-pr-comments/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/address-github-pr-comments/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not push without user request
- Do not dismiss valid security feedback

## Examples

- `/address-github-pr-comments`

## Maintainers

Behavioral eval: `.cursor/skills/address-github-pr-comments/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
