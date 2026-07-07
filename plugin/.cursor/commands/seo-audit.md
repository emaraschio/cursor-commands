---
name: seo-audit
version: 2
description: SEO audit of pages or app
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/seo-audit/eval/cases.md
  ship_gate: [A]
---

## Overview

SEO audit of pages or app. Full workflow: `.cursor/skill-contracts/seo-audit/SKILL.md` (user install: `~/.cursor/skill-contracts/seo-audit/SKILL.md`).

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/seo-audit/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/seo-audit/SKILL.md`.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Recommend only legitimate tactics.** Trigger: proposing SEO improvements. Wrong: suggesting black-hat tactics such as cloaking, link schemes, or keyword stuffing. Correct: recommend only white-hat, guideline-compliant tactics. Reason: black-hat tactics risk search penalties that drop the site from results.
- **Ground findings in measurable checks.** Trigger: reporting audit findings. Wrong: asserting issues from intuition without evidence. Correct: base each finding on a measurable check or observed metric; measure first. Reason: unmeasured claims send teams chasing non-issues.

## Examples

- `/seo-audit`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/seo-audit/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
