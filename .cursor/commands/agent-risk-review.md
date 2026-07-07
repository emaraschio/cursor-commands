---
name: agent-risk-review
version: 2
description: One-page agent permission brief before granting access to a system, tool, or account
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/agent-risk-review/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Produce a one-page agent permission brief before granting an AI agent access to a system, tool, or account. Full workflow: `.cursor/skill-contracts/agent-risk-review/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/agent-risk-review/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake → Discovery → Draft → Clarify gate → Deliver); do not skip the clarify-before-finalize gate.
3. **Report** the final seven-section brief in chat; offer optional save under `docs/agent-permissions/<slug>.md` when the host has `docs/`.

## Anti-patterns

- **Default to least privilege, never blanket access.** Trigger: drafting the allowed-actions tier. Wrong: granting full admin or broad write access without explicit limits. Correct: scope each grant to least privilege and require documented limits for anything destructive. Reason: an over-permissioned agent turns a small mistake into a production-wide one.
- **Resolve ambiguity before finalizing.** Trigger: a permission tier, limit, or log destination is unclear. Wrong: publishing the final brief on guessed or maximal defaults. Correct: stop at the clarify gate and ask before finalizing. Reason: a brief shipped on assumptions authorizes access no one actually reviewed.
- **Never route secrets into logs.** Trigger: specifying the required-logs section. Wrong: logging tokens, credentials, PII, or PHI in plain text. Correct: place them under must-not-log and never-allowed. Reason: logs are retained and broadly readable, so a logged secret is a leaked secret.

## Examples

- `/agent-risk-review` with "GitHub org token for merge bot"
- `/agent-risk-review` with "AWS prod read-only for incident agent"

## Maintainers

Behavioral eval: `.cursor/skill-contracts/agent-risk-review/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
