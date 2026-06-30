# Roadmap

Public OSS trajectory for **cursor-commands** (generic slash commands + skills + behavioral eval rubrics). Organization-specific commands belong in the **host workspace** that installs this pack (overlay after `./scripts/install.sh`).

## Current state (honest)

| Layer | What runs today | Gap |
|-------|-----------------|-----|
| **Structure** | `validate-cursor-commands.py` in CI: layout, frontmatter, ship_gate binding | Does not score agent behavior |
| **Install** | `install-smoke.yml`: merge/replace/prune + symlink resolve | Does not exercise agents in IDE |
| **Docs** | `docs.yml`: links, forbidden org strings, required files | Does not read eval case semantics |
| **Ship gate** | [eval-fixtures.yml](../.github/workflows/eval-fixtures.yml) `--strict` on ship-gate rows | Structural only; PARTIAL/FAIL scoring is manual |
| **Release** | [release.yml](../.github/workflows/release.yml) on `v*` tags | No LLM regression in CI |

**Risk:** Ship-gate CI can pass while agent behavior regresses on non-gate sections or edge cases. PR authors must still walk ship gate sections when changing `SKILL.md`; record manual IDE smoke per [VERIFICATION.md](VERIFICATION.md) on releases.

---

## Priority track: eval enforcement in CI

**Goal:** Make ship gate sections a **merge blocker** in GitHub Actions (without running an LLM on every case in v1).

Work in two explicit phases: **plan**, then **execute**. Do not skip planning.

### Phase 1: Plan (complete)

Deliverables before writing the runner or workflow:

- [x] **Inventory** ([docs/EVAL_INVENTORY.md](EVAL_INVENTORY.md)): 28 commands, 98 ship-gate rows (S1 to S5 vs H, `fixture_ready`). Regenerate via `scripts/inventory-eval-cases.py`.
- [x] **Fixture model**: Full-structural v1 in [docs/EVAL_CI.md](EVAL_CI.md) (`fixtures.yaml`, S5 algorithm, global checks).
- [x] **CI scope**: `eval-fixtures.yml` on PR/push when `.cursor/commands/**` or `.cursor/skills/**` change; `workflow_dispatch` for full catalog.
- [x] **Failure contract**: `FAIL <command> <case_id> <check_id> <message>`; stable `check_id` enum in EVAL_CI.md.
- [x] **Non-goals (v1)**: No LLM judge; non-gate sections manual; no org-overlay commands here.
- [x] **v1.0 gate**: **Eval CI Phase 2 is a hard blocker** for public launch (soft exception for private submodule pins documented in EVAL_CI.md).

**Plan sign-off:** Docs-only PR with `EVAL_CI.md` + `EVAL_INVENTORY.md` + inventory script. Label `eval-ci-phase1-done` when merged. **Do not** add `run-eval-fixtures.yml` until Phase 2.

### Phase 2: Execute (complete)

1. [x] `scripts/run-eval-fixtures.py`: ship-gate structural checks (S1, S3 to S5 via `fixtures.yaml`).
2. [x] `scripts/eval_lib.py`: shared parsing; `scripts/test_eval_lib.py` unit tests.
3. [x] Extended `validate-cursor-commands.py`: S2 section binding + COMMANDS_INDEX ship gate match.
4. [x] `.github/workflows/eval-fixtures.yml`: `--strict` mode; add as **required check** in branch protection (manual).
5. [x] `scripts/bootstrap-fixtures.py`: regenerate `eval/fixtures.yaml` for all 28 commands (90 fixture rows; 8 H/Setup waived).
6. [x] Tag **`v0.3.0`** on merge.

**Execute done when:** A PR that removes a ship-gate requirement from `SKILL.md` without updating fixtures **fails** CI.

---

## Released

