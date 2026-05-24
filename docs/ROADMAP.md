# Roadmap

Public OSS trajectory for **cursor-commands** (generic slash commands + skills + manual evals). organization-specific–specific commands were moved to host workspaces (e.g. private dotfiles overlay) as of **v0.2.0**.

## Released

| Tag | Milestone |
|-----|-----------|
| `v0.1` | Initial 32-command tree, validator, CI |
| `v0.1.1` | Install: fix broken `~/.cursor` symlinks before `mkdir` |
| `v0.1.2` | CI: submodule + link-check fixes |
| `v0.1.3` | OSS-portable docs (no private host-repo URLs) |
| `v0.2.0` | **Generic-only catalog** (27 commands, 28 skills); extension pack external |
| `v0.2.1` | History rewrite: org-scoped paths purged from all commits; `docs/PUBLISHING.md` |

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
| organization-specific slash commands | Host workspace overlay (e.g. dotfiles `.cursor/commands/`) |
| `benchmark-rules`, HIPAA `security-review` | Host workspace `.cursor/skills/` |
| Cursor **rules**, **agents**, **memory-bank** | Host workspace (IDE root repo) |
| `character.mdc` / `ai-engineer.mdc` | Consumer rules repos |

**Planned org home (TBD):** `organization-specific/dev-tools` on GitHub — org-scoped commands/skills will likely migrate out of private dotfiles into that repo (not created yet).

## Open decisions

1. **Public timing** — flip visibility when v1.0 checklist is complete; org-scoped paths must be absent from history ([PUBLISHING.md](PUBLISHING.md))
2. **Org pack migration** — dotfiles overlay → `organization-specific/dev-tools` (timing TBD)
3. **`requirement-to-implementation`** — add thin `/requirement-to-implementation` command or keep skill-only

## How to use this doc

Update checkboxes when milestones land. Bump `CHANGELOG.md` and tag semver on each release (`v0.x` pre-1.0, `v1.0.0` when launch criteria are met).
