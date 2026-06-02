---
name: define-agent-goal
version: 1
description: Turn a rough task into a six-part agent Goal (outcome, verification, constraints, boundaries, iteration, stopping condition); plan-only, no execution in the same turn
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/define-agent-goal/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Define a six-part agent Goal so an agent can run a task with minimal babysitting. Plan-only — does not execute the task in the same turn. Full workflow: `.cursor/skills/define-agent-goal/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Deliverable | Six-section Goal in chat |
| Execution | None in same turn (follow-up or `requirement-to-implementation`) |
| Ambiguity | Clarify before finalize |
| Examples | Generic names only (`service-a`, `repo1`) |

## Steps

1. **Read** `.cursor/skills/define-agent-goal/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake → Discovery → Draft → Clarify gate → Deliver); do not skip the clarify gate or start executing the task.
3. **Report** the final Goal (sections 1–6); offer optional save under `docs/agent-goals/` when the host has `docs/`.

## Anti-patterns

- Do not skip Goal sections or publish a final Goal with vague autonomy
- Do not execute, edit code, or run destructive commands in the same turn unless the user explicitly skips Goal definition
- Do not claim a native Codex Goals API — this is a portable Goal document
- Do not use employer, product, or internal repo names in examples (OSS catalog)

## Examples

- `/define-agent-goal`
- `/define-agent-goal` with "reduce flaky tests in service-a"

## Maintainers

Behavioral eval: `.cursor/skills/define-agent-goal/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