| Tag | Milestone |
|-----|-----------|
| `v0.1` | Initial command tree, validator, CI |
| `v0.1.1` | Install: fix broken `~/.cursor` symlinks before `mkdir` |
| `v0.1.2` | CI: submodule + link-check fixes |
| `v0.1.3` | OSS-portable docs (no private host-repo URLs) |
| `v0.2.0` | **Generic-only catalog** (27 commands, 28 skills); org extensions external |
| `v0.2.1` | History rewrite: org-scoped paths purged from all commits; `docs/PUBLISHING.md` |
| `v0.2.2` | Docs CI and roadmap release-table fixes |
| `v0.2.3` | Org strings scrubbed from tree and history; trademark check in CI |
| `v0.2.x` | [COMMANDS_INDEX.md](../.cursor/docs/COMMANDS_INDEX.md) ship gate legend |
| `v0.3.0` | **Eval CI Phase 2:** `eval-fixtures.yml`, `fixtures.yaml` for 27 commands, `--strict` runner |
| `v0.3.1` | **Install merge mode** (default); `--replace`, `--prune`; `test_install.sh` in CI |
| `v0.3.2` | **`/requirement-to-implementation`** command + eval tree; `SECURITY.md`; issue/PR templates |
| `v1.0.0` | **Stable public launch**: full `main` CI matrix, release workflow, RTI skill genericized, verification sign-off |

## v1.0.0: public launch (complete)

Exit criteria:

- [x] **Eval CI track Phase 2 complete** (ship gate fixtures block PRs; see [Priority track](#priority-track-eval-enforcement-in-ci))
- [x] Repository visibility **public** ([PUBLISHING.md §3](PUBLISHING.md#3-make-the-repository-public))
- [x] `CHANGELOG.md` kept from `v0.2.0` onward
- [x] README version banner matches latest tag (`v1.0.0`)
- [x] All CI workflows green without private-repo link-check ignores
- [x] `docs/VERIFICATION.md` manual smoke test documented and run for `v1.0.0` (see release record table)
- [x] Install **merge mode** (default): symlink only this repo’s files; do not `rm -rf` entire `~/.cursor/commands` or `skills` (see [Install UX](#install-ux))
- [x] `docs/DEPENDENCIES.md` for `gh`, babysit, optional Docker
- [x] Deprecated commands removed or moved to `archive/`: none in catalog; N/A
- [x] No organization trademarks or private org URLs in tree or git history ([PUBLISHING.md §1](PUBLISHING.md#1-purge-org-specific-content-from-git-history); re-verified 2026-05-25)

Shipped in v1.0.0:

- [x] GitHub issue + PR templates, `SECURITY.md`
- [x] Release workflow on tag ([release.yml](../.github/workflows/release.yml))
- [x] All four CI workflows on every push to `main`

## v1.x: after launch

### Install UX

Shipped in `v0.3.1`.

- **Default:** merge (`mkdir -p` and symlink catalog entries only); foreign files and non-repo symlinks preserved
- **`--replace`:** remove `commands/` and `skills/` trees first (legacy full reset)
- **`--prune`:** drop stale symlinks that still point into this repo but left the catalog
- Host **overlay:** install generic (`install.sh`), then org-specific symlinks from the host workspace (see dotfiles `install-cursor-commands.sh`)

### Evaluations (later)

- **Recorded agent runs** or sampled manual regression: optional; not required for v1.0 eval CI
- **Full-catalog periodic walk**: release checklist, not per-PR

### External dependencies

- `/merge-open-prs` → user-global **babysit** at `~/.cursor/skills-cursor/babysit/SKILL.md`
- Options: document only, optional submodule, or minimal inlined contract (trade-off: duplication)

## Out of scope (this repo)

| Item | Where it lives |
|------|----------------|
| Org-scoped slash commands | Host workspace overlay (`.cursor/commands/` in the repo you open in Cursor) |
| Org-scoped skills (benchmarks, domain security review, etc.) | Host workspace `.cursor/skills/` |
| Cursor **rules**, **agents**, **memory-bank** | Host workspace (IDE root repo) |
| Custom rule files (`*.mdc`) | Consumer rules repos |

**Planned org home (TBD):** separate host-org extension repository; timing TBD (not in this generic catalog).

## Open decisions

1. ~~**Eval CI before public?**~~ Resolved: Phase 2 shipped; repo public at v1.0.0.
2. ~~**Public timing**~~. Resolved: v1.0.0 (2026-05-25).
3. **Org extension packaging**: host overlay vs. separate extension repository (timing TBD; post-v1.0). **User plugin** for generic catalog shipped in **v1.4.0** (`docs/PLUGIN.md`); marketplace submission TBD.

## How to use this doc

1. **Phases 1 and 2** complete: `docs/EVAL_CI.md`, `docs/EVAL_INVENTORY.md`, `eval-fixtures.yml`.
2. Enable **Eval fixtures** as a required GitHub check on `main`.
3. Bump [CHANGELOG.md](../CHANGELOG.md) and tag semver on each release (`v*`; only **`v1.0.0`** published today; older pre-release tags removed from remote).
