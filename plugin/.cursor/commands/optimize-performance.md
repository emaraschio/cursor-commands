---
name: optimize-performance
version: 2
description: Profile and optimize performance bottlenecks
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/optimize-performance/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Profile and optimize performance bottlenecks. Full workflow: `.cursor/skill-contracts/optimize-performance/SKILL.md` (user install: `~/.cursor/skill-contracts/optimize-performance/SKILL.md`).

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/optimize-performance/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/optimize-performance/SKILL.md`.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Measure before optimizing.** Trigger: a suspected performance problem. Wrong: rewriting code based on a guess about what is slow. Correct: profile to find the real bottleneck, then optimize it. Reason: unmeasured optimizations often target the wrong code and add complexity for no gain.
- **Do not trade readability for micro-gains.** Trigger: a change that shaves a negligible amount of time. Wrong: obscuring the code for an unmeasurable speedup. Correct: keep the readable version unless the gain is significant and measured. Reason: unreadable code costs more in maintenance than a micro-optimization saves.

## Examples

- `/optimize-performance`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/optimize-performance/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
