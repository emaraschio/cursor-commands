# Changelog

All notable changes to this project are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- **`/git-sync-workspace`** — slash command and skill to sync git repos in a Cursor multi-root workspace to remote default (`fetch --all --prune`, checkout default, `pull --ff-only`); skips dirty or unsafe repos; eval ship gate **A, S**; catalog 30 → 31 commands/skills.

## [1.1.0] - 2026-05-29

### Added

- **`/scoped-audit`** — slash command and skill for scoped, plan-first parallel audits of large surfaces (capped subagent fan-out, verify-before-report, approval gate before any change); eval ship gate **A, S**; catalog 29 → 30 commands/skills.
- **`/agent-risk-review`** — slash command and skill for one-page agent permission briefs (allowed, approval-required, forbidden, limits, logging, rollback, first-week test plan); eval ship gate **A, S**; catalog 28 → 29 commands/skills.

## [1.0.0] - 2026-05-25

First stable public release of the generic cursor-commands catalog.

### Added

- **Release CI** — `.github/workflows/release.yml` runs full verification and publishes GitHub Releases from `CHANGELOG.md` on `v*` tags.
- **v1.0 sign-off** — manual verification record in [docs/VERIFICATION.md](docs/VERIFICATION.md).

### Changed

- **Public launch** — repository visibility public; `main` branch protection requires `validate`, `docs`, `install-smoke`, `eval-fixtures`.
- **`requirement-to-implementation` SKILL** — host-agnostic verification wording (no Rails-specific test commands); generic exploration risk examples.
- **CI on `main`** — all four workflows run on every push to `main` (PRs keep path filters for speed).
- **Docs** — README/CONTRIBUTING/ROADMAP/PUBLISHING/EVAL_CI reflect stable v1.0; org-string attestation for launch.

### Notes

- Consumers on pre-`v0.2.x` clones: re-fetch after history rewrite; pin **`v1.0.0`** for merge-mode install and full eval fixture coverage.
- `merge-open-prs` sections **B–F** remain **manual-only** eval (8 Setup/H rows waived in CI); ship gate **A, D, E** are structural in CI.

## [0.3.2] - 2026-05-24

### Added

- **`/requirement-to-implementation`** thin slash command and eval tree (`eval/cases.md`, `fixtures.yaml`); closes skill-only gap (28 commands, 28 skills, 1:1 catalog).
- **`SECURITY.md`** — vulnerability reporting scope for this prompt catalog.
- **GitHub templates** — `ISSUE_TEMPLATE/bug_report.yml`, `feature_request.yml`, `config.yml`, `pull_request_template.md`.

### Changed

- `EXPECTED_COMMANDS` 27 → 28 in validator and install script.
- `scripts/bootstrap-fixtures.py` — `REQUIREMENT_TO_IMPLEMENTATION_CASES` overrides for plan-before-implement ship gate.

## [0.3.1] - 2026-05-24

### Changed

- **Breaking (install default):** `scripts/install.sh` now uses **merge mode** by default — it no longer `rm -rf` entire `~/.cursor/commands` or `skills` trees. Host overlays and user files are preserved. Use `./scripts/install.sh --replace` for the previous wipe-then-install behavior.
- Catalog symlink validation checks only managed entries (broken host overlay symlinks no longer fail install).

### Added

- `scripts/install.sh --prune` — remove stale symlinks that point into this repo but left the catalog.
- `scripts/test_install.sh` — merge/replace/prune tests; run in `install-smoke` CI.

## [0.3.0] - 2026-05-24

### Added

- **Eval CI (Phase 2):** `scripts/eval_lib.py`, `scripts/run-eval-fixtures.py`, `scripts/bootstrap-fixtures.py`, `scripts/test_eval_lib.py`.
- `.github/workflows/eval-fixtures.yml` — structural ship-gate checks (`--strict`) on PRs touching commands/skills.
- `eval/fixtures.yaml` for all 27 commands (86 automated ship-gate rows; 8 Setup/H cases manual-only on `merge-open-prs`).

### Changed

- `validate-cursor-commands.py` — ship gate section binding and COMMANDS_INDEX consistency.
- `merge-open-prs` case A3 — added missing `**FAIL if:**` rubric line.

## [0.2.3] - 2026-05-24

### Changed

- Docs and git history scrubbed: no organization-specific trademarks or URLs in tree or commits.
- Docs CI: forbidden-string check; link-check config simplified.

## [0.2.2] - 2026-05-24

### Fixed

- Docs CI and `ROADMAP.md` release table (`v0.2.1` entry).

## [0.2.1] - 2026-05-24

### Removed

- Git history rewritten (`git filter-repo`): org-scoped command paths and bootstrap script no longer appear in any commit. **Force-reclone** or reset if you pinned an older SHA.

## [0.2.0] - 2026-05-24

### Changed

- **Breaking:** Org-scoped commands and skills removed from this repo (27 generic commands, 28 skills). Host workspaces install an overlay.
- Domain-specific `security-review` moved to host extension pack.

### Added

- [docs/ROADMAP.md](docs/ROADMAP.md) — public launch and v1.0 criteria

## [0.1.3] - 2026-05-24

### Changed

- Docs: no private host-repo URLs; portable `VERIFICATION.md`
- Validator scans `docs/`, `README.md`, `CONTRIBUTING.md`

## [0.1.2] - 2026-05-24

### Fixed

- README: correct submodule init for parent repos
- CI: install-smoke workflow planning; link-check ignores for private repos

## [0.1.1] - 2026-05-24

### Fixed

- `install.sh`: remove broken `commands`/`skills` symlinks before `mkdir`

## [0.1.0] - 2026-05-24

### Added

- Initial catalog: commands, skills, manual evals, validator, CI workflows
