# Cursor IDE verification

Run after plugin install ([docs/PLUGIN.md](PLUGIN.md)) or `./scripts/install.sh` (merge mode by default). Automated checks run in CI via `install-smoke.yml` and `scripts/test_install.sh`; this doc covers manual IDE validation.

## Plugin smoke test (recommended)

1. Install via **Customize → Plugins → + Add** with `https://github.com/emaraschio/cursor-commands` (user scope).
2. Reload the window if needed.
3. Open agent chat; type `/` and confirm `/code-review` and `/commit-same-branch` appear.
4. Run **`/define-agent-goal`** on a small task; agent should deliver a plan-only Goal (no code edits in the same turn).
5. On **Cursor iOS** (same account): start an agent, confirm `/` lists catalog commands, run one lightweight command.

## Automated (install script)

The install script already verifies:

- 37 command symlinks and 37 skill symlinks
- Each symlink target resolves
- `validate-cursor-commands.py` passes
- `merge-open-prs` skill is reachable under `$CURSOR_HOME`

## Manual smoke test (symlink install)

1. **Restart Cursor** or reload the window (slash commands load from `~/.cursor/commands/` when using `install.sh`).
2. Open the slash command palette; confirm entries such as `/code-review` and `/commit-same-branch`.
3. Run **`/code-review`** on a small diff; the agent should read `~/.cursor/skills/code-review/SKILL.md`.
4. In a git repo with `gh` authenticated, run **`/merge-open-prs --dry-run`**; agent should follow the merge-open-prs skill and reference **babysit** at `~/.cursor/skills-cursor/babysit/SKILL.md` (install babysit separately if missing).
5. Optional: open any workspace that has a `.cursor/memory-bank/` directory and run **`/update-memory-bank`**; command and skill should resolve via the install symlinks (memory-bank content lives in the host repo, not in cursor-commands).

Record pass/fail in release notes when cutting a tag.

## Release record

| Tag | Date | Verifier | Result | Notes |
|-----|------|----------|--------|-------|
| v1.3.0 | 2026-06-21 | @emaraschio | PASS | Validator + eval fixtures green; 36/36 commands/skills. Palette: `/tdd`, `/structure-prompt`, `/agent-work-receipt` expected after Cursor reload. Manual IDE smoke not re-run. |
| v1.0.0 | 2026-05-25 | @emaraschio | PASS | Merge install: 28/28 symlinks; validator + eval fixtures green. Palette: `/code-review`, `/requirement-to-implementation` expected after Cursor reload. `/merge-open-prs --dry-run` not re-run (optional). |

## Merge mode (host overlay)

If you use a host overlay (e.g. org commands in dotfiles after generic install):

1. Run `./scripts/install.sh` (or your wrapper that calls it).
2. Confirm overlay commands still exist under `~/.cursor/commands/` alongside catalog entries.
3. Re-run install after a submodule bump; overlay symlinks must survive without `--replace`.
