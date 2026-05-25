---
name: requirement-to-implementation
version: 1
description: Structured workflow from requirement through plan approval, implementation, verification, and documentation
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/requirement-to-implementation/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Take a requirement (feature, bug, refactor, chore, or performance task) from any source through intake, exploration, an approved plan, implementation, and documentation. Full workflow: `.cursor/skills/requirement-to-implementation/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/requirement-to-implementation/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake → Context → Explore → Plan → [Approve] → Implement → Document); do not skip the approval gate.
3. **Report** outcomes per skill (requirement summary, plan, verification, memory-bank updates as specified).

## Anti-patterns

- Do not implement before the user approves the plan
- Do not skip intake or exploration when the requirement is ambiguous
- Do not commit or push without explicit user request

## Examples

- `/requirement-to-implementation`
- `/requirement-to-implementation` with a GitHub issue URL or pasted ticket

## Maintainers

Behavioral eval: `.cursor/skills/requirement-to-implementation/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
