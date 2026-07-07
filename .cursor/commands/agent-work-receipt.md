---
name: agent-work-receipt
version: 2
description: Conservative six-section receipt of completed agent-assisted work (output, time, review, risk, value)
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/agent-work-receipt/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Produce a conservative agent work receipt after completed work: finished output, time estimates, review burden, risks, and value judgment. Retrospective only; no new implementation in the same turn. Full workflow: `.cursor/skill-contracts/agent-work-receipt/SKILL.md` (user install: `~/.cursor/skill-contracts/agent-work-receipt/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Scope | Full session unless user narrows in the message |
| Time fields | Agent estimates, labeled as estimates |
| Evidence | Conversation + read-only git (`status`, `diff`, `log`) when repo present |
| Execution | Retrospective only, no new implementation in same turn |
| Examples | Generic names only (`service-a`, `repo1`) |

## Steps

1. **Read** `.cursor/skill-contracts/agent-work-receipt/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/agent-work-receipt/SKILL.md`.
2. **Execute** phases in order (Intake → Evidence → Inventory → Estimates → Review & risk → Value → Deliver).
3. **Report** the six-section receipt in chat using the skill template.

## Anti-patterns

- **Count only landed work, not drafts.** Trigger: tallying finished output. Wrong: counting drafts, ideas, or abandoned attempts as completed work. Correct: list only artifacts that actually landed and stay conservative. Reason: a receipt that counts unused output overstates value and misleads the decision it informs.
- **Stay retrospective; start no new work.** Trigger: writing the receipt for a finished session. Wrong: starting new implementation, commits, or destructive commands in the same turn. Correct: account for completed work only and defer new work to a separate turn. Reason: a receipt that mutates the repo it is measuring corrupts its own evidence.
- **Label time as estimates, never measured fact.** Trigger: reporting human baseline and agent-assisted time. Wrong: presenting invented durations as measured elapsed time, or inflating savings to match a request. Correct: give estimates labeled as estimates and backed by evidence. Reason: fabricated time figures turn the receipt into marketing rather than accounting.

## Examples

- `/agent-work-receipt` after a coding session with landed changes
- `/agent-work-receipt` for "the refactor in service-a" (scoped receipt)

## Maintainers

Behavioral eval: `.cursor/skill-contracts/agent-work-receipt/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
