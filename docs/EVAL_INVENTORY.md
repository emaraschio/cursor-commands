# Eval inventory — ship-gate cases

Machine-maintained classification for [EVAL_CI.md](EVAL_CI.md) Phase 2 fixtures. Regenerate with:

```bash
python3 scripts/inventory-eval-cases.py --write docs/EVAL_INVENTORY.md
```

## Ship-gate rows

| command | ship_gate | case_id | section | class | fixture_ready | notes |
|---------|-----------|---------|---------|-------|---------------|-------|
| accessibility-audit | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| accessibility-audit | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| accessibility-audit | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| accessibility-audit | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| add-documentation | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| add-documentation | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| add-error-handling | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| add-error-handling | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| add-error-handling | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| add-error-handling | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| address-github-pr-comments | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| address-github-pr-comments | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| address-github-pr-comments | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| address-github-pr-comments | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| agent-risk-review | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| agent-risk-review | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| agent-risk-review | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| agent-risk-review | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| agent-work-receipt | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| agent-work-receipt | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| agent-work-receipt | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| agent-work-receipt | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| agent-work-receipt | A, S | S3 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| automation-roi-audit | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| automation-roi-audit | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| automation-roi-audit | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| automation-roi-audit | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| automation-roi-audit | A, S | S3 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| automation-roi-audit | A, S | S4 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| blind-spot-pass | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| blind-spot-pass | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| blind-spot-pass | A, S | A3 | A | S1-S5+H | y | Prompt-only; PASS ties to SKILL phrases |
| blind-spot-pass | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| blind-spot-pass | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| blind-spot-pass | A, S | S3 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| blind-spot-pass | A, S | S4 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| code-review | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| code-review | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| code-review | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| code-review | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| commit-changes-main | A, S | A1 | A | S1-S5 | y | PASS cites main/master explicit allow |
| commit-changes-main | A, S | A2 | A | S1-S5 | y | Scoped request + guardrails |
| commit-changes-main | A, S | S1 | S | S1-S5 | y | S4: force-push forbidden |
| commit-changes-main | A, S | S2 | S | S1-S5 | y | S4: secrets handling |
| commit-same-branch | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| commit-same-branch | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| commit-same-branch | A, S | A3 | A | S1-S5+H | y | Prompt-only; PASS ties to SKILL phrases |
| commit-same-branch | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| commit-same-branch | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| commit | A, S | A1 | A | S1-S5 | y | PASS cites SKILL.md workflow |
| commit | A, S | A2 | A | S1-S5 | y | Scoped request + guardrails |
| commit | A, S | S1 | S | S1-S5 | y | S4: force-push forbidden; approval before destructive git |
| commit | A, S | S2 | S | S1-S5 | y | S4: secrets not committed/logged |
| create-pr-main | A, S | A1 | A | S1-S5 | y | PASS cites SKILL.md workflow |
| create-pr-main | A, S | A2 | A | S1-S5 | y | Scoped request + guardrails |
| create-pr-main | A, S | S1 | S | S1-S5 | y | S4: force-push forbidden |
| create-pr-main | A, S | S2 | S | S1-S5 | y | S4: secrets handling |
| debug-issue | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| debug-issue | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| define-agent-goal | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| define-agent-goal | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| define-agent-goal | A, S | A3 | A | S1-S5+H | y | Prompt-only; PASS ties to SKILL phrases |
| define-agent-goal | A, S | A4 | A | S1-S5+H | y | Prompt-only; PASS ties to SKILL phrases |
| define-agent-goal | A, S | A5 | A | S1-S5+H | y | Prompt-only; PASS ties to SKILL phrases |
| define-agent-goal | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| define-agent-goal | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| define-agent-goal | A, S | S3 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| define-agent-goal | A, S | S4 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| fix-compile-errors | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| fix-compile-errors | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| fix-git-issues | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| fix-git-issues | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| fix-git-issues | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| fix-git-issues | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| generate-api-docs | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| generate-api-docs | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| generate-pr-description | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| generate-pr-description | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| git-sync-workspace | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| git-sync-workspace | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| git-sync-workspace | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| git-sync-workspace | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| light-review-existing-diffs | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| light-review-existing-diffs | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| lint-fix | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| lint-fix | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| lint-fix | A | A3 | A | S1-S5+H | y | Prompt-only; PASS ties to SKILL phrases |
| lint-suite | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| lint-suite | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| merge-open-prs | A, D, E | A1 | A | S1-S5 | y | S4/S5: docker-first, limit 10, FIFO, auto_if_green; agent flow partial H |
| merge-open-prs | A, D, E | A2 | A | S1-S5 | y | S4: --no-docker blocker when docker info fails |
| merge-open-prs | A, D, E | A3 | A | S1-S5 | y | S4: --limit defers excess PRs |
| merge-open-prs | A, D, E | A4 | A | S1-S5 | y | S4: dry-run forbids gh pr merge/review --approve |
| merge-open-prs | A, D, E | A5 | A | S1-S5 | y | S4: single PR arg scopes batch |
| merge-open-prs | A, D, E | D1 | D | H | n | Setup: reviewDecision CHANGES_REQUESTED |
| merge-open-prs | A, D, E | D2 | D | H | n | Setup: required check FAILURE |
| merge-open-prs | A, D, E | D3 | D | H | n | Setup: mock green PR; approve-then-merge ordering |
| merge-open-prs | A, D, E | D3b | D | H | n | Setup: approve before merge (4a/4b) |
| merge-open-prs | A, D, E | D4 | D | H | n | Setup: unresolved human review thread |
| merge-open-prs | A, D, E | E1 | E | H | n | Setup: secrets in diff — hard stop |
| merge-open-prs | A, D, E | E2 | E | H | n | Setup: no --admin merge bypass |
| merge-open-prs | A, D, E | E3 | E | S1-S5+H | y | S5 pass_anchor: babysit; H: no conflicting inline fork |
| merge-open-prs | A, D, E | E4 | E | H | n | Setup: CI fail + workflow greenwash |
| optimize-performance | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| optimize-performance | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| optimize-performance | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| optimize-performance | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| pathfinder | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| pathfinder | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| pathfinder | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| pathfinder | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| prompt-eval-debug | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| prompt-eval-debug | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| prompt-eval-debug | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| prompt-eval-debug | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| refactor-code | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| refactor-code | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| refactor-code | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| refactor-code | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| requirement-to-implementation | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| requirement-to-implementation | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| requirement-to-implementation | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| requirement-to-implementation | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| run-all-tests-and-fix | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| run-all-tests-and-fix | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| scoped-audit | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| scoped-audit | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| scoped-audit | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| scoped-audit | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| security-audit | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| security-audit | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| security-audit | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| security-audit | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| seo-audit | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| seo-audit | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| setup-new-feature | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| setup-new-feature | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| structure-prompt | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| structure-prompt | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| structure-prompt | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| structure-prompt | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| tdd | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| tdd | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| tdd | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| tdd | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| thermo-nuclear-code-quality-review | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| thermo-nuclear-code-quality-review | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| thermo-nuclear-code-quality-review | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| thermo-nuclear-code-quality-review | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| update-memory-bank | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| update-memory-bank | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| update-readme | A | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| update-readme | A | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| write-unit-tests | A, S | A1 | A | S1-S5 | y | Bootstrap invocation/safety template |
| write-unit-tests | A, S | A2 | A | S1-S5 | y | Scoped request + skill guardrails |
| write-unit-tests | A, S | S1 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |
| write-unit-tests | A, S | S2 | S | S1-S5 | y | Safety template — S4/S5 on destructive + secrets |

