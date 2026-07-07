---
name: address-github-pr-comments
version: 2
description: Address review comments on the current GitHub PR
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/address-github-pr-comments/eval/cases.md
  ship_gate: [A, S]
---

## Overview

Address review comments on the current GitHub PR. Full workflow: `.cursor/skill-contracts/address-github-pr-comments/SKILL.md` (user install: `~/.cursor/skill-contracts/address-github-pr-comments/SKILL.md`).

## Defaults

_None. See skill for workflow defaults._

## Steps

1. **Read** `.cursor/skill-contracts/address-github-pr-comments/SKILL.md` for the full agent contract; if that file is missing, read `~/.cursor/skill-contracts/address-github-pr-comments/SKILL.md`.
2. **Execute** the workflow in order; do not skip safety steps.
3. **Report** outcomes per skill (summary, tables, or checklist as specified).

## Anti-patterns

- **Push only when asked.** Trigger: fixes for review comments are committed. Wrong: pushing to the PR branch without being asked. Correct: push only on an explicit request from the user. Reason: an unrequested push can trigger CI and notify reviewers before the work is ready.
- **Do not dismiss valid security feedback.** Trigger: a reviewer raises a security concern. Wrong: marking the thread resolved without addressing it. Correct: address the concern or justify with evidence before resolving. Reason: dismissing valid security feedback can ship a real vulnerability.

## Examples

- `/address-github-pr-comments`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/address-github-pr-comments/eval/cases.md`. Ship gate sections: **A, S** before changing `SKILL.md` or this command.
