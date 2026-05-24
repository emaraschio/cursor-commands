# Roadmap

Public OSS trajectory for **cursor-commands** (generic slash commands + skills + behavioral eval rubrics). Organization-specific commands belong in the **host workspace** that installs this pack (overlay after `./scripts/install.sh`).

## Current state (honest)

| Layer | What runs today | Gap |
|-------|-----------------|-----|
| **Structure** | `validate-cursor-commands.py` in CI — command/skill/eval file layout, frontmatter, ship_gate present | Does not score behavior |
| **Install** | `install-smoke.yml` — symlinks resolve | Does not exercise agents |
| **Docs** | `docs.yml` — links, forbidden org strings | Does not read eval cases |
| **Ship gate** | Documented in [COMMANDS_INDEX.md](../.cursor/docs/COMMANDS_INDEX.md) and [EVAL_GUIDE.md](../.cursor/docs/EVAL_GUIDE.md) | **Honored only if a human runs manual walks** — easy to ignore on PRs |

**Risk:** We can merge prompt changes with **0 FAIL** on ship gate sections and CI stays green. Until eval enforcement lands in CI, treat every `SKILL.md` / command change as **ship gate debt** unless the PR author records a manual walk.

---

## Priority track — eval enforcement in CI

**Goal:** Make ship gate sections a **merge blocker** in GitHub Actions (without running an LLM on every case in v1).

Work in two explicit phases: **plan**, then **execute**. Do not skip planning.

### Phase 1 — Plan (complete)

Deliverables before writing the runner or workflow:

- [x] **Inventory** — [docs/EVAL_INVENTORY.md](EVAL_INVENTORY.md): 27 commands, 94 ship-gate rows (S1–S5 vs H, `fixture_ready`). Regenerate via `scripts/inventory-eval-cases.py`.
- [x] **Fixture model** — Full-structural v1 in [docs/EVAL_CI.md](EVAL_CI.md) (`fixtures.yaml`, S5 algorithm, global checks).
- [x] **CI scope** — Documented: `eval-fixtures.yml` on PR/push when `.cursor/commands/**` or `.cursor/skills/**` change; `workflow_dispatch` for full catalog.
- [x] **Failure contract** — `FAIL <command> <case_id> <check_id> <message>`; stable `check_id` enum in EVAL_CI.md.
- [x] **Non-goals (v1)** — No LLM judge; non-gate sections manual; no org-overlay commands here.
- [x] **v1.0 gate** — **Eval CI Phase 2 is a hard blocker** for public launch (soft exception for private submodule pins documented in EVAL_CI.md).

**Plan sign-off:** Docs-only PR with `EVAL_CI.md` + `EVAL_INVENTORY.md` + inventory script. Label `eval-ci-phase1-done` when merged. **Do not** add `run-eval-fixtures.yml` until Phase 2.

### Phase 2 — Execute (after plan sign-off)

Implementation order:

1. [ ] `scripts/run-eval-fixtures.py` — structural checks for **ship gate sections only** (read `eval.ship_gate` from command frontmatter).
2. [ ] Extend `validate-cursor-commands.py` — assert every `ship_gate` id exists as `## Section <id>` in `cases.md`; every ship-gate case has PASS/PARTIAL/FAIL rubric lines.
3. [ ] `.github/workflows/eval-fixtures.yml` — run on PR + push to `main` when eval-related paths change; required check on PRs.
4. [ ] Wire into contributor docs — [CONTRIBUTING.md](../CONTRIBUTING.md) PR checklist: CI runs ship-gate fixtures; manual full walk still recommended for non-gate sections.
5. [ ] Backfill fixtures for **high-risk** commands first (`merge-open-prs`, `commit`, `commit-changes-main`, `create-pr-main`) then remainder.
6. [ ] Tag release (e.g. `v0.3.0`) when all commands have ship-gate fixtures and workflow is required on PRs.

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

## v1.0.0 — public launch

Exit criteria (all required):

- [ ] **Eval CI track Phase 2 complete** (ship gate fixtures block PRs — see [Priority track](#priority-track--eval-enforcement-in-ci))
- [ ] Repository visibility **public**
- [ ] `CHANGELOG.md` kept from `v0.2.0` onward
- [ ] README version banner matches latest tag
- [ ] All CI workflows green without private-repo link-check ignores (drop self-repo ignore in `.markdown-link-check.json` when public)
- [ ] `docs/VERIFICATION.md` manual smoke test documented and run once per release
- [ ] Install **merge mode** (default): symlink only this repo’s files; do not `rm -rf` entire `~/.cursor/commands` or `skills` (see [Install UX](#install-ux))
- [ ] `docs/DEPENDENCIES.md` for `gh`, babysit, optional Docker
- [ ] Deprecated commands removed or moved to `archive/` (none in generic catalog today)
- [ ] No organization trademarks or private org URLs in tree or git history ([PUBLISHING.md](PUBLISHING.md))

Nice-to-have before or shortly after v1.0:

- [ ] GitHub issue + PR templates, `SECURITY.md`
- [ ] Release workflow on tag (validate + install-smoke + eval-fixtures + notes from `CHANGELOG.md`)
- [ ] Validate workflow on every push to `main` (not only `.cursor/**` path filters)

## v1.x — after launch

### Install UX

Today `scripts/install.sh` replaces the entire `commands/` and `skills/` directories. Planned:

- **Default:** merge — symlink only files from this repo
- **`--replace`:** current behavior for users who own the whole tree
- Document host **overlay** pattern (install generic, then org-specific symlinks)

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
4. **`requirement-to-implementation`** — add thin `/requirement-to-implementation` command or keep skill-only

## How to use this doc

1. **Phase 1** is complete — see `docs/EVAL_CI.md` and `docs/EVAL_INVENTORY.md`.
2. Execute **Phase 2** (`run-eval-fixtures.py`, `eval-fixtures.yml`) after the Phase 1 sign-off PR merges.
3. Bump [CHANGELOG.md](../CHANGELOG.md) and tag semver on each release (`v0.x` pre-1.0, `v1.0.0` when launch criteria are met).
