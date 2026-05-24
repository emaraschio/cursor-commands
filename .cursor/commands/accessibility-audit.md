---
name: accessibility-audit
version: 1
description: Audit UI for WCAG accessibility issues and fixes
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/accessibility-audit/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Audit UI for WCAG accessibility issues and fixes. Full workflow: `.cursor/skills/accessibility-audit/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/accessibility-audit/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Fix only a11y issues; do not refactor unrelated code
- Do not skip keyboard/screen reader checks

## Examples

- `/accessibility-audit`
- `/accessibility-audit on checkout form`

## Maintainers

Behavioral eval: `.cursor/skills/accessibility-audit/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
