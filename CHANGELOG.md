# Changelog

All notable changes to this project are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [1.4.0] - 2026-06-30

### Added

- **User plugin packaging**: `.cursor-plugin/plugin.json` and `.cursor-plugin/marketplace.json` bundle `.cursor/commands` and `.cursor/skills` via materialized `plugin/` (no `.git`; avoids fsmonitor socket copy failures on folder install). [docs/PLUGIN.md](docs/PLUGIN.md) documents GitHub URL and folder install, mobile smoke, cache cleanup, and `scripts/sync-plugin-package.sh`. Validator checks manifest paths, semver, and package sync.
- **`/thermo-nuclear-code-quality-review`**: slash command and skill for an extremely strict maintainability review that hunts for code-judo simplifications, guards the 1000-line file threshold, and blocks spaghetti-condition growth without changing behavior; explicit invocation only; eval ship gate **A, S**; catalog 36 → 37 commands/skills.

### Changed

- **Anti-patterns as enforced contract**: catalog-wide `Trigger / Wrong / Correct / Reason` shape in skills; `skill_required` anchors in `eval/fixtures.yaml`; CI fails if guards regress ([#22](https://github.com/emaraschio/cursor-commands/pull/22)).
- **README.md**: user plugin package, `sync-plugin-package.sh`, and anti-patterns contract ([#21](https://github.com/emaraschio/cursor-commands/pull/21), [#24](https://github.com/emaraschio/cursor-commands/pull/24)).
- **CONTRIBUTING.md**: plugin manifest and sync workflow for contributors.
- **CI**: `actions/checkout` v6 → v7 ([#20](https://github.com/emaraschio/cursor-commands/pull/20)).

### Fixed

- **Plugin folder install**: marketplace `"source": "plugin"` and materialized `plugin/` tree so Customize folder picker does not copy `.git/fsmonitor--daemon.ipc`.
- **Plugin package**: exclude host `merge-open-prs` profiles from synced `plugin/` tree.

## [1.3.0] - 2026-06-21

### Added

- **`/tdd`**: slash command and skill for Canon test-driven development (specify, encode, fulfill): clarify specifications, one failing test per cycle, minimal code to green, approval gates, kitchen-cleaning refactor rule, inline light review; RSpec examples in skill appendix; eval ship gate **A, S**; catalog 33 → 34 commands/skills.
- **`/agent-work-receipt`**: slash command and skill for a conservative six-section receipt of completed agent-assisted work (output, time, review, risk, value); eval ship gate **A, S**; catalog 34 → 35 commands/skills.
- **`/structure-prompt`**: slash command and skill to turn a rough request into a structured, production-grade prompt (verification, structured detail, constraints, structure, search priority, internal-first); eval ship gate **A, S**; catalog 35 → 36 commands/skills.

### Changed

- **README.md**: document GitHub repository topics for discoverability.
- **`.gitignore`**: ignore local `.cursor/plans/` and `merge-open-prs/profiles/` overlays.

## [1.2.0] - 2026-06-03

### Added

- **`/prompt-eval-debug`**: slash command and skill to debug any prompt via a tiny eval suite (control, edge, capability-boundary), failure diagnosis (prompt vs missing tool vs harness), and smallest next change without blind rewrite; eval ship gate **A, S**; catalog 32 → 33 commands/skills.
- **`/define-agent-goal`**: slash command and skill to draft a six-part agent Goal (outcome, verification, constraints, boundaries, iteration policy, stopping condition); plan-only, no same-turn execution; eval ship gate **A, S**; catalog 31 → 32 commands/skills.
- **`/git-sync-workspace`**: slash command and skill to sync git repos in a Cursor multi-root workspace to remote default (`fetch --all --prune`, checkout default, `pull --ff-only`); skips dirty or unsafe repos; eval ship gate **A, S**; catalog 30 → 31 commands/skills.

### Changed

- **CONTRIBUTING.md**: open source catalog section (generic examples, portable references, PR checklist).
- **EVAL_GUIDE.md**: ad-hoc prompt debugging section linking `/prompt-eval-debug` to catalog eval maintenance.

## [1.1.0] - 2026-05-29

### Added

- **`/scoped-audit`**: slash command and skill for scoped, plan-first parallel audits of large surfaces (capped subagent fan-out, verify-before-report, approval gate before any change); eval ship gate **A, S**; catalog 29 → 30 commands/skills.
- **`/agent-risk-review`**: slash command and skill for one-page agent permission briefs (allowed, approval-required, forbidden, limits, logging, rollback, first-week test plan); eval ship gate **A, S**; catalog 28 → 29 commands/skills.

## [1.0.0] - 2026-05-25

First stable public release of the generic cursor-commands catalog.

### Added

- **Release CI**: `.github/workflows/release.yml` runs full verification and publishes GitHub Releases from `CHANGELOG.md` on `v*` tags.
- **v1.0 sign-off**: manual verification record in [docs/VERIFICATION.md](docs/VERIFICATION.md).

### Changed

- **Public launch**: repository visibility public; `main` branch protection requires `validate`, `docs`, `install-smoke`, `eval-fixtures`.
- **`requirement-to-implementation` SKILL**: host-agnostic verification wording (no Rails-specific test commands); generic exploration risk examples.
- **CI on `main`**: all four workflows run on every push to `main` (PRs keep path filters for speed).
- **Docs**: README/CONTRIBUTING/ROADMAP/PUBLISHING/EVAL_CI reflect stable v1.0; org-string attestation for launch.

### Notes

- Consumers on pre-`v0.2.x` clones: re-fetch after history rewrite; pin **`v1.0.0`** for merge-mode install and full eval fixture coverage.
- `merge-open-prs` sections **B to F** remain **manual-only** eval (8 Setup/H rows waived in CI); ship gate **A, D, E** are structural in CI.

## [0.3.2] - 2026-05-24

### Added

- **`/requirement-to-implementation`** thin slash command and eval tree (`eval/cases.md`, `fixtures.yaml`); closes skill-only gap (28 commands, 28 skills, 1:1 catalog).
- **`SECURITY.md`**: vulnerability reporting scope for this prompt catalog.
- **GitHub templates**: `ISSUE_TEMPLATE/bug_report.yml`, `feature_request.yml`, `config.yml`, `pull_request_template.md`.

### Changed

- `EXPECTED_COMMANDS` 27 → 28 in validator and install script.
- `scripts/bootstrap-fixtures.py`: `REQUIREMENT_TO_IMPLEMENTATION_CASES` overrides for plan-before-implement ship gate.

## [0.3.1] - 2026-05-24

### Changed

- **Breaking (install default):** `scripts/install.sh` now uses **merge mode** by default: it no longer `rm -rf` entire `~/.cursor/commands` or `skills` trees. Host overlays and user files are preserved. Use `./scripts/install.sh --replace` for the previous wipe-then-install behavior.
- Catalog symlink validation checks only managed entries (broken host overlay symlinks no longer fail install).

### Added

- `scripts/install.sh --prune`: remove stale symlinks that point into this repo but left the catalog.
- `scripts/test_install.sh`: merge/replace/prune tests; run in `install-smoke` CI.

## [0.3.0] - 2026-05-24

### Added

- **Eval CI (Phase 2):** `scripts/eval_lib.py`, `scripts/run-eval-fixtures.py`, `scripts/bootstrap-fixtures.py`, `scripts/test_eval_lib.py`.
- `.github/workflows/eval-fixtures.yml`: structural ship-gate checks (`--strict`) on PRs touching commands/skills.
- `eval/fixtures.yaml` for all 27 commands (86 automated ship-gate rows; 8 Setup/H cases manual-only on `merge-open-prs`).

### Changed

- `validate-cursor-commands.py`: ship gate section binding and COMMANDS_INDEX consistency.
- `merge-open-prs` case A3: added missing `**FAIL if:**` rubric line.

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

- [docs/ROADMAP.md](docs/ROADMAP.md): public launch and v1.0 criteria

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
