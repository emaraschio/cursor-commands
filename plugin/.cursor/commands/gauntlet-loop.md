---
name: gauntlet-loop
version: 2
description: Beat a real-world quality bar via builder/critic loops; critics alone decide when each part passes
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/gauntlet-loop/eval/cases.md
  ship_gate: [A, S, R]
---

## Overview

Run a Gauntlet Loop: take a GOAL and a REAL-WORLD EQUIVALENT as the quality bar, decompose into independent parts, and run each part through a build → critique → pass|iterate|terminal loop. Critics use fresh context, inspect the artifact, and compare against the reference (blind side-by-side when possible). A part passes only when better than the reference (equal fails); otherwise the critic returns the largest specific gap. Builders never evaluate their own work. Full workflow: `.cursor/skill-contracts/gauntlet-loop/SKILL.md` (user install: `~/.cursor/skill-contracts/gauntlet-loop/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Intake | GOAL and REAL-WORLD EQUIVALENT required; inaccessible reference blocks |
| Iteration cap | 5 rounds per part (overridable at intake) |
| Stall | Same gap twice with no improvement; halt that part |
| Critic mode | Subagent when available; else fresh-context simulation (report which) |
| Blind comparison | Prefer side-by-side without labeling which is the reference |
| Part list | Publish then proceed unless the user objects |
| Examples | Generic names only (`project-a`, `game-1`) |

## Steps

1. **Read** `.cursor/skill-contracts/gauntlet-loop/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/gauntlet-loop/SKILL.md`.
2. **Execute** phases in order (Intake → Decompose → Per-part loop → Deliver).
3. **Report** the part table (rounds, verdicts, remaining gaps, critic mode per part) and halt on stalled or capped parts; do not claim a pass without a critic verdict after artifact inspection.

## Anti-patterns

- **GOAL and REAL-WORLD EQUIVALENT required.** Trigger: starting without a clear goal or reference. Wrong: inventing a quality bar or proceeding with a vague "make it better". Correct: ask one focused question per missing field; never invent the reference. Reason: without a real equivalent there is no gauntlet, only vibes.
- **Do not let builders evaluate their own work.** Trigger: a builder finishes a part. Wrong: the same agent context grades its own output as pass. Correct: hand the artifact to a separate critic with fresh context. Reason: self-review collapses the loop into confirmation bias.
- **Critic uses fresh context.** Trigger: assigning critique. Wrong: critic sees the full build transcript and rationalizations. Correct: give the critic only the artifact, the reference (or both unlabeled), and the part bar. Reason: build history contaminates comparison.
- **Pass only if better than the reference.** Trigger: critic returns a verdict. Wrong: passing on "good enough", "close", or equal quality. Correct: pass only when better than the REAL-WORLD EQUIVALENT; equal or worse returns the largest specific gap. Reason: the bar is beat-the-example, not polish-until-tired.
- **Largest specific gap, not vague feedback.** Trigger: critic finds the generated work inferior or equal. Wrong: "improve polish" or "make it better". Correct: name the single largest concrete gap versus the reference. Reason: vague feedback wastes the next builder round.
- **Blind side-by-side when possible.** Trigger: comparing artifact and reference. Wrong: telling the critic which item is generated when unlabeled comparison is feasible, or claiming blind when labeled. Correct: present them side by side without labels when possible; if not, state the comparison was not blind. Reason: labeled comparison biases the critic toward the known reference.
- **Cap and stall, never infinite loop.** Trigger: a part keeps failing critique. Wrong: looping forever on the same gap. Correct: stop at the iteration cap (default 5) or when the same gap repeats twice with no improvement; report and halt that part. Reason: unbounded loops burn tokens without raising quality.
- **Do not skip the critic.** Trigger: user says "just ship" or "looks fine" after a build. Wrong: skipping critique or letting the builder self-pass. Correct: still run a fresh-context critic before any pass. Reason: skipping critique deletes the gauntlet.
- **Inaccessible reference blocks intake.** Trigger: reference named but unreachable (dead link, missing file). Wrong: inventing a substitute bar or proceeding from vague memory. Correct: stop and ask how to obtain an inspectable reference. Reason: a gauntlet without an inspectable bar is theater.

## Examples

- `/gauntlet-loop` with GOAL "ship a playable racer for game-1" and REAL-WORLD EQUIVALENT "classic kart racer feel"
- `/gauntlet-loop` when GOAL is present but the reference is missing (expect a question before decompose)
- `/gauntlet-loop` with an explicit iteration cap of 3 for a scoped UI part on project-a
- `/gauntlet-loop` when the reference URL is dead (expect inaccessible-reference stop)

## Maintainers

Behavioral eval: `.cursor/skill-contracts/gauntlet-loop/eval/cases.md`. Ship gate sections: **A, S, R** before changing `SKILL.md` or this command.
