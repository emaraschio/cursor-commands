---
name: tdd
version: 2
description: Canon TDD (specify, encode, fulfill) with one test at a time, approval gates, and kitchen-cleaning refactor when needed
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/tdd/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Guide a specify-encode-fulfill TDD session on the host project's test framework: clarify specs, one failing test per cycle, minimal code to green, user approval before continuing. Full workflow: `.cursor/skill-contracts/tdd/SKILL.md` (user install: `~/.cursor/skill-contracts/tdd/SKILL.md`).

## Defaults

| Setting | Default |
|---------|---------|
| Loop | Specify → one failing test → minimal fulfill → behavior commit → optional refactor |
| Tests per cycle | One |
| Specification form | Under scenario A, X happens; under scenario B, Y happens |
| Pre-existing failures | Pause; fix or stash before continuing |
| RSpec examples | `.cursor/skill-contracts/tdd/appendix-rspec-examples.md` (fallback: `~/.cursor/skill-contracts/tdd/appendix-rspec-examples.md`) |

## Steps

1. **Read** `.cursor/skill-contracts/tdd/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/tdd/SKILL.md`.
2. **Execute** clarify → specification list → kitchen check → one-test cycles with approvals.
3. **Report** progress per cycle; do not batch tests or skip approval gates.

## Anti-patterns

- **One failing test per cycle, minimal code to green.** Trigger: starting a TDD cycle. Wrong: writing the whole test suite up front, or adding speculative code beyond the current failing test. Correct: encode one failing test, then write just enough code to pass it. Reason: batching tests or speculative code abandons the red-green loop that keeps the design honest.
- **Assert concrete behavior, never vague correctness.** Trigger: writing a test assertion. Wrong: asserting "works correctly" or "handles properly" without stating the expected outcome. Correct: assert the specific expected result for the scenario. Reason: vague assertions pass without proving the behavior, so they catch no regression.
- **Keep behavior commits clean and the suite green.** Trigger: ready to commit a behavior change. Wrong: committing with unrelated failing tests, or mixing refactoring into the behavior commit. Correct: commit the behavior change alone on a green suite, then refactor separately. Reason: mixed or red commits make history hard to bisect and hide what actually changed.

## Examples

- `/tdd` with a draft specification in the message
- `/tdd` for label behavior on `service-a` when status is passed vs failed

## Maintainers

Behavioral eval: `.cursor/skill-contracts/tdd/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
