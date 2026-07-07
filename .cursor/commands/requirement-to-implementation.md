---
name: requirement-to-implementation
version: 2
description: Structured workflow from requirement through plan approval, implementation, verification, and documentation
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/requirement-to-implementation/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Take a requirement (feature, bug, refactor, chore, or performance task) from any source through intake, exploration, an approved plan, implementation, and documentation. Full workflow: `.cursor/skill-contracts/requirement-to-implementation/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/requirement-to-implementation/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake → Context → Explore → Plan → [Approve] → Implement → Document); do not skip the approval gate.
3. **Report** outcomes per skill (requirement summary, plan, verification, memory-bank updates as specified).

## Anti-patterns

- **Do not implement before plan approval.** Trigger: the user asks to implement immediately. Wrong: writing production code before presenting a plan and getting approval. Correct: present the structured plan and wait for explicit approval before implementing. Reason: plans are cheap and rework is expensive, and unapproved changes can go the wrong direction.
- **Do not skip intake or exploration.** Trigger: an ambiguous requirement. Wrong: jumping to a plan without intake questions or codebase exploration. Correct: run intake and exploration to map the blast radius before planning. Reason: skipping discovery produces plans that miss affected files and risks.
- **Commit only when asked.** Trigger: finishing implementation. Wrong: committing or pushing without an explicit request. Correct: stop after verifying and let the user request the commit. Reason: surprise commits and pushes are hard to undo.

## Examples

- `/requirement-to-implementation`
- `/requirement-to-implementation` with a GitHub issue URL or pasted ticket

## Maintainers

Behavioral eval: `.cursor/skill-contracts/requirement-to-implementation/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
