---
name: instruction-ablation
version: 2
description: Rebuild a minimal instruction set from a bare baseline on one real task; add instructions only after repeated failures
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/instruction-ablation/eval/cases.md
  ship_gate: [A, S, R]
---

## Overview

Run an ablation rebuild: confirm a bare baseline, execute one real task in-session under guardrails only, log what already works, and propose a new instruction only when the same failure repeats. Retest each proposal; keep it only if verification improves. Do not rewrite rules, skills, or memories until the user says apply now. Full workflow: `.cursor/skill-contracts/instruction-ablation/SKILL.md` (user install: `~/.cursor/skill-contracts/instruction-ablation/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Mode | In-chat bare run |
| Intake | TASK, GUARDRAILS, EXIT CRITERIA, VERIFICATION required |
| Propose instruction | Only after repeated failure (same pattern ≥2 times) |
| Apply to disk | Never without explicit **apply now** and targets |
| Examples | Generic names only (`service-a`, `task-1`) |

## Steps

1. **Read** `.cursor/skill-contracts/instruction-ablation/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/instruction-ablation/SKILL.md`.
2. **Execute** phases in order (Intake → Baseline gate → Bare run → Struggle log → Instruction proposals → Deliver).
3. **Report** baseline status, bare-run outcome, struggle log, proposal ledger, minimal kept set, delete candidates (if stack provided), and halt; do not write rules/skills/memories without **apply now**.

## Anti-patterns

- **Four intake fields required.** Trigger: starting ablation without complete intake. Wrong: inventing missing TASK / GUARDRAILS / EXIT CRITERIA / VERIFICATION or starting the bare run anyway. Correct: ask one focused question per gap. Reason: a bare run without clear exit and verification cannot judge keep/drop.
- **No instruction after a one-off mistake.** Trigger: a single failure during the bare run. Wrong: adding a new rule or skill clause immediately. Correct: log it as one-off unless the same failure pattern repeats (≥2). Reason: one-offs inflate the stack the skill exists to thin.
- **Never claim a bare environment without confirmation.** Trigger: starting the bare run. Wrong: stating hooks, memories, or rules were disabled when the user did not confirm. Correct: ask for clean-chat confirmation or declare contamination. Reason: fake bare baselines make ablation theater.
- **Do not rewrite the stack without apply now.** Trigger: finishing the minimal instruction set. Wrong: editing `rules`, skills, or memories in the same turn. Correct: deliver the report and wait for **apply now** with targets. Reason: ablation recommends; the user owns the stack.
- **Keep/drop requires VERIFICATION.** Trigger: deciding whether a proposed instruction stays. Wrong: keeping it because it "feels better" with no check against EXIT CRITERIA / VERIFICATION. Correct: retest and keep only if verification measurably improves. Reason: untested instructions recreate prompt bloat.
- **Do not skip the bare baseline for a prompt rewrite.** Trigger: user pastes an existing prompt and asks to improve it. Wrong: jumping into `/prompt-eval-debug`-style edits without a bare run. Correct: run ablation from baseline, or route them to `prompt-eval-debug` if they only want to edit a pasted prompt. Reason: different jobs; conflating them skips the evidence rebuild.

## Examples

- `/instruction-ablation` with TASK, GUARDRAILS, EXIT CRITERIA, and VERIFICATION for `task-1` on `service-a`
- `/instruction-ablation` when the user also pastes their current rules/skills for delete-candidate review
- `/instruction-ablation` with missing intake fields (expect questions before the bare run)

## Maintainers

Behavioral eval: `.cursor/skill-contracts/instruction-ablation/eval/cases.md`. Ship gate sections: **A, S, R** before changing `SKILL.md` or this command.
