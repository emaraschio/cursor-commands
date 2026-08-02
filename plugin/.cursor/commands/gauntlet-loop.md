---
name: gauntlet-loop
version: 3
description: Beat a real-world quality bar via builder/critic loops; critics alone decide when each part passes
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/gauntlet-loop/eval/cases.md
  ship_gate: [A, S, R]
---

## Overview

Run a Gauntlet Loop: take a GOAL and a REAL-WORLD EQUIVALENT with an inspectable reference pack, decompose into independent parts, and run each part through a build → critique → pass|iterate|terminal loop. After all parts pass, run an integration critic on the whole. Optional BUDGET ceiling, taste-domain pride gate, and gap ledger for resume. Critics use fresh context, inspect the artifact, and compare against the pack (blind when possible). A part passes only when better than the reference (equal fails); otherwise the critic returns the largest specific gap. Builders never evaluate their own work. Full workflow: `.cursor/skill-contracts/gauntlet-loop/SKILL.md` (user install: `~/.cursor/skill-contracts/gauntlet-loop/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Intake | GOAL, REAL-WORLD EQUIVALENT, and inspectable reference pack required |
| Iteration cap | 5 rounds per part (overridable at intake) |
| BUDGET | None beyond per-part cap (optional total rounds / wall-clock) |
| Stall | Same gap twice with no improvement; halt that part |
| Critic mode | Subagent when available; else fresh-context simulation (report which) |
| Blind comparison | Prefer side-by-side without labeling which is the reference |
| Integration critic | Required after all parts pass before done |
| Pride gate | Taste domains only (UI, game feel, writing); else "not a taste domain" |
| Gap ledger | Record round/gap/verdict; consult on resume |
| Part list | Publish then proceed unless the user objects |
| Examples | Generic names only (`project-a`, `game-1`) |

## Steps

1. **Read** `.cursor/skill-contracts/gauntlet-loop/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/gauntlet-loop/SKILL.md`.
2. **Execute** phases in order (Intake → Decompose → Per-part loop → Integration critic → Deliver).
3. **Report** the part table, integration verdict, gap ledger, pride gate (or not a taste domain), and halt on stalled, capped, or budgeted parts; do not claim done from part-local passes alone.

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
- **Reference pack required.** Trigger: reference named as a famous product with no files, screenshots, clip, build, or repo path. Wrong: grading from memory of that product. Correct: assemble an inspectable reference pack or block intake. Reason: critics need something to open, not folklore.
- **Integration critic before done.** Trigger: every part has a local pass. Wrong: declaring the gauntlet done without a whole-artifact critique. Correct: run an integration critic on the assembled artifact versus the whole reference pack. Reason: local wins can still lose the whole.
- **Budget ceiling stops the loop.** Trigger: BUDGET (total rounds or wall-clock) is exhausted mid-loop. Wrong: soft-passing remaining parts to finish under budget. Correct: terminal as `fail (budget)`, report, and halt. Reason: inventing a pass to save tokens deletes the quality bar.
- **Pride gate on taste domains.** Trigger: machine (including integration) passes on UI, game feel, or writing. Wrong: shipping without asking if the human is proud versus the reference. Correct: ask the pride gate yes/no before ship; for objective domains state "not a taste domain". Reason: taste is partly subjective; the human is the last critic.
- **Gap ledger for resume.** Trigger: resuming a prior gauntlet session. Wrong: blindly retrying a gap already marked stalled. Correct: read the gap ledger first and change approach or skip that gap. Reason: rediscovering the same stall wastes the next session.

## Examples

- `/gauntlet-loop` with GOAL "ship a playable racer for game-1", REAL-WORLD EQUIVALENT, and a reference pack of screenshots plus a playable build
- `/gauntlet-loop` when GOAL is present but the reference is missing (expect a question before decompose)
- `/gauntlet-loop` with an explicit iteration cap of 3 and BUDGET of 20 total rounds for a scoped UI part on project-a
- `/gauntlet-loop` when the reference URL is dead (expect inaccessible-reference stop)
- `/gauntlet-loop` resume with a prior gap ledger (expect stalled gaps not blindly retried)

## Maintainers

Behavioral eval: `.cursor/skill-contracts/gauntlet-loop/eval/cases.md`. Ship gate sections: **A, S, R** before changing `SKILL.md` or this command.
