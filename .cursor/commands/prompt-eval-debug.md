---
name: prompt-eval-debug
version: 1
description: Debug any prompt with a tiny eval suite (control, edge, boundary), failure diagnosis, and smallest next change—no blind rewrite
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/prompt-eval-debug/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Improve a pasted prompt by designing a tiny eval suite, diagnosing failures, and proposing the smallest next change — without rewriting blindly. Full workflow: `.cursor/skills/prompt-eval-debug/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Eval suite | 1 control (C0) + 3 edge (E1–E3) + 1 capability-boundary (B1) |
| Prompt change | Smallest next change only (no full rewrite in v1) |
| Scoring | User runs cases manually; skill does not claim CI or automated scores |
| Examples | Generic names only (`service-a`, `task-handler`) |

## Steps

1. **Read** `.cursor/skills/prompt-eval-debug/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake → Tiny eval suite → Run guidance → Diagnosis → Smallest next change → Deliver).
3. **Report** suite table, diagnoses, and one smallest next change in chat.

## Anti-patterns

- Do not rewrite the whole prompt without an eval suite and diagnosis
- Do not skip the capability-boundary case (B1)
- Do not claim catalog CI ran the user's ad-hoc suite
- Do not use employer, product, or internal repo names in examples (OSS catalog)

## Examples

- `/prompt-eval-debug` with pasted prompt and task description
- `/prompt-eval-debug` for a `task-handler` routing prompt that fails on ambiguous input

## Maintainers

Behavioral eval: `.cursor/skills/prompt-eval-debug/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
