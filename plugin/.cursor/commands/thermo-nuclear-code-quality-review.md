---
name: thermo-nuclear-code-quality-review
version: 1
description: Extremely strict maintainability review hunting for code-judo simplifications, giant files, and spaghetti-condition growth
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/thermo-nuclear-code-quality-review/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Extremely strict maintainability review that hunts for code-judo simplifications, giant files, and spaghetti-condition growth without changing behavior. Full workflow: `.cursor/skill-contracts/thermo-nuclear-code-quality-review/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Scope | current branch diff against its merge base |
| Posture | block on structural regressions; keep behavior identical |
| Findings | a few high-conviction comments over a long list of nits |
| Invocation | explicit only (do not auto-suggest) |
| Ship gate | A, S |

## Steps

1. **Read** `.cursor/skill-contracts/thermo-nuclear-code-quality-review/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Push for the code judo move, not surface polish.** Trigger: a diff that works but carries avoidable structural complexity. Wrong: approving it or leaving only rename and style nits. Correct: name the code judo move that deletes whole branches or layers and push for it. Reason: a review that only polishes lets incidental complexity calcify into permanent debt.
- **Block unjustified file-size and spaghetti growth.** Trigger: a diff pushing a file past 1000 lines or bolting ad-hoc conditionals onto an unrelated flow. Wrong: accepting it because the tests pass. Correct: ask to decompose first and move the logic behind a dedicated abstraction. Reason: sprawl and scattered special cases make the surrounding code permanently harder to reason about.

## Examples

- `/thermo-nuclear-code-quality-review`
- `/thermo-nuclear-code-quality-review` scoped to a single file or module

## Maintainers

Behavioral eval: `.cursor/skill-contracts/thermo-nuclear-code-quality-review/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
