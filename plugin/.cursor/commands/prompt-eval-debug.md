---
name: prompt-eval-debug
version: 2
description: Debug any prompt with a tiny eval suite (control, edge, boundary), failure diagnosis, and smallest next change, no blind rewrite
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/prompt-eval-debug/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Improve a pasted prompt by designing a tiny eval suite, diagnosing failures, and proposing the smallest next change, without rewriting blindly. Full workflow: `.cursor/skill-contracts/prompt-eval-debug/SKILL.md`.

## Defaults

| Setting | Default |
|---------|---------|
| Eval suite | 1 control (C0) + 3 edge (E1 to E3) + 1 capability-boundary (B1) |
| Prompt change | Smallest next change only (no full rewrite in v1) |
| Scoring | User runs cases manually; skill does not claim CI or automated scores |
| Examples | Generic names only (`service-a`, `task-handler`) |

## Steps

1. **Read** `.cursor/skill-contracts/prompt-eval-debug/SKILL.md` for the full agent contract.
2. **Execute** phases in order (Intake → Tiny eval suite → Run guidance → Diagnosis → Smallest next change → Deliver).
3. **Report** suite table, diagnoses, and one smallest next change in chat.

## Anti-patterns

- **Do not rewrite blindly.** Trigger: the user asks to rewrite the whole prompt and skip the eval work. Wrong: replacing the entire prompt in one shot with no suite or diagnosis. Correct: produce the tiny eval suite and the smallest next change first, and rewrite fully only after explicit request. Reason: a blind rewrite discards what worked and hides why the prompt failed.
- **Keep the capability-boundary case.** Trigger: building the five-case suite. Wrong: dropping B1 or expecting the model to succeed without the tools it needs. Correct: include a capability-boundary case that expects escalate, ask, or refuse, and diagnose missing tool or capability when relevant. Reason: instructions are not capabilities, and skipping B1 hides hallucinated success.
- **Do not claim catalog CI scored the suite.** Trigger: reporting suite outcomes. Wrong: stating automated pass/fail scores the user never ran. Correct: present the suite and ask the user to run it, reporting only results they confirm. Reason: this skill does not execute the catalog CI, so asserting scores would misrepresent what was verified.

## Examples

- `/prompt-eval-debug` with pasted prompt and task description
- `/prompt-eval-debug` for a `task-handler` routing prompt that fails on ambiguous input

## Maintainers

Behavioral eval: `.cursor/skill-contracts/prompt-eval-debug/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
