---
name: write-unit-tests
version: 2
description: Write meaningful unit tests for target code
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/write-unit-tests/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Write meaningful unit tests for target code. Full workflow: `.cursor/skills/write-unit-tests/SKILL.md`.

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skills/write-unit-tests/SKILL.md` for the full agent contract.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Test behavior, not implementation trivia.** Trigger: choosing what a unit test should assert. Wrong: asserting private internals, call counts, or getters that restate the code. Correct: assert observable behavior and public contracts. Reason: trivia tests break on harmless refactors and prove nothing about correctness.
- **Mock only what you must.** Trigger: the unit under test touches collaborators. Wrong: mocking every dependency, including pure logic you could call directly. Correct: mock external boundaries (network, clock, filesystem) and use real objects for the rest. Reason: over-mocking tests the mocks instead of the code and hides real integration breaks.

## Examples

- `/write-unit-tests`

## Maintainers

Behavioral eval: `.cursor/skills/write-unit-tests/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
