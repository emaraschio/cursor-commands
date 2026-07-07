# Commands index

Canonical catalog of slash commands. Authoring: [COMMAND_SCHEMA.md](COMMAND_SCHEMA.md). Evals: [EVAL_GUIDE.md](EVAL_GUIDE.md).

## Ship gate

**Ship gate** is the set of behavioral eval sections you must **PASS** (no `PARTIAL`, no `FAIL`) before merging changes to that command’s `SKILL.md` or slash entry.

| Concept | Where it lives |
|---------|----------------|
| Section IDs in the table below | Copied from command frontmatter `eval.ship_gate` (e.g. `A, S`) |
| Rubric cases | `skills/<name>/eval/cases.md` under headings like `## Section A: …` |
| How to walk and score | [EVAL_GUIDE.md](EVAL_GUIDE.md) |

**Common section letters** (not every command uses all of them):

| ID | Typical theme | Examples |
|----|----------------|----------|
| **A** | Invocation / defaults | Bare `/command`, scoped request, flags (`--dry-run`, `--limit`) |
| **S** | Safety | No destructive git/production actions without consent; no leaking secrets |
| **D** | Gate / merge policy | CI green, approvals, dry-run must not merge (`merge-open-prs` only today) |
| **E** | Extended safety | Batch limits, babysit contract, post-merge smoke (`merge-open-prs` only today) |

Commands with extra sections in `cases.md` (e.g. **B**, **C**, **F** on `merge-open-prs`) are still useful for full walks; only the letters listed in **Ship gate** block release for that command.

**Release bar:** 100% PASS on ship gate sections; optional full walk targets ≥90% adjusted pass across all cases. See each skill’s `eval/README.md`.

**CI:** [eval-fixtures.yml](../../.github/workflows/eval-fixtures.yml) runs `run-eval-fixtures.py --strict` on ship-gate cases. Spec: [docs/EVAL_CI.md](../../docs/EVAL_CI.md). Inventory: [docs/EVAL_INVENTORY.md](../../docs/EVAL_INVENTORY.md). Non-gate sections still need manual walks.

