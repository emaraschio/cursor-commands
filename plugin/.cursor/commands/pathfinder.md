---
name: pathfinder
version: 2
description: Map the fog of war before building; separate fixed decisions from open frontiers and unknowns, tag each unknown with a next move, and lay out parallel tracks; plan-only, no execution in the same turn
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/pathfinder/eval/cases.md
  ship_gate: [A, S, R]
---

## Overview

Map a project's uncertainty before building. Given a goal and known context, produce a six-section fog map: decisions already fixed, decision frontiers, fog-of-war questions, a next move per unknown, a parallel work plan, and the next three actions. Plan-only. Does not execute the project in the same turn. Full workflow: `.cursor/skill-contracts/pathfinder/SKILL.md` (user install: `~/.cursor/skill-contracts/pathfinder/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Deliverable | Six-section fog map in chat |
| Execution | None in same turn (follow-up track, or `define-agent-goal`) |
| Ambiguity | Clarify the goal and separate fixed from unknown before drafting |
| Next-move labels | research, prototype, ask an expert, user test, delegate |
| Examples | Generic names only (`service-a`, `repo1`) |

## Steps

1. **Read** `.cursor/skill-contracts/pathfinder/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/pathfinder/SKILL.md`.
2. **Execute** phases in order (Intake -> Discovery -> Draft the map -> Deliver); do not skip discovery or start building the project.
3. **Report** the fog map (sections 1 to 6); offer optional save under `docs/decision-maps/` when the host has `docs/`.

## Anti-patterns

- **Separate fixed from unknown.** Trigger: drafting the "decisions already fixed" section. Wrong: listing an assumption as a settled decision. Correct: mark a decision fixed only when the context states it; An assumption is not a fixed decision, so keep assumptions in frontiers or fog. Reason: false certainty hides the real risk and sends the project building on ground that was never solid.
- **Tag every unknown with a next move.** Trigger: listing fog-of-war questions. Wrong: leaving an unknown with no resolution path. Correct: label each unknown with exactly one next move (research, prototype, ask an expert, user test, or delegate). Reason: an unknown with no next move never gets resolved and resurfaces mid-build.
- **Deliver the map without building it.** Trigger: finishing the map for a project whose next step looks obvious. Wrong: scaffolding code or running destructive commands in the same turn. Correct: stop at the map (plan-only) unless the user explicitly says to skip planning and build now. Reason: this skill is plan-only, and building on unmapped fog is exactly the failure it exists to prevent.
- **Parallel tracks and three actions.** Trigger: filling the parallel work plan and next-actions sections. Wrong: a single-thread plan or vague next steps. Correct: 3 to 5 parallel tracks plus exactly three concrete actions today. Reason: a map without parallelizable work and concrete next steps fails to unlock progress.
- **Docs save only after confirm.** Trigger: host has a `docs/` directory and the map is ready. Wrong: writing `docs/decision-maps/...` unprompted. Correct: offer the path and write only after the user confirms. Reason: unsolicited docs clutter the host workspace.
- **Do not claim a native product feature.** Trigger: describing what this deliverable is. Wrong: implying a built-in Cursor product feature. Correct: present this as a portable planning document for Cursor agents. Reason: a native-product claim misleads the user about what shipped.

## Examples

- `/pathfinder` with a greenfield project goal and a paste of requirements
- `/pathfinder` with "rebuild the billing flow" and a few known constraints

## Maintainers

Behavioral eval: `.cursor/skill-contracts/pathfinder/eval/cases.md`. Ship gate sections: **A, S, R** before changing `SKILL.md` or this command.
