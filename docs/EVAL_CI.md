# Eval CI specification

Authoritative spec for ship-gate enforcement in GitHub Actions. **Phase 2 implemented:** [run-eval-fixtures.py](../scripts/run-eval-fixtures.py), [eval-fixtures.yml](../.github/workflows/eval-fixtures.yml), `fixtures.yaml` on all 28 commands.

Related: [EVAL_GUIDE.md](../.cursor/docs/EVAL_GUIDE.md) (manual walks), [COMMANDS_INDEX.md](../.cursor/docs/COMMANDS_INDEX.md) (ship gate column), [ROADMAP.md](ROADMAP.md) (priority track).

## Problem

`validate-cursor-commands.py` confirms files and frontmatter exist. It does **not** verify that `SKILL.md` still satisfies ship-gate cases in `eval/cases.md`. Ship gate is the merge contract; CI must enforce it structurally before v1.0.

## Enforcement model (v1 — full structural)

No LLM in CI. Five automated check layers plus one manual-only class:

| Class | Check | Phase 2 owner |
|-------|--------|----------------|
| **S1** | Rubric shape: `**Prompt:**`, `**PASS if:**`, `**FAIL if:**` on each ship-gate case | `run-eval-fixtures.py` |
| **S2** | `## Section <id>` exists for every id in `eval.ship_gate` | `validate-cursor-commands.py` |
| **S3** | Command `## Steps` references `SKILL.md` (step 1) | `run-eval-fixtures.py` |
| **S4** | `SKILL.md` contains `skill_required` / omits `skill_forbidden` from `fixtures.yaml` | `run-eval-fixtures.py` |
| **S5** | `**PASS if:**` aligns with text in `SKILL.md` (phrase match or `pass_anchor`) | `run-eval-fixtures.py` |
| **H** | Agent behavior under `**Setup:**` or mock state — human walk only | Not in CI |

Inventory column `fixture_ready`: **y** only when S4+S5 can block bad `SKILL.md` edits without an agent run.

---

## Fixture file layout

Per command with a slash entry and eval:

```text
.cursor/skills/<name>/eval/fixtures.yaml
```

Only ship-gate cases (`eval.ship_gate` in command frontmatter). Non-gate sections (e.g. `merge-open-prs` B/C/F) stay manual.

### Schema (`schema_version: 1`)

```yaml
schema_version: 1
command: commit
ship_gate: [A, S]
cases:
  A1:
    rubric: required
    skill_required:
      - "SKILL.md"
      - "conventional"
    skill_forbidden:
      - "force-push"
    pass_must_reference_skill: true
  S1:
    skill_required:
      - "destructive"
    skill_forbidden:
      - "without approval"
    pass_must_reference_skill: true
  A2:
    rubric: required
    pass_must_reference_skill: true
```

| Field | Required | Meaning |
|-------|----------|---------|
| `rubric` | When `fixture_ready` | Must be `required` — runner validates PASS/FAIL lines |
| `skill_required` | Optional | Substrings that must appear in `SKILL.md` (case-insensitive) |
| `skill_forbidden` | Optional | Substrings that must not appear in `SKILL.md` |
| `pass_must_reference_skill` | Optional | If true, run S5 alignment on `**PASS if:**` |
| `pass_anchor` | Optional | Exact substring when PASS prose is abstract but skill text exists |

**H-class cases:** no `fixtures.yaml` entry; listed in inventory with `fixture_ready: n`.

Phase 2 rollout: require `fixtures.yaml` for every inventory row with `fixture_ready: y`.

### Pilot examples (Phase 2 backfill order)

