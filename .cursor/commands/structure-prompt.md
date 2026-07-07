---
name: structure-prompt
version: 2
description: Turn a rough request into a structured, production-grade prompt using applicable prompting dimensions (verification, structured detail, constraints, structure, search priority, internal-first)
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/structure-prompt/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Compose a copyable, structured prompt from a rough ask by applying only the prompting dimensions that fit, then report what was applied or omitted. Produces a prompt; does not run the task. Full workflow: `.cursor/skill-contracts/structure-prompt/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Dimensions | Apply only those that fit (product verification, structured high-stakes, constraints-upfront, scannable structure, search priority, internal-first) |
| Effort | Proportional to stakes; trivial asks get a light prompt, not the full template |
| Output | One copyable prompt block + an applied/omitted note |
| Model | Model-agnostic; no hardcoded model names or canonical leaked-prompt claims |
| Examples | Generic names only (`service-a`) |

## Steps

1. **Read** `.cursor/skill-contracts/structure-prompt/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake -> Classify -> Fill template -> Deliver).
3. **Report** the structured prompt and the applied/omitted dimension note in chat.

## Anti-patterns

- **Match effort to stakes.** Trigger: a simple or one-line request. Wrong: bolting on all six dimensions and dumping the full template. Correct: produce a light prompt proportional to the ask and note which dimensions are not applicable. Reason: over-engineering a trivial ask wastes the user's time and buries the actual request.
- **Produce the prompt, do not run it.** Trigger: finishing the structured prompt. Wrong: executing the underlying task the prompt describes. Correct: return the copyable prompt and stop. Reason: this skill builds prompts, and running the task skips the user's review of the prompt.
- **Do not invent product facts.** Trigger: the prompt asks about a tool's current capabilities. Wrong: asserting pricing, APIs, or a model name from memory. Correct: add a clause to verify against current docs and flag that product knowledge may be stale. Reason: stale or invented product claims propagate into every downstream answer.

## Examples

- `/structure-prompt` with a rough research request needing current sources
- `/structure-prompt` for an ambiguous report ask that needs constraints and a scannable format

## Maintainers

Behavioral eval: `.cursor/skill-contracts/structure-prompt/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
