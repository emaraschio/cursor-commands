---
name: scoped-audit
version: 1
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

- Do not run the full surface before a scoped sample first pass
- Do not report findings that were not verified against the source
- Do not make changes (migrations, edits) until the plan is approved
- Do not spawn unbounded subagents — respect the concurrency cap
- Do not confuse this with single-domain audits (`security-audit`, `seo-audit`, `accessibility-audit`) or single-requirement builds (`requirement-to-implementation`)

## Examples

- `/scoped-audit` with "find every feature flag set to 0% or 100% and flag the stale ones"
- `/scoped-audit` with "inventory all deprecated API call sites across the repo"

## Maintainers

Behavioral eval: `.cursor/skills/scoped-audit/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