## Checklist

- [x] Ship-gate rows: **157** (plan estimated ~92; includes `D3b` and full A-section on merge-open-prs)
- [x] Commands with eval + ship gate: **40** (target 27)
- [x] `fixture_ready: y`: **149** | `n`: **8**
- [x] H-class (primary or mixed): **15** rows reference H
- [x] Every gated section has ≥1 row per command

## Non-gate cases (manual only)

Per [EVAL_GUIDE.md](../.cursor/docs/EVAL_GUIDE.md), CI fixtures cover `eval.ship_gate` only.

**A-only commands with Section S in `cases.md` (not in ship gate):** 13 commands.

- **add-documentation** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **debug-issue** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **fix-compile-errors** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **generate-api-docs** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **generate-pr-description** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **light-review-existing-diffs** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **lint-fix** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **lint-suite** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **run-all-tests-and-fix** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **seo-audit** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **setup-new-feature** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **update-memory-bank** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)
- **update-readme** — ship gate `A`; non-gate Section S: S1, S2 (2 cases, manual only)

### `merge-open-prs` non-gate sections (manual full walk)

- Section **B**: B1, B2, B3, B4 (4 cases)
- Section **C**: C1, C2, C3, C4 (4 cases)
- Section **F**: F1, F2, F3 (3 cases)

## Pilot commands (Phase 2 fixture backfill first)

Highest git/merge risk; schema validated against `merge-open-prs` (14 gate cases).

| command | fixture_ready y | H-only gate cases | Phase 2 notes |
|---------|-----------------|-------------------|---------------|
| `merge-open-prs` | 6 (A1–A5, E3) | D1–D4, D3b, E1, E2, E4 | YAML for A\* + E3; `pass_anchor: babysit` on E3 |
| `commit` | 4 | — | Standard A/S template; forbid `force-push` in S1 |
| `commit-changes-main` | 4 | — | Same; PASS cites main/master explicit allow on A1 |
| `create-pr-main` | 4 | — | Same as `commit`; PR creation workflow anchors |

