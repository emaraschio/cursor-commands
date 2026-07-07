---
name: merge-open-prs
version: 2
description: Batch review, verify (Docker-first), and merge open PRs when green
scope: generic
requires_skill: true
eval:
  path: .cursor/skill-contracts/merge-open-prs/eval/cases.md
  ship_gate: [A, D, E]
---

## Overview

Review, verify, approve, and merge open pull requests in the **current repo**. Docker verification and batch cap of 10 are on by default.

## Defaults

| Setting | Default | Override |
|---------|---------|----------|
| Verification | **Docker-first** | `--no-docker` |
| Batch size | **10 PRs** | `--limit N` |
| Merge | **auto_if_green** | `--dry-run` |

## Steps

1. **Read** `.cursor/skill-contracts/merge-open-prs/SKILL.md` for the full contract (preflight, inventory, babysit, review, verify, gate, merge, post-smoke); if that file is missing, read `~/.cursor/skill-contracts/merge-open-prs/SKILL.md`.
2. **Parse flags:** `--dry-run`, `--no-docker`, `--limit N`, optional PR number.
3. **Execute** phases 0 to 5 in order. Per PR, follow **babysit** at `~/.cursor/skills-cursor/babysit/SKILL.md`.
4. **Emit** plan table before processing and summary table after post-batch smoke.

## Anti-patterns

- **Merge only when the gate passes.** Trigger: a PR looks ready. Wrong: merging without local verification or a passing auto_if_green gate. Correct: run local verify, confirm CI, reviews, and threads, then merge only if every gate check passes. Reason: merging unverified code can break the default branch for everyone.
- **Do not silently skip Docker.** Trigger: `docker info` fails and the user did not pass `--no-docker`. Wrong: falling back to host test heuristics without telling the user. Correct: stop with a blocker and suggest `--no-docker` only if they accept non-Docker verification. Reason: a silent fallback verifies the PR differently than intended and can mask failures.
- **Keep the batch bounded.** Trigger: more open PRs than the limit. Wrong: processing an unbounded queue of PRs. Correct: process up to `--limit` (default 10) FIFO and report the deferred count. Reason: runaway merges are hard to review and hard to undo.

## Examples

- `/merge-open-prs`
- `/merge-open-prs --dry-run`
- `/merge-open-prs --limit 3`
- `/merge-open-prs 42`

## Maintainers

Behavioral eval: `.cursor/skill-contracts/merge-open-prs/eval/cases.md`. Ship gate: **A, D, E** before changing `SKILL.md`.
