---
name: define-agent-goal
version: 3
description: Turn a rough task into an agent Goal (six core sections, 3 to 5 success criteria, helper goals when parallel, approval gate); plan-only, no execution in the same turn
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/define-agent-goal/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Define an agent Goal using **human-reviewed autonomy**: the agent drafts what done means, how to verify it, boundaries, and (when parallelism is implied) per-helper mini-goals; you approve or edit before any execution. Plan-only. Does not execute the task in the same turn. Full workflow: `.cursor/skill-contracts/define-agent-goal/SKILL.md` (user install: `~/.cursor/skill-contracts/define-agent-goal/SKILL.md`). End-user notes: `.cursor/skill-contracts/define-agent-goal/reference.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Deliverable | Goal in chat (sections 1 to 6; section 7 when parallel work is implied) |
| Success criteria | 3 to 5 checkboxes under Verification |
| Execution | None in same turn (follow-up or `requirement-to-implementation`) |
| Discovery | Fast path when full intake template is provided and unambiguous |
| Persistence | Opt-in save to `docs/agent-goals/<slug>.md` only after explicit user confirm |
| Examples | Generic names only (`service-a`, `repo1`) |

## Steps

1. **Read** `.cursor/skill-contracts/define-agent-goal/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/define-agent-goal/SKILL.md`.
2. **Execute** phases in order (Intake → Discovery [or fast path] → Draft → Clarify gate → Deliver); do not skip the clarify gate or start executing the task.
3. **Report** the final Goal with 3 to 5 success criteria, approval handshake, copyable intake template for reuse, and section 7 helper goals when parallelism applies.
4. **Offer** optional save under `docs/agent-goals/` only when the host has `docs/` and the user explicitly confirms write.

## Anti-patterns

- **Complete every Goal section with bounded autonomy.** Trigger: drafting the final Goal from a vague task. Wrong: publishing with missing sections or vague autonomy like "fix everything". Correct: clarify first, fill all six sections (plus section 7 when parallel), and keep boundaries narrow. Reason: an under-specified Goal lets the agent act far beyond what the user intended.
- **Require helper goals when work is parallel.** Trigger: cross-repo, audit fan-out, explore-then-implement, or explicit subagents. Wrong: a single-agent Goal with no section 7. Correct: add one mini-goal per helper (outcome, verification, boundaries). Reason: parallel work without named helpers collapses into vague autonomy.
- **Define the Goal without executing it.** Trigger: delivering the Goal. Wrong: editing code or running destructive commands in the same turn. Correct: stop at the Goal unless the user explicitly says to skip Goal definition and execute now. Reason: this skill is plan-only, so acting without that explicit consent risks unwanted or irreversible changes.
- **Write docs only after confirmation.** Trigger: host has a `docs/` directory. Wrong: writing `docs/agent-goals/` on Goal delivery alone. Correct: offer the path and write only after the user confirms save. Reason: approving the Goal is not consent to create files.
- **Do not claim a native Goals product feature.** Reason: this is a portable Goal document for Cursor agents, and implying a built-in Goals API would mislead the user.

## Examples

- `/define-agent-goal`
- `/define-agent-goal` with "reduce flaky tests in service-a"
- `/define-agent-goal` with a filled intake block:

```markdown
**Task:** Reduce flaky integration tests in service-a
**Context:** `service-a/spec/integration/`, CI job `integration`
**Constraints:** No production deploys; keep existing test intent
**Definition of done:** Flake rate under 1% over 10 CI runs; no deleted coverage without replacement
```

- `/define-agent-goal` with a parallel task (e.g. "audit feature flags across repo1, repo2, and repo3"); expect section 7 with one mini-goal per repo/helper

## Maintainers

Behavioral eval: `.cursor/skill-contracts/define-agent-goal/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
