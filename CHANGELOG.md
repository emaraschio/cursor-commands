# Changelog

All notable changes to this project are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

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
