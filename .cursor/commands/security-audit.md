---
name: security-audit
version: 2
description: Security audit of codebase or change
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/security-audit/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Security audit of codebase or change. Full workflow: `.cursor/skill-contracts/security-audit/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/security-audit/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Triage dependency CVEs, never ignore them.** Trigger: the dependency audit surfaces a known CVE. Wrong: noting the version and moving on. Correct: assess severity and whether the path is reachable, then flag or patch the affected dependency. Reason: an unhandled known CVE is exactly the exploit route an audit exists to close.
- **Keep live secrets out of findings.** Trigger: the scan turns up a real credential, token, or key. Wrong: pasting the live value into the report to evidence the finding. Correct: redact the value and cite only its location. Reason: an audit report circulates widely, so a pasted secret leaks it further.
- **Do not run write or destructive operations without explicit consent.** Reason: an audit is read-first, so commits, merges, pushes, or production scripts run without an explicit request are hard to undo.

## Examples

- `/security-audit`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/security-audit/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
