---
name: pathfinder
version: 1
description: Map the fog of war before building; separate fixed decisions from open frontiers and unknowns, tag each unknown with a next move, and lay out parallel tracks; plan-only, no execution in the same turn
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/pathfinder/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Map a project's uncertainty before building. Given a goal and known context, produce a six-section fog map: decisions already fixed, decision frontiers, fog-of-war questions, a next move per unknown, a parallel work plan, and the next three actions. Plan-only. Does not execute the project in the same turn. Full workflow: `.cursor/skills/pathfinder/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Deliverable | Six-section fog map in chat |
| Execution | None in same turn (follow-up track, or `define-agent-goal`) |
| Ambiguity | Clarify the goal and separate fixed from unknown before drafting |
| Next-move labels | research, prototype, ask an expert, user test, delegate |
| Examples | Generic names only (`service-a`, `repo1`) |

## Steps

1. **Read** `.cursor/skills/pathfinder/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake -> Discovery -> Draft the map -> Deliver); do not skip discovery or start building the project.
3. **Report** the fog map (sections 1 to 6); offer optional save under `docs/decision-maps/` when the host has `docs/`.

## Anti-patterns

- **Separate fixed from unknown.** Trigger: drafting the "decisions already fixed" section. Wrong: listing an assumption as a settled decision. Correct: mark a decision fixed only when the context states it, and keep assumptions in frontiers or fog. Reason: false certainty hides the real risk and sends the project building on ground that was never solid.
- **Tag every unknown with a next move.** Trigger: listing fog-of-war questions. Wrong: leaving an unknown with no resolution path. Correct: label each unknown with exactly one next move (research, prototype, ask an expert, user test, or delegate). Reason: an unknown with no next move never gets resolved and resurfaces mid-build.
- **Deliver the map without building it.** Trigger: finishing the map for a project whose next step looks obvious. Wrong: scaffolding code or running destructive commands in the same turn. Correct: stop at the map unless the user explicitly says to skip planning and build now. Reason: this skill is plan-only, and building on unmapped fog is exactly the failure it exists to prevent.
- **Do not claim a native product feature.** Reason: this is a portable planning document for Cursor agents, and implying a built-in feature would mislead the user.

## Examples

- `/pathfinder` with a greenfield project goal and a paste of requirements
- `/pathfinder` with "rebuild the billing flow" and a few known constraints

## Maintainers

Behavioral eval: `.cursor/skills/pathfinder/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
