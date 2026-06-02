# cursor-commands

[![Validate](https://github.com/emaraschio/cursor-commands/actions/workflows/validate.yml/badge.svg)](https://github.com/emaraschio/cursor-commands/actions/workflows/validate.yml)
[![Install smoke](https://github.com/emaraschio/cursor-commands/actions/workflows/install-smoke.yml/badge.svg)](https://github.com/emaraschio/cursor-commands/actions/workflows/install-smoke.yml)
[![Docs](https://github.com/emaraschio/cursor-commands/actions/workflows/docs.yml/badge.svg)](https://github.com/emaraschio/cursor-commands/actions/workflows/docs.yml)
[![Eval fixtures](https://github.com/emaraschio/cursor-commands/actions/workflows/eval-fixtures.yml/badge.svg)](https://github.com/emaraschio/cursor-commands/actions/workflows/eval-fixtures.yml)

**Stable release: [`v1.1.0`](CHANGELOG.md#110---2026-05-29)** — Generic Cursor slash commands, Agent Skills, and behavioral eval rubrics. Install from `main` or `git checkout v1.1.0`. Ship-gate sections are enforced in CI via [docs/EVAL_CI.md](docs/EVAL_CI.md). Organization-specific packs install from the **host workspace**.

Inspired by install ergonomics from [hamzafer/cursor-commands](https://github.com/hamzafer/cursor-commands); this repo adds **skills**, **eval rubrics**, and **structural ship-gate CI** (`run-eval-fixtures.py --strict`).

## What you get

- **32** generic slash commands (git, review, security audits, agent goals, agent risk review, scoped parallel audits, workspace git sync, PR workflows, requirement-to-implementation, etc.)
- **32** skill directories (one per command)
- **Behavioral evals** (`PASS` / `PARTIAL` / `FAIL`) per command — regression guardrails when editing prompts

## Installation

### Standalone clone

```bash
git clone https://github.com/emaraschio/cursor-commands.git
cd cursor-commands
chmod +x scripts/install.sh
./scripts/install.sh          # merge mode (default)
```

Commands and skills from this catalog are symlinked into `~/.cursor/commands/` and `~/.cursor/skills/`. **Merge mode (default)** keeps your own files and host overlays (org-specific commands installed afterward). Use `./scripts/install.sh --replace` only if you want to wipe those directories first. Use `--prune` to remove stale symlinks that still point into this repo after a catalog rename.

### As a Git submodule

If a parent repo (for example personal dotfiles) vendors this tree:

```bash
cd path/to/parent-repo
git submodule update --init path/to/cursor-commands
./path/to/cursor-commands/scripts/install.sh
```

The parent repo owns workspace-specific Cursor **rules**, **agents**, and **memory-bank** files. This repo only ships shared slash commands and skills.

### Custom Cursor home

```bash
CURSOR_HOME="$HOME/.cursor" ./scripts/install.sh

# Host overlay: install generic, then org-specific symlinks from your dotfiles (merge-safe).
```

## Architecture

```text
.cursor/commands/<name>.md   # thin slash entry (YAML frontmatter)
.cursor/skills/<name>/
  SKILL.md                   # full agent contract
  eval/
    cases.md                 # behavioral rubric
    README.md                # ship gate + how to score
```

Details: [COMMAND_SCHEMA.md](.cursor/docs/COMMAND_SCHEMA.md)

```mermaid
flowchart LR
  slash["/command"] --> cmd["commands/name.md"]
  cmd --> skill["skills/name/SKILL.md"]
  skill --> eval["eval/cases.md"]
```

## Catalog

Full table: [COMMANDS_INDEX.md](.cursor/docs/COMMANDS_INDEX.md)

| Highlight | Description |
|-----------|-------------|
| `/merge-open-prs` | Batch review, Docker verify, merge when green (limit 10) |
| `/code-review` | Thorough PR review before approval |

**External dependency:** `/merge-open-prs` expects the user-global **babysit** skill at `~/.cursor/skills-cursor/babysit/SKILL.md`.

**Org-specific commands** (domain scripts, onboarding, custom security review, rules benchmarks) are **not** in this repo — install them from your host workspace overlay. See [docs/ROADMAP.md](docs/ROADMAP.md).

## Evaluations

We treat prompts like code: editable contracts need reviewable tests.

- **Structural checks in CI** — no LLM judge on every PR (flaky, expensive); ship-gate rows use `fixtures.yaml`.
- Each command defines **ship gate** sections in frontmatter (e.g. `A`, `S`; merge-open-prs uses `A`, `D`, `E`).
- Scoring: `PARTIAL` counts as fail; target 0 `FAIL` on ship gate before merge.

How to run: [EVAL_GUIDE.md](.cursor/docs/EVAL_GUIDE.md)

Example flow:

1. Read only `skills/<name>/SKILL.md`.
2. For each case in `eval/cases.md`, draft the agent response.
3. Mark `PASS` / `PARTIAL` / `FAIL`.
4. Fix skill/command before push if any ship-gate case fails.

After install, optional IDE check: [docs/VERIFICATION.md](docs/VERIFICATION.md)

## Validation

```bash
python3 scripts/validate-cursor-commands.py
python3 scripts/run-eval-fixtures.py --strict
```

CI on `main` and PRs: **validate**, **docs**, **install-smoke**, **eval-fixtures** (see branch protection). New releases: push tag `v*` to run [release.yml](.github/workflows/release.yml).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security reports: [SECURITY.md](SECURITY.md).

## Related

- [Cursor slash commands docs](https://cursor.com/docs/agent/chat/commands)
- [hamzafer/cursor-commands](https://github.com/hamzafer/cursor-commands) — minimal command-only collection

## License

MIT — see [LICENSE](LICENSE).
