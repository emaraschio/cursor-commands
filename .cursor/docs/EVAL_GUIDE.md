# Behavioral evaluation guide

Manual rubric walks for Cursor commands. No automated agent runner in v1.

## When to run

- Before merging changes to `commands/<name>.md` or `skills/<name>/SKILL.md`
- When bumping `version` in command frontmatter
- After adding or editing eval cases

## Ad-hoc prompt debugging

Catalog evals are **regression guardrails** for shipped commands. When you are still iterating on wording, use [`/prompt-eval-debug`](../commands/prompt-eval-debug.md) ([`skills/prompt-eval-debug/SKILL.md`](../skills/prompt-eval-debug/SKILL.md)) to draft a tiny suite (control, edge, capability-boundary) before rewriting a prompt or adding rows to `eval/cases.md`. That command does not run in CI and does not replace ship-gate walks.

For **Canon TDD sessions** (one test at a time, specify-encode-fulfill), use [`/tdd`](../commands/tdd.md) ([`skills/tdd/SKILL.md`](../skills/tdd/SKILL.md)): a workflow skill, not a substitute for `eval/cases.md`.

## How to score

1. Read `skills/<name>/SKILL.md` only (pretend you have not seen the command file).
2. For each case in `eval/cases.md`, draft what the agent would do.
3. Verdict: `PASS` | `PARTIAL` | `FAIL`
4. **Adjusted pass rate:** `PARTIAL` counts as `FAIL`
5. Target: **0 FAIL**, ≥90% adjusted on full walk; **ship gate sections must be 100% PASS**

## Ship gate

Each command frontmatter lists `eval.ship_gate` (e.g. `[A, S]`). You must PASS every case in those sections before push.

## User rules

Global Cursor user rules (commit, PR, git safety) override command text on conflict. Eval cases for git commands note alignment with those rules.

## Recording results

Optional: note date and outcome in `COMMANDS_INDEX.md` column `last_reviewed`.

## Future automation

Org-specific benchmark skills in a host workspace overlay may run cases in parallel. v1 stays manual only in this repo.
