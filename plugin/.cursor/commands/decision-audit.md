---
name: decision-audit
version: 1
description: Post-build decision ledger and pride gate; audit meaningful choices without changing code until revise
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/decision-audit/eval/cases.md
  ship_gate: [A, S]
---

## Overview

After work has landed (or a scoped branch/session), list meaningful agent decisions and assumptions, surface why / alternatives / confidence, flag debt and edge cases, and ask the pride gate. Audit only; no code changes until the user says revise now. Full workflow: `.cursor/skill-contracts/decision-audit/SKILL.md` (user install: `~/.cursor/skill-contracts/decision-audit/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Scope | Full session or current branch unless user narrows |
| Evidence | Conversation + read-only git (`status`, `diff`, `log`) when repo present |
| Intensity | Standard (single mode; no red-team variant in v1) |
| Execution | Audit only; no edits, commits, or destructive commands in the same turn |
| Examples | Generic names only (`service-a`, `branch-1`) |

## Steps

1. **Read** `.cursor/skill-contracts/decision-audit/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/decision-audit/SKILL.md`.
2. **Execute** phases in order (Intake → Evidence → Ledger → Debt and edges → Pride gate → Halt).
3. **Report** the decision ledger, debt/edge notes, pride gate, and halt line; do not revise code in the same turn.

## Anti-patterns

- **Ledger of choices, not a line-by-line review.** Trigger: auditing after a build. Wrong: dumping a file-by-file code review without naming decisions. Correct: list meaningful choices (architecture, API shape, libraries, deferred work) with why, alternatives, and confidence. Reason: the job is judgment autopsy, not another diff scavenger hunt.
- **Stay audit-only until revise now.** Trigger: finishing the ledger or pride gate. Wrong: editing code, committing, or opening a PR in the same turn. Correct: deliver the audit and wait for an explicit **revise now** (with targets). Reason: ledger approval is not permission to mutate the branch.
- **Ground decisions in evidence.** Trigger: filling the ledger. Wrong: inventing choices that have no support in conversation or diff. Correct: cite session or git evidence, or mark confidence low / none recorded. Reason: invented decisions fake accountability.
- **Always ask the pride gate.** Trigger: closing the audit. Wrong: soft-selling ship readiness or skipping the two yes/no questions. Correct: ask whether the human is proud of the branch and would stand behind it in production. Reason: the pride gate is the cheap, high-signal filter this skill exists to force.

## Examples

- `/decision-audit` after a coding session with landed changes
- `/decision-audit` for "the auth refactor on branch-1" (scoped ledger)
- `/decision-audit` mid-task with nothing landed yet (expect stop or ask to wait)

## Maintainers

Behavioral eval: `.cursor/skill-contracts/decision-audit/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