See [EVAL_INVENTORY.md — Pilot commands](EVAL_INVENTORY.md#pilot-commands-phase-2-fixture-backfill-first).

`commit` / `create-pr-main` / `commit-changes-main` share the bootstrap A+S template (four `fixture_ready: y` rows each). `merge-open-prs` mixes six structural rows (A1–A5, E3) with eight **H** rows (D\\*, E1/E2/E4) that stay manual-only in v1.

---

## Global structural checks

Applied to every command in the catalog (27 today):

| check_id | Rule |
|----------|------|
| `missing_section` | Each `ship_gate` id has `## Section <id>` in `cases.md` |
| `missing_case` | Each gated section has ≥1 `###` case |
| `rubric_incomplete` | Each ship-gate case has `**PASS if:**` and `**FAIL if:**` |
| `command_no_skill_ref` | Command body step 1 references `SKILL.md` |
| `index_ship_gate_mismatch` | [COMMANDS_INDEX.md](../.cursor/docs/COMMANDS_INDEX.md) ship gate column matches frontmatter |

---

## S5 alignment algorithm (Phase 2)

1. **Extract phrases** from `SKILL.md`: lines under `##` / `###`, table cell text, `**bold**`, backtick literals (min length 4 after trim).
2. **Parse** each ship-gate case `**PASS if:**` (and optional `pass_anchor` from `fixtures.yaml`).
3. **Match:** at least one extracted phrase appears as a substring of PASS text (case-insensitive), or `pass_anchor` is a substring of `SKILL.md`.
4. **Stopwords** stripped for token overlap fallback: `the`, `a`, `an`, `and`, `or`, `must`, `should`, `agent`, `user`, `if`, `not`.

Failure: `pass_alignment_failed` with case id and hint to add `pass_anchor`.

---

## CI scope (Phase 2)

Workflow name: **`eval-fixtures.yml`**.

| Event | Paths |
|-------|--------|
| `pull_request` → `main` | `.cursor/commands/**`, `.cursor/skills/**`, `scripts/run-eval-fixtures.py`, `scripts/validate-cursor-commands.py`, `scripts/inventory-eval-cases.py` |
| `push` → `main` | same |
| `workflow_dispatch` | full catalog |

**Job layout (recommended):** single job, ordered steps:

1. `python3 scripts/check_forbidden_org_strings.py`
2. `python3 scripts/validate-cursor-commands.py` (extended S2)
3. `python3 scripts/run-eval-fixtures.py`

Keeps one checkout; `validate.yml` may remain for fast path-only PRs until workflows are merged.

**Branch protection:** require **Eval fixtures** (new) alongside Validate, Docs, Install smoke.

`docs/**` changes do not need to run fixtures unless they touch inventory/spec (optional path add later).

---

## Failure contract

| Requirement | Behavior |
|-------------|----------|
| Exit code | `1` if any check fails |
| Success stdout | `OK: <N> commands, <M> ship-gate cases checked` |
| Failure stderr | `FAIL <command> <case_id> <check_id> <message>` |
| Job summary | Markdown table: command, case_id, check_id, message (Phase 2) |

**Stable `check_id` values:** `missing_section`, `missing_case`, `rubric_incomplete`, `skill_required_missing`, `skill_forbidden_present`, `pass_alignment_failed`, `command_no_skill_ref`, `index_ship_gate_mismatch`, `fixtures_missing`, `fixtures_invalid`.

**Example:**

```text
FAIL merge-open-prs D3 pass_alignment_failed PASS line has no SKILL.md anchor
```

---

## v1.0 public launch gate

**Decision (Phase 1):** Eval CI Phase 2 is a **hard blocker** for making this repository public.

Rationale: ship gate is the only enforced quality contract for prompts; without CI, the catalog is documentation-only.

**Public catalog (v1.0.0+):** All 28 commands have ship-gate `fixtures.yaml` where applicable. Every ship-gate row in [EVAL_INVENTORY.md](EVAL_INVENTORY.md) is either `fixture_ready: y` with a `fixtures.yaml` entry, or `fixture_ready: n` with `class: H` and documented waiver (e.g. `merge-open-prs` Setup/H cases).

---

## Non-goals (v1)

- LLM or Cursor agent invocation in CI
- Running `gh`, Docker, git, or live PR merges
- Scoring PARTIAL vs PASS (structural only)
- Org-overlay commands (host workspace, not this repo)
- Full-catalog manual walks (release checklist only)

---

## Phase 1 sign-off

See [ROADMAP.md — Phase 1](ROADMAP.md#phase-1--plan-next). Complete when:

- [x] [EVAL_INVENTORY.md](EVAL_INVENTORY.md) merged
- [x] This document merged
- [x] CI scope and failure contract agreed (this doc)
- [x] v1.0 blocker confirmed (above)
- [ ] Label `eval-ci-phase1-done` on the sign-off PR or close tracking issue

Phase 2 is live on `main` with `--strict` in CI.

**Branch protection:** Mark the **Eval fixtures** workflow as a required check (Settings → Branches → `main`).

---

## Maintaining inventory

Regenerate case classification after changing `cases.md` or `ship_gate`:

```bash
python3 scripts/inventory-eval-cases.py --write docs/EVAL_INVENTORY.md
```

Commit the updated `EVAL_INVENTORY.md` with the behavior change PR.
