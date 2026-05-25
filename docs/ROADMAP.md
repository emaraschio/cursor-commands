# Roadmap

Public OSS trajectory for **cursor-commands** (generic slash commands + skills + behavioral eval rubrics). Organization-specific commands belong in the **host workspace** that installs this pack (overlay after `./scripts/install.sh`).

## Current state (honest)

| Layer | What runs today | Gap |
|-------|-----------------|-----|
| **Structure** | `validate-cursor-commands.py` in CI — command/skill/eval file layout, frontmatter, ship_gate present | Does not score behavior |
| **Install** | `install-smoke.yml` — symlinks resolve | Does not exercise agents |
| **Docs** | `docs.yml` — links, forbidden org strings | Does not read eval cases |
| **Ship gate** | [eval-fixtures.yml](../.github/workflows/eval-fixtures.yml) + manual walks for non-gate sections | Structural S1–S5 enforced in CI when `fixtures.yaml` present |

**Risk:** We can merge prompt changes with **0 FAIL** on ship gate sections and CI stays green. Until eval enforcement lands in CI, treat every `SKILL.md` / command change as **ship gate debt** unless the PR author records a manual walk.

---

## Priority track — eval enforcement in CI

**Goal:** Make ship gate sections a **merge blocker** in GitHub Actions (without running an LLM on every case in v1).

Work in two explicit phases: **plan**, then **execute**. Do not skip planning.

### Phase 1 — Plan (complete)

Deliverables before writing the runner or workflow:

- [x] **Inventory** — [docs/EVAL_INVENTORY.md](EVAL_INVENTORY.md): 28 commands, 98 ship-gate rows (S1–S5 vs H, `fixture_ready`). Regenerate via `scripts/inventory-eval-cases.py`.
- [x] **Fixture model** — Full-structural v1 in [docs/EVAL_CI.md](EVAL_CI.md) (`fixtures.yaml`, S5 algorithm, global checks).
- [x] **CI scope** — Documented: `eval-fixtures.yml` on PR/push when `.cursor/commands/**` or `.cursor/skills/**` change; `workflow_dispatch` for full catalog.
- [x] **Failure contract** — `FAIL <command> <case_id> <check_id> <message>`; stable `check_id` enum in EVAL_CI.md.
- [x] **Non-goals (v1)** — No LLM judge; non-gate sections manual; no org-overlay commands here.
- [x] **v1.0 gate** — **Eval CI Phase 2 is a hard blocker** for public launch (soft exception for private submodule pins documented in EVAL_CI.md).

**Plan sign-off:** Docs-only PR with `EVAL_CI.md` + `EVAL_INVENTORY.md` + inventory script. Label `eval-ci-phase1-done` when merged. **Do not** add `run-eval-fixtures.yml` until Phase 2.

### Phase 2 — Execute (complete)

1. [x] `scripts/run-eval-fixtures.py` — ship-gate structural checks (S1, S3–S5 via `fixtures.yaml`).
2. [x] `scripts/eval_lib.py` — shared parsing; `scripts/test_eval_lib.py` unit tests.
3. [x] Extended `validate-cursor-commands.py` — S2 section binding + COMMANDS_INDEX ship gate match.
4. [x] `.github/workflows/eval-fixtures.yml` — `--strict` mode; add as **required check** in branch protection (manual).
5. [x] `scripts/bootstrap-fixtures.py` — regenerate `eval/fixtures.yaml` for all 28 commands (90 fixture rows; 8 H/Setup waived).
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

## v1.0.0 — public launch

Exit criteria (all required):

- [x] **Eval CI track Phase 2 complete** (ship gate fixtures block PRs — see [Priority track](#priority-track--eval-enforcement-in-ci))
- [x] Repository visibility **public** ([PUBLISHING.md §3](PUBLISHING.md#3-make-the-repository-public))
- [x] `CHANGELOG.md` kept from `v0.2.0` onward
- [x] README version banner matches latest tag (`v0.3.2`)
- [x] All CI workflows green without private-repo link-check ignores
- [ ] `docs/VERIFICATION.md` manual smoke test documented and run once per release
- [x] Install **merge mode** (default): symlink only this repo’s files; do not `rm -rf` entire `~/.cursor/commands` or `skills` (see [Install UX](#install-ux))
- [x] `docs/DEPENDENCIES.md` for `gh`, babysit, optional Docker
- [ ] Deprecated commands removed or moved to `archive/` (none in generic catalog today)
- [ ] No organization trademarks or private org URLs in tree or git history ([PUBLISHING.md](PUBLISHING.md))

Nice-to-have before or shortly after v1.0:

- [x] GitHub issue + PR templates, `SECURITY.md`
- [ ] Release workflow on tag (validate + install-smoke + eval-fixtures + notes from `CHANGELOG.md`)
- [ ] Validate workflow on every push to `main` (not only `.cursor/**` path filters)

## v1.x — after launch

### Install UX

Shipped in `v0.3.1`.

- **Default:** merge — `mkdir -p` and symlink catalog entries only; foreign files and non-repo symlinks preserved
- **`--replace`:** remove `commands/` and `skills/` trees first (legacy full reset)
- **`--prune`:** drop stale symlinks that still point into this repo but left the catalog
- Host **overlay:** install generic (`install.sh`), then org-specific symlinks from the host workspace (see dotfiles `install-cursor-commands.sh`)

### Evaluations (later)

- **Recorded agent runs** or sampled manual regression — optional; not required for v1.0 eval CI
- **Full-catalog periodic walk** — release checklist, not per-PR

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

**Planned org home (TBD):** separate host-org extension repository — timing TBD (not in this generic catalog).

## Open decisions

1. **Eval CI before public?** — Default in this roadmap: **yes** (v1.0 blocked until Phase 2). Override only with explicit sign-off.
2. **Public timing** — after v1.0 checklist ([PUBLISHING.md](PUBLISHING.md))
3. **Org extension packaging** — host overlay vs. separate extension repository (timing TBD)
4. ~~**`requirement-to-implementation`**~~ — resolved in `v0.3.2` (thin command + eval tree)

## How to use this doc

1. **Phase 1–2** complete — `docs/EVAL_CI.md`, `docs/EVAL_INVENTORY.md`, `eval-fixtures.yml`.
2. Enable **Eval fixtures** as a required GitHub check; bump consumer submodule pins to `v0.3.0`.
3. Bump [CHANGELOG.md](../CHANGELOG.md) and tag semver on each release (`v0.x` pre-1.0, `v1.0.0` when launch criteria are met).
