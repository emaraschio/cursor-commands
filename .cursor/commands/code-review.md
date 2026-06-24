---
name: code-review
version: 2
description: Thorough PR code review before approval
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/code-review/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Thorough PR code review before approval. Full workflow: `.cursor/skills/code-review/SKILL.md`.

## Defaults

_None — see skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/code-review/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Check security and tests before approving.** Trigger: a change that looks clean on the surface. Wrong: approving without reviewing security-sensitive paths or test coverage. Correct: verify security risks and test coverage before signing off. Reason: an approval is a quality gate, so unverified code ships vulnerabilities and regressions.
- **Weigh substance over style.** Trigger: noticing formatting or naming preferences. Wrong: blocking the review on subjective style nits. Correct: focus on correctness, design, and risk, and raise style points as non-blocking. Reason: style nitpicks crowd out substantive feedback and stall the author.

## Examples

- `/code-review`

## Maintainers

Behavioral eval: `.cursor/skills/code-review/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
