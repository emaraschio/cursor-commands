---
name: seo-audit
version: 1
description: SEO audit of pages or app
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/seo-audit/eval/cases.md
  ship_gate: [A]
---

## Overview

SEO audit of pages or app. Full workflow: `.cursor/skills/seo-audit/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/seo-audit/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- Do not recommend black-hat tactics
- Ground recommendations in measurable checks

## Examples

- `/seo-audit`

## Maintainers

Behavioral eval: `.cursor/skills/seo-audit/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
