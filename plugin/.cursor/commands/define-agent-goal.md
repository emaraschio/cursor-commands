---
name: define-agent-goal
version: 2
description: Turn a rough task into a six-part agent Goal (outcome, verification, constraints, boundaries, iteration, stopping condition); plan-only, no execution in the same turn
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/define-agent-goal/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Define a six-part agent Goal so an agent can run a task with minimal babysitting. Plan-only. Does not execute the task in the same turn. Full workflow: `.cursor/skill-contracts/define-agent-goal/SKILL.md` (user install: `~/.cursor/skill-contracts/define-agent-goal/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Deliverable | Six-section Goal in chat |
| Execution | None in same turn (follow-up or `requirement-to-implementation`) |
| Ambiguity | Clarify before finalize |
| Examples | Generic names only (`service-a`, `repo1`) |

## Steps

1. **Read** `.cursor/skill-contracts/define-agent-goal/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/define-agent-goal/SKILL.md`.
2. **Execute** phases in order (Intake → Discovery → Draft → Clarify gate → Deliver); do not skip the clarify gate or start executing the task.
3. **Report** the final Goal (sections 1 to 6); offer optional save under `docs/agent-goals/` when the host has `docs/`.

## Anti-patterns

- **Complete every Goal section with bounded autonomy.** Trigger: drafting the final Goal from a vague task. Wrong: publishing with missing sections or vague autonomy like "fix everything". Correct: clarify first, fill all six sections, and keep boundaries narrow. Reason: an under-specified Goal lets the agent act far beyond what the user intended.
- **Define the Goal without executing it.** Trigger: delivering the Goal. Wrong: editing code or running destructive commands in the same turn. Correct: stop at the Goal unless the user explicitly says to skip Goal definition and execute now. Reason: this skill is plan-only, so acting without that explicit consent risks unwanted or irreversible changes.
- **Do not claim a native Goals product feature.** Reason: this is a portable Goal document for Cursor agents, and implying a built-in Goals API would mislead the user.

## Examples

- `/define-agent-goal`
- `/define-agent-goal` with "reduce flaky tests in service-a"

## Maintainers

Behavioral eval: `.cursor/skill-contracts/define-agent-goal/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
