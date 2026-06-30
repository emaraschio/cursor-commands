---
name: scoped-audit
version: 2
description: Scoped, plan-first parallel audit of a large surface using capped subagents, with verification before reporting and an approval gate before any change
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/scoped-audit/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Run a large "check-N-things" task (audit, inventory, or migration) as a scoped, plan-first workflow: decompose the surface, fan out capped parallel subagents, verify findings before reporting, and make changes only after explicit approval. Full workflow: `.cursor/skills/scoped-audit/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| First pass | Scoped sample only (never the full surface) |
| Concurrent subagents | Capped (≤ 6) |
| Changes | None until the plan is approved |

## Steps

1. **Read** `.cursor/skills/scoped-audit/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Scope → Plan → Approval gate → Scoped sample → Parallel fan-out → Verify → Report → optional gated changes); do not skip the approval gate or the verification step.
3. **Report** the catalog of verified findings; propose changes separately and wait for approval before editing.

## Anti-patterns

- **Sample before you fan out.** Trigger: starting a large check-N-things pass. Wrong: running the full surface before the approach is validated. Correct: run a scoped sample first to confirm the finding shape and verification method. Reason: an unvalidated full run across a large surface burns tokens and compounds mistakes.
- **Verify findings before reporting.** Trigger: assembling the catalog from subagent results. Wrong: reporting a subagent summary as fact without rechecking. Correct: re-check each finding against the source and flag what cannot be confirmed. Reason: large parallel passes are where agents hallucinate, so an unverified catalog is worse than none.
- **Make no changes until the plan is approved.** Trigger: the user asks to audit and fix in one pass. Wrong: editing or migrating across the surface before approval. Correct: present proposed changes separately and wait for an explicit approval gate. Reason: bulk edits before review are hard to unwind across a large surface.

## Examples

- `/scoped-audit` with "find every feature flag set to 0% or 100% and flag the stale ones"
- `/scoped-audit` with "inventory all deprecated API call sites across the repo"

## Maintainers

Behavioral eval: `.cursor/skills/scoped-audit/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
