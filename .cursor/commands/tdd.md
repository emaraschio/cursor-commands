---
name: tdd
version: 1
description: Canon TDD (specify, encode, fulfill) with one test at a time, approval gates, and kitchen-cleaning refactor when needed
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/tdd/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Guide a specify-encode-fulfill TDD session on the host project's test framework: clarify specs, one failing test per cycle, minimal code to green, user approval before continuing. Full workflow: `.cursor/skills/tdd/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Loop | Specify → one failing test → minimal fulfill → behavior commit → optional refactor |
| Tests per cycle | One |
| Specification form | Under scenario A, X happens; under scenario B, Y happens |
| Pre-existing failures | Pause; fix or stash before continuing |
| RSpec examples | `.cursor/skills/tdd/appendix-rspec-examples.md` |

## Steps

1. **Read** `.cursor/skills/tdd/SKILL.md` for the full agent contract.
2. **Execute** clarify → specification list → kitchen check → one-test cycles with approvals.
3. **Report** progress per cycle; do not batch tests or skip approval gates.

## Anti-patterns

- Do not write all tests before implementation
- Do not use vague assertions ("works correctly", "handles properly")
- Do not commit with unrelated failing tests in the suite
- Do not mix behavior changes and refactoring in one commit
- Do not add speculative or defensive code beyond the current failing test

## Examples

- `/tdd` with a draft specification in the message
- `/tdd` for label behavior on `service-a` when status is passed vs failed

## Maintainers

Behavioral eval: `.cursor/skills/tdd/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
