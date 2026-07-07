---
name: generate-api-docs
version: 2
description: Generate API documentation from code
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/generate-api-docs/eval/cases.md
  ship_gate: [A]
---

## Overview

Generate API documentation from code. Full workflow: `.cursor/skill-contracts/generate-api-docs/SKILL.md` (user install: `~/.cursor/skill-contracts/generate-api-docs/SKILL.md`).

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/generate-api-docs/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/generate-api-docs/SKILL.md`.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Document only endpoints that exist in code.** Trigger: writing the API reference. Wrong: inventing endpoints, parameters, or responses not present in the source. Correct: document only endpoints found in the code and verify each against the implementation. Reason: invented endpoints mislead consumers and break integrations.
- **Never expose secrets in examples.** Trigger: writing example requests and responses. Wrong: pasting real tokens, keys, or credentials into samples. Correct: use placeholder values for any secret in examples. Reason: committed secrets leak credentials and force rotation.

## Examples

- `/generate-api-docs`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/generate-api-docs/eval/cases.md`. Ship gate sections: **A** before changing `SKILL.md` or this command.
