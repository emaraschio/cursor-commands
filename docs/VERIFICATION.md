# Cursor IDE verification

Run after `./scripts/install.sh` (merge mode by default). Automated checks run in CI via `install-smoke.yml` and `scripts/test_install.sh`; this doc covers manual IDE validation.

## Automated (install script)

The install script already verifies:

- 28 command symlinks and 28 skill symlinks
- Each symlink target resolves
- `validate-cursor-commands.py` passes
- `merge-open-prs` skill is reachable under `$CURSOR_HOME`

## Manual smoke test

1. **Restart Cursor** or reload the window (slash commands load from `~/.cursor/commands/`).
2. Open the slash command palette — confirm entries such as `/code-review` and `/commit-same-branch`.
3. Run **`/code-review`** on a small diff — the agent should read `~/.cursor/skills/code-review/SKILL.md`.
4. In a git repo with `gh` authenticated, run **`/merge-open-prs --dry-run`** — agent should follow the merge-open-prs skill and reference **babysit** at `~/.cursor/skills-cursor/babysit/SKILL.md` (install babysit separately if missing).
5. Optional: open any workspace that has a `.cursor/memory-bank/` directory and run **`/update-memory-bank`** — command and skill should resolve via the install symlinks (memory-bank content lives in the host repo, not in cursor-commands).

Record pass/fail in release notes when cutting a tag.

## Merge mode (host overlay)

If you use a host overlay (e.g. org commands in dotfiles after generic install):

1. Run `./scripts/install.sh` (or your wrapper that calls it).
2. Confirm overlay commands still exist under `~/.cursor/commands/` alongside catalog entries.
3. Re-run install after a submodule bump — overlay symlinks must survive without `--replace`.
