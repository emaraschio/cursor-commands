# External dependencies

Optional tools and skills referenced by this catalog. Install only what the commands you use require.

## Required for install

| Dependency | Used by | Notes |
|------------|---------|--------|
| `bash`, `python3` | `scripts/install.sh`, validators | CI uses Python 3.11+ |

## Command-specific (host machine)

| Dependency | Commands / skills | Notes |
|------------|-------------------|--------|
| [`gh`](https://cli.github.com/) | `merge-open-prs`, `create-pr-main`, `generate-pr-description`, `address-github-pr-comments`, `requirement-to-implementation` (issue intake) | Authenticate with `gh auth login` |
| **git** | `git-sync-workspace` | Discover repos, preflight, `fetch --all --prune`, checkout default, `pull --ff-only` |
| **babysit** skill | `merge-open-prs` | User-global: `~/.cursor/skills-cursor/babysit/SKILL.md` (not shipped in this repo) |
| **Docker** | `merge-open-prs` (default verify path) | `docker info` must succeed unless `--no-docker` |

## Host workspace (not in this repo)

| Item | Purpose |
|------|---------|
| Cursor IDE | Slash commands and skills |
| `.cursor/memory-bank/` | `update-memory-bank`, `requirement-to-implementation` context phases |
| Org overlay commands/skills | Domain workflows after `./scripts/install.sh` |

## CI (contributors)

GitHub Actions runs validate, docs (link check + forbidden strings), install-smoke, and eval-fixtures. No Docker or `gh` merge operations in CI.