| Command | Scope | Skill | Eval cases | Ship gate | Last reviewed |
|---------|-------|-------|------------|-----------|---------------|
| `accessibility-audit` | generic | yes | [cases](../skills/accessibility-audit/eval/cases.md) | A, S | 2026-06-24 PASS |
| `add-documentation` | generic | yes | [cases](../skills/add-documentation/eval/cases.md) | A | 2026-06-24 PASS |
| `add-error-handling` | generic | yes | [cases](../skills/add-error-handling/eval/cases.md) | A, S | 2026-06-24 PASS |
| `address-github-pr-comments` | generic | yes | [cases](../skills/address-github-pr-comments/eval/cases.md) | A, S | 2026-06-24 PASS |
| `agent-risk-review` | generic | yes | [cases](../skills/agent-risk-review/eval/cases.md) | A, S | 2026-06-24 PASS |
| `agent-work-receipt` | generic | yes | [cases](../skills/agent-work-receipt/eval/cases.md) | A, S | 2026-06-24 PASS |
| `blind-spot-pass` | generic | yes | [cases](../skills/blind-spot-pass/eval/cases.md) | A, S | 2026-07-07 PASS |
| `code-review` | generic | yes | [cases](../skills/code-review/eval/cases.md) | A, S | 2026-06-24 PASS |
| `commit` | generic | yes | [cases](../skills/commit/eval/cases.md) | A, S | 2026-06-24 PASS |
| `commit-changes-main` | generic | yes | [cases](../skills/commit-changes-main/eval/cases.md) | A, S | 2026-06-24 PASS |
| `commit-same-branch` | generic | yes | [cases](../skills/commit-same-branch/eval/cases.md) | A, S | 2026-06-24 PASS |
| `create-pr-main` | generic | yes | [cases](../skills/create-pr-main/eval/cases.md) | A, S | 2026-06-24 PASS |
| `debug-issue` | generic | yes | [cases](../skills/debug-issue/eval/cases.md) | A | 2026-06-24 PASS |
| `define-agent-goal` | generic | yes | [cases](../skills/define-agent-goal/eval/cases.md) | A, S | 2026-06-24 PASS |
| `fix-compile-errors` | generic | yes | [cases](../skills/fix-compile-errors/eval/cases.md) | A | 2026-06-24 PASS |
| `fix-git-issues` | generic | yes | [cases](../skills/fix-git-issues/eval/cases.md) | A, S | 2026-06-24 PASS |
| `generate-api-docs` | generic | yes | [cases](../skills/generate-api-docs/eval/cases.md) | A | 2026-06-24 PASS |
| `generate-pr-description` | generic | yes | [cases](../skills/generate-pr-description/eval/cases.md) | A | 2026-06-24 PASS |
| `git-sync-workspace` | generic | yes | [cases](../skills/git-sync-workspace/eval/cases.md) | A, S | 2026-06-24 PASS |
| `light-review-existing-diffs` | generic | yes | [cases](../skills/light-review-existing-diffs/eval/cases.md) | A | 2026-06-24 PASS |
| `lint-fix` | generic | yes | [cases](../skills/lint-fix/eval/cases.md) | A | 2026-06-24 PASS |
| `lint-suite` | generic | yes | [cases](../skills/lint-suite/eval/cases.md) | A | 2026-06-24 PASS |
| `merge-open-prs` | generic | yes | [cases](../skills/merge-open-prs/eval/cases.md) | A, D, E | 2026-06-24 PASS |
| `optimize-performance` | generic | yes | [cases](../skills/optimize-performance/eval/cases.md) | A, S | 2026-06-24 PASS |
| `pathfinder` | generic | yes | [cases](../skills/pathfinder/eval/cases.md) | A, S | 2026-07-02 PASS |
| `prompt-eval-debug` | generic | yes | [cases](../skills/prompt-eval-debug/eval/cases.md) | A, S | 2026-06-24 PASS |
| `refactor-code` | generic | yes | [cases](../skills/refactor-code/eval/cases.md) | A, S | 2026-06-24 PASS |
| `requirement-to-implementation` | generic | yes | [cases](../skills/requirement-to-implementation/eval/cases.md) | A, S | 2026-06-24 PASS |
| `run-all-tests-and-fix` | generic | yes | [cases](../skills/run-all-tests-and-fix/eval/cases.md) | A | 2026-06-24 PASS |
| `scoped-audit` | generic | yes | [cases](../skills/scoped-audit/eval/cases.md) | A, S | 2026-06-24 PASS |
| `security-audit` | generic | yes | [cases](../skills/security-audit/eval/cases.md) | A, S | 2026-06-24 PASS |
| `seo-audit` | generic | yes | [cases](../skills/seo-audit/eval/cases.md) | A | 2026-06-24 PASS |
| `setup-new-feature` | generic | yes | [cases](../skills/setup-new-feature/eval/cases.md) | A | 2026-06-24 PASS |
| `structure-prompt` | generic | yes | [cases](../skills/structure-prompt/eval/cases.md) | A, S | 2026-06-24 PASS |
| `tdd` | generic | yes | [cases](../skills/tdd/eval/cases.md) | A, S | 2026-06-24 PASS |
| `thermo-nuclear-code-quality-review` | generic | yes | [cases](../skills/thermo-nuclear-code-quality-review/eval/cases.md) | A, S | 2026-06-24 PASS |
| `update-memory-bank` | generic | yes | [cases](../skills/update-memory-bank/eval/cases.md) | A | 2026-06-24 PASS |
| `update-readme` | generic | yes | [cases](../skills/update-readme/eval/cases.md) | A | 2026-06-24 PASS |
| `write-unit-tests` | generic | yes | [cases](../skills/write-unit-tests/eval/cases.md) | A, S | 2026-06-24 PASS |

**Organization-specific commands** live in the **host workspace** that installs this pack (`.cursor/commands/` + `.cursor/skills/` overlay after `./scripts/install.sh`). Not shipped here.

