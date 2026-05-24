---
name: optimize-performance
version: 1
description: Profile and optimize performance bottlenecks
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/optimize-performance/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Profile and optimize performance bottlenecks. Full workflow: `.cursor/skills/optimize-performance/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/optimize-performance/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not optimize without measuring first
- Do not trade readability for micro-gains

## Examples

- `/optimize-performance`

## Maintainers

Behavioral eval: `.cursor/skills/optimize-performance/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
