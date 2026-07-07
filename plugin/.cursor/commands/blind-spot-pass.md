---
name: blind-spot-pass
version: 1
description: Run a pre-build blind spot pass; classify knowns and unknowns across four quadrants, ask high-leverage interview questions; plan-only, no execution in the same turn
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/blind-spot-pass/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Before building, run a blind spot pass on the user's rough plan. Treat the prompt as the map and the real project as the territory: classify gaps across four knowledge quadrants, ask 5 to 10 high-leverage interview questions, and stop before building. Plan-only. Does not execute the task in the same turn. Full workflow: `.cursor/skill-contracts/blind-spot-pass/SKILL.md` (user install: `~/.cursor/skill-contracts/blind-spot-pass/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Deliverable | Five-section pass in chat (four quadrants + interview questions) |
| Execution | None in same turn (follow-up build, `define-agent-goal`, or `requirement-to-implementation`) |
| Question count | 5 to 10, ranked by leverage on structure, architecture, audience, scope, workflow, quality |
| Ambiguity | Clarify the plan before classifying quadrants |
| Examples | Generic names only (`product-a`, `service-a`, `repo1`) |

## Steps

1. **Read** `.cursor/skill-contracts/blind-spot-pass/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/blind-spot-pass/SKILL.md`.
2. **Execute** phases in order (Intake → Discovery → Draft the pass → Deliver); do not skip discovery or start building.
3. **Report** the blind spot pass (sections 1 to 5); offer optional save under `docs/blind-spot-passes/` when the host has `docs/`.

## Anti-patterns

- **Classify all four quadrants.** Trigger: drafting the pass from a rough plan. Wrong: skipping unknown knowns or unknown unknowns, or collapsing quadrants into a single list. Correct: populate every quadrant explicitly, marking thin quadrants when the context is sparse. Reason: the pass exists to surface what the prompt omitted, and skipped quadrants hide unstated assumptions.
- **Ask high-leverage questions, not trivia.** Trigger: producing the interview questions. Wrong: listing shallow yes/no questions that would not change the output. Correct: ask 5 to 10 questions ranked by how much the answer would change structure, architecture, audience, scope, workflow, or quality. Reason: low-leverage questions waste the interview gate before building.
- **Pass before build.** Trigger: finishing the pass on a plan whose next step looks obvious. Wrong: editing code, scaffolding, or running destructive commands in the same turn. Correct: stop at the interview questions unless the user explicitly says to skip the pass and build now. Reason: building on unexamined assumptions defeats the technique.
- **Do not claim a native product feature.** Reason: this is a portable planning document for Cursor agents, and implying a built-in feature would mislead the user.

## Examples

- `/blind-spot-pass` with a rough plan to build a landing page for product-a
- `/blind-spot-pass` before `/requirement-to-implementation` on a feature sketch

## Maintainers

Behavioral eval: `.cursor/skill-contracts/blind-spot-pass/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
