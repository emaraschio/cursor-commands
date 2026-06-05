---
name: agent-work-receipt
version: 1
description: Conservative six-section receipt of completed agent-assisted work (output, time, review, risk, value)
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/agent-work-receipt/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Produce a conservative agent work receipt after completed work — finished output, time estimates, review burden, risks, and value judgment. Retrospective only; no new implementation in the same turn. Full workflow: `.cursor/skills/agent-work-receipt/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Scope | Full session unless user narrows in the message |
| Time fields | Agent estimates, labeled as estimates |
| Evidence | Conversation + read-only git (`status`, `diff`, `log`) when repo present |
| Execution | Retrospective only — no new implementation in same turn |
| Examples | Generic names only (`service-a`, `repo1`) |

## Steps

1. **Read** `.cursor/skills/agent-work-receipt/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake → Evidence → Inventory → Estimates → Review & risk → Value → Deliver).
3. **Report** the six-section receipt in chat using the skill template.

## Anti-patterns

- Do not count drafts, ideas, or unused output as finished work
- Do not default to "major time saver" without evidence
- Do not start new implementation, commits, or destructive commands in the same turn
- Do not invent elapsed time as fact — estimates only
- Do not use employer, product, or internal repo names in examples (OSS catalog)

## Examples

- `/agent-work-receipt` after a coding session with landed changes
- `/agent-work-receipt` for "the refactor in service-a" — scoped receipt

## Maintainers

Behavioral eval: `.cursor/skills/agent-work-receipt/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
