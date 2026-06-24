---
name: lint-suite
version: 2
description: Run project linters and fix findings repo-wide
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/lint-suite/eval/cases.md
  ship_gate: [A]
---

## Overview

Run project linters and fix findings repo-wide. Full workflow: `.cursor/skills/lint-suite/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/lint-suite/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Do not disable rules to pass.** Trigger: a lint rule that is hard to satisfy. Wrong: disabling or suppressing the rule to get a green run. Correct: fix the underlying issue, suppressing only with a documented justification. Reason: silencing rules hides real problems and erodes the value of the linter.
- **Re-run the linter to verify zero issues.** Trigger: finishing a batch of lint fixes. Wrong: assuming the fixes worked without re-running. Correct: re-run the linter and confirm a clean, zero-issue result. Reason: unverified fixes can leave or introduce violations that reach the main branch.

## Examples

- `/lint-suite`

## Maintainers

Behavioral eval: `.cursor/skills/lint-suite/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
