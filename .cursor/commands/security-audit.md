---
name: security-audit
version: 1
description: Security audit of codebase or change
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/security-audit/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Security audit of codebase or change. Full workflow: `.cursor/skills/security-audit/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/security-audit/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not ignore dependency CVEs
- Do not expose findings with live secrets

## Examples

- `/security-audit`

## Maintainers

Behavioral eval: `.cursor/skills/security-audit/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
