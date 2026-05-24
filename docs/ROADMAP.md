# Roadmap

Public OSS trajectory for **cursor-commands** (generic slash commands + skills + manual evals). Organization-specific commands belong in the **host workspace** that installs this pack (overlay after `./scripts/install.sh`).

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

## v1.0.0 — public launch (next)

Exit criteria (all required):

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
- [ ] Release workflow on tag (validate + install-smoke + notes from `CHANGELOG.md`)
- [ ] Validate workflow on every push to `main` (not only `.cursor/**` path filters)

## v1.x — quality and ergonomics

### Install UX

Today `scripts/install.sh` replaces the entire `commands/` and `skills/` directories. Planned:

- **Default:** merge — symlink only files from this repo
- **`--replace`:** current behavior for users who own the whole tree
- Document host **overlay** pattern (install generic, then org-specific symlinks)

### Evaluations

- **v0.1:** manual walks only (`EVAL_GUIDE.md`)
- **v1.x:** `scripts/run-eval-fixtures.py` — structural checks on ship-gate cases (no LLM-in-CI)
- **Later:** optional recorded agent runs; not a v1.0 blocker

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

## Open decisions

1. **Public timing** — flip visibility when v1.0 checklist is complete ([PUBLISHING.md](PUBLISHING.md))
2. **Org extension packaging** — host overlay vs. separate extension repository (timing TBD)
3. **`requirement-to-implementation`** — add thin `/requirement-to-implementation` command or keep skill-only

## How to use this doc

Update checkboxes when milestones land. Bump `CHANGELOG.md` and tag semver on each release (`v0.x` pre-1.0, `v1.0.0` when launch criteria are met).
