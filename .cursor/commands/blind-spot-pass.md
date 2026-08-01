---
name: blind-spot-pass
version: 3
description: Run a pre-build blind spot pass; four quadrants with deps/edge/blast under unknown unknowns, high-leverage questions, two-step halt; red-team only on request; plan-only
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/blind-spot-pass/eval/cases.md
  ship_gate: [A, S, R]
---

## Overview

Before building, run a blind spot pass on the user's rough plan. Treat the prompt as the map and the real project as the territory: classify gaps across four knowledge quadrants (with Dependencies, Edge cases, and Blast radius under unknown unknowns), ask 5 to 10 high-leverage interview questions, and halt with a two-step handshake before building. Default intensity is **standard**; **red-team** only when the user asks to challenge or break the plan. Plan-only on delivery and on pass approval. Full workflow: `.cursor/skill-contracts/blind-spot-pass/SKILL.md` (user install: `~/.cursor/skill-contracts/blind-spot-pass/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Deliverable | Five-section pass in chat (four quadrants + interview questions; §4 has required sub-bullets) |
| Intensity | **standard** always; **red-team** only if user asks to challenge / break / red-team |
| Handshake | Approve or edit the pass, then later **execute now**; pass approval is not build |
| Execution | None in same turn unless explicit skip-the-pass-and-build |
| Question count | 5 to 10, ranked by leverage on structure, architecture, audience, scope, workflow, quality |
| Persistence | Offer save under `docs/blind-spot-passes/`; write only after user confirms |
| Examples | Generic names only (`product-a`, `service-a`, `repo1`) |

## Steps

1. **Read** `.cursor/skill-contracts/blind-spot-pass/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/blind-spot-pass/SKILL.md`.
2. **Execute** phases in order (Intake → Discovery → Draft the pass → Deliver); do not skip discovery or start building.
3. **Report** the blind spot pass (sections 1 to 5) with §4 sub-bullets and the two-step approval handshake.
4. **Offer** optional save under `docs/blind-spot-passes/` when the host has `docs/`; write only after the user confirms.

## Anti-patterns

- **Classify all four quadrants.** Trigger: drafting the pass from a rough plan. Wrong: skipping unknown knowns or unknown unknowns, or collapsing quadrants into a single list. Correct: populate every quadrant explicitly, marking thin quadrants when the context is sparse. Reason: the pass exists to surface what the prompt omitted, and skipped quadrants hide unstated assumptions.
- **Require §4 Dependencies, Edge cases, and Blast radius.** Trigger: writing unknown unknowns. Wrong: a mushy risk paragraph with no sub-bullets. Correct: include all three sub-bullets, or mark **N/A** when genuinely empty; do not invent facts. Reason: vague §4 lets the model skip failure modes the pass is meant to surface.
- **Ask high-leverage questions, not trivia.** Trigger: producing the interview questions. Wrong: listing shallow yes/no questions that would not change the output. Correct: ask 5 to 10 questions ranked by leverage on structure, architecture, audience, scope, workflow, or quality. Reason: low-leverage questions waste the interview gate before building.
- **Stay a blind spot pass.** Trigger: user did not ask to challenge or break the plan, or pastes a step-by-step implementation plan for technical audit. Wrong: defaulting to a hostile free-form risk report, or replacing the four quadrants with a principal-engineer plan audit. Correct: use **standard** unless they ask for red-team / challenge / break; stay map/territory and point them at a dedicated plan-preflight skill, not this one. Reason: this skill audits the ask, not a finished build plan; unsolicited red-team burns tokens.
- **Two-step handshake: pass approval is not build.** Trigger: user says "approved" or "LGTM" on the pass. Wrong: scaffolding or coding in that turn. Correct: acknowledge and wait for a later **execute now** (unless they explicitly skip the pass and build now). Reason: conflating review with build defeats the gate.
- **Implementation notes after execute now.** Trigger: follow-up build after **execute now**. Wrong: silent assumptions during the follow-up build. Correct: maintain an Implementation notes section logging each material assumption (what, why, and what would change if wrong). Reason: unlogged assumptions recreate the blind spots the pass was meant to surface.
- **Docs save only after confirm.** Trigger: host has a `docs/` directory and the pass is ready. Wrong: writing `docs/blind-spot-passes/...` unprompted. Correct: offer the path and write only after the user confirms. Reason: unsolicited docs clutter the host workspace.
- **Do not claim a native product feature.** Trigger: describing what this deliverable is. Wrong: implying a built-in Cursor product feature. Correct: present this as a portable planning document for Cursor agents. Reason: a native-product claim misleads the user about what shipped.

## Examples

- `/blind-spot-pass` with a rough plan to build a landing page for product-a
- `/blind-spot-pass` before `/requirement-to-implementation` on a feature sketch
- `/blind-spot-pass` with "red-team this plan" or "challenge why this ask might fail"
- After pass delivery, user says "approved" → acknowledge and wait; user later says "execute now" → begin the build

## Maintainers

Behavioral eval: `.cursor/skill-contracts/blind-spot-pass/eval/cases.md`. Ship gate sections: **A, S, R** before changing `SKILL.md` or this command.
