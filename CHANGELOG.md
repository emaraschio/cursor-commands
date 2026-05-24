# Changelog

All notable changes to this project are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

## [0.2.0] - 2026-05-24

### Changed

- **Breaking:** organization-specific commands and skills removed from this repo (27 generic commands, 28 skills). Host workspaces install an overlay (e.g. dotfiles `.cursor/commands/` + `.cursor/skills/`).
- `security-review` moved with extension pack (HIPAA-specific; was misleadingly tagged `generic`).

### Added

- [docs/ROADMAP.md](docs/ROADMAP.md) — public launch and v1.0 criteria

## [0.1.3] - 2026-05-24

### Changed

- Docs: no private dotfiles URLs; portable `VERIFICATION.md`
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
