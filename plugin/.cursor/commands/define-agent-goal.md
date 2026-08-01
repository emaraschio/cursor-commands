---
name: define-agent-goal
version: 5
description: Turn a rough task into an agent Goal (six core sections, 3 to 5 success criteria, helper goals when parallel, two-step approval); plan-only, no execution in the same turn
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/define-agent-goal/eval/cases.md
  ship_gate: [A, S, R]
---

## Overview

Define an agent Goal using **human-reviewed autonomy** and a **two-step handshake**: draft the Goal and wait for Goal approval; execute only after a later explicit **execute now**. Plan-only on delivery and on Goal approval. Full workflow: `.cursor/skill-contracts/define-agent-goal/SKILL.md` (user install: `~/.cursor/skill-contracts/define-agent-goal/SKILL.md`). End-user notes: `.cursor/skill-contracts/define-agent-goal/reference.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Deliverable | Goal in chat (sections 1 to 6; section 7 when parallel work is implied) |
| Success criteria | 3 to 5 checkboxes under Verification |
| Handshake | Approve Goal, then later **execute now**; Goal approval is not execute |
| Discovery | Fast path when full intake template is provided and unambiguous |
| Persistence | Always auto-write to `<host-repo-root>/agent-goals/<kebab-slug>.md` (gitignored); never `docs/agent-goals/` |
| Examples | Generic names only (`service-a`, `repo1`) |

## Steps

1. **Read** `.cursor/skill-contracts/define-agent-goal/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/define-agent-goal/SKILL.md`.
2. **Execute** phases in order (Intake → Discovery [or fast path] → Draft → Clarify gate → Deliver); do not skip the clarify gate or start executing the task.
3. **Report** the final Goal with 3 to 5 success criteria, two-step approval handshake, copyable intake template, and section 7 helper goals when parallelism applies (each with iteration and stopping).
4. **Auto-write** under `<host-repo-root>/agent-goals/<kebab-slug>.md` (ensure `/agent-goals/` is gitignored); never use `docs/agent-goals/`.

## Anti-patterns

- **Clarify gate before publish.** Trigger: outcome, verification, stopping condition, or boundaries are ambiguous. Wrong: publishing a Goal with guessed or TBD outcome/verification/stopping/boundaries. Correct: stop at the Clarify gate and ask before finalizing. Reason: a Goal shipped on assumptions authorizes work no one reviewed.
- **3 to 5 success criteria.** Trigger: drafting section 2 Verification. Wrong: fewer than 3 or more than 5 checkboxes. Correct: include 3 to 5 success criteria as scannable, testable checkboxes. Reason: too few criteria leave done-ness vague; too many bury the signal.
- **Complete every Goal section with bounded autonomy.** Trigger: drafting the final Goal from a vague task. Wrong: publishing with missing sections or vague autonomy like "fix everything". Correct: clarify first, fill all six sections (plus section 7 when parallel), and keep boundaries narrow. Reason: an under-specified Goal lets the agent act far beyond what the user intended.
- **Require helper goals when work is parallel.** Trigger: cross-repo, audit fan-out, explore-then-implement, or explicit subagents. Wrong: a single-agent Goal with no section 7, or mini-goals missing iteration/stopping. Correct: add one mini-goal per helper with outcome, verification, boundaries, iteration policy, and stopping condition (inherit parent when identical). Reason: parallel work without named helpers collapses into vague autonomy.
- **Do not invent section 7 for single-agent work.** Trigger: one repo, one surface, no fan-out. Wrong: padding the Goal with unused helpers. Correct: omit section 7. Reason: false-positive parallelism wastes tokens and muddies ownership.
- **Two-step handshake: Goal approval is not execute.** Trigger: finishing Goal delivery, or user says "approved" or "LGTM" on the Goal. Wrong: editing code, running destructive commands, or starting the underlying task in that turn. Correct: deliver the Goal and stop; acknowledge approval and wait for a later **execute now** (unless they explicitly skip Goal definition and order execution). Reason: this skill defines the Goal; conflating review with run causes unwanted changes.
- **Save: always auto-write to root `agent-goals/` (gitignored).** Trigger: Goal delivery. Wrong: writing under `docs/agent-goals/` or committing Goals. Correct: `<host-repo-root>/agent-goals/<kebab-slug>.md` with `/agent-goals/` in `.gitignore`. Reason: Goals are local working notes; `docs/` paths get tracked and fight that intent.
- **Do not claim a native Goals product feature.** Trigger: describing what this deliverable is. Wrong: implying a built-in Goals API or product feature. Correct: present this as a portable Goal document for Cursor agents. Reason: a native-product claim misleads the user about what shipped.
- **Prefer the intake fast path.** Trigger: all four intake fields are present and unambiguous. Wrong: re-asking obvious duplicate questions. Correct: skip redundant discovery and draft the Goal. Reason: redundant interviews burn tokens when the user already supplied the inputs.

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

- `/define-agent-goal` with a parallel task (e.g. "audit feature flags across repo1, repo2, and repo3"); expect section 7 with rich mini-goals per repo/helper
- After Goal delivery, user says "approved" → acknowledge and wait; user later says "execute now" → begin the task

## Maintainers

Behavioral eval: `.cursor/skill-contracts/define-agent-goal/eval/cases.md`. Ship gate sections: **A, S, R** before changing `SKILL.md` or this command.
