---
name: accessibility-audit
version: 2
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

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/accessibility-audit/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Fix only accessibility issues.** Trigger: spotting unrelated code smells during the audit. Wrong: refactoring unrelated code in the same pass. Correct: change only accessibility issues and note unrelated findings separately. Reason: mixed diffs hide the a11y fix and are hard to review.
- **Do not skip keyboard and screen reader checks.** Trigger: running the audit. Wrong: relying only on automated tooling and skipping manual checks. Correct: verify keyboard navigation and screen reader behavior, not just automated scans. Reason: automated tools miss many real accessibility barriers.

## Examples

- `/accessibility-audit`
- `/accessibility-audit on checkout form`

## Maintainers

Behavioral eval: `.cursor/skills/accessibility-audit/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
