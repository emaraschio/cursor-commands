---
name: merge-open-prs
version: 1
description: Batch review, verify (Docker-first), and merge open PRs when green
scope: generic
requires_skill: true
eval:
  path: .cursor/skills/merge-open-prs/eval/cases.md
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

1. **Read** `.cursor/skills/merge-open-prs/SKILL.md` for the full contract (preflight, inventory, babysit, review, verify, gate, merge, post-smoke).
2. **Parse flags:** `--dry-run`, `--no-docker`, `--limit N`, optional PR number.
3. **Execute** phases 0–5 in order. Per PR, follow **babysit** at `~/.cursor/skills-cursor/babysit/SKILL.md`.
4. **Emit** plan table before processing and summary table after post-batch smoke.

## Anti-patterns

- Merging without local verify or gate pass
- Silently skipping Docker when `docker info` fails (use `--no-docker` explicitly)
- Processing unbounded PRs
- Duplicating babysit inline instead of reading the skill

## Examples

- `/merge-open-prs`
- `/merge-open-prs --dry-run`
- `/merge-open-prs --limit 3`
- `/merge-open-prs 42`

## Maintainers

Behavioral eval: `.cursor/skills/merge-open-prs/eval/cases.md`. Ship gate: **A, D, E** before changing `SKILL.md`.
