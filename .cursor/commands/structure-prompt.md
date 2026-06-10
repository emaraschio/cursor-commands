---
name: structure-prompt
version: 1
description: Turn a rough request into a structured, production-grade prompt using applicable prompting dimensions (verification, structured detail, constraints, structure, search priority, internal-first)
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/structure-prompt/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Compose a copyable, structured prompt from a rough ask by applying only the prompting dimensions that fit, then report what was applied or omitted. Produces a prompt; does not run the task. Full workflow: `.cursor/skills/structure-prompt/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Dimensions | Apply only those that fit (product verification, structured high-stakes, constraints-upfront, scannable structure, search priority, internal-first) |
| Effort | Proportional to stakes; trivial asks get a light prompt, not the full template |
| Output | One copyable prompt block + an applied/omitted note |
| Model | Model-agnostic; no hardcoded model names or canonical leaked-prompt claims |
| Examples | Generic names only (`service-a`) |

## Steps

1. **Read** `.cursor/skills/structure-prompt/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake -> Classify -> Fill template -> Deliver).
3. **Report** the structured prompt and the applied/omitted dimension note in chat.

## Anti-patterns

- Do not bolt on all six dimensions when the request is simple
- Do not execute the task the prompt describes; only produce the prompt
- Do not invent product capabilities, pricing, or model names
- Do not claim a leaked system prompt is canonical
- Do not use employer, product, or internal repo names in examples (OSS catalog)

## Examples

- `/structure-prompt` with a rough research request needing current sources
- `/structure-prompt` for an ambiguous report ask that needs constraints and a scannable format

## Maintainers

Behavioral eval: `.cursor/skills/structure-prompt/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
