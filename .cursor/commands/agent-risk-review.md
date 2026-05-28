---
name: agent-risk-review
version: 1
description: One-page agent permission brief before granting access to a system, tool, or account
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/agent-risk-review/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Produce a one-page agent permission brief before granting an AI agent access to a system, tool, or account. Full workflow: `.cursor/skills/agent-risk-review/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/agent-risk-review/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake → Discovery → Draft → Clarify gate → Deliver); do not skip the clarify-before-finalize gate.
3. **Report** the final seven-section brief in chat; offer optional save under `docs/agent-permissions/<slug>.md` when the host has `docs/`.

## Anti-patterns

- Do not recommend blanket admin or full write access without explicit limits
- Do not finalize the brief while any permission tier is ambiguous
- Do not confuse this with codebase `security-audit`
- Do not instruct logging of secrets, tokens, PII, or PHI

## Examples

- `/agent-risk-review` with "GitHub org token for merge bot"
- `/agent-risk-review` with "AWS prod read-only for incident agent"

## Maintainers

Behavioral eval: `.cursor/skills/agent-risk-review/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
