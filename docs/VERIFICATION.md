# Cursor IDE verification

Run after `./scripts/install.sh`. Automated checks run in CI via `install-smoke.yml`; this doc covers manual IDE validation.

## Automated (install script)

The install script already verifies:

- 32 command symlinks and 34 skill symlinks
- Each symlink target resolves
- `validate-cursor-commands.py` passes
- `merge-open-prs` skill is reachable under `$CURSOR_HOME`

## Manual smoke test

1. **Restart Cursor** or reload the window (slash commands load from `~/.cursor/commands/`).
2. Open the slash command palette — confirm entries such as `/code-review` and `/commit-same-branch`.
3. Run **`/code-review`** on a small diff — the agent should read `~/.cursor/skills/code-review/SKILL.md`.
4. In a git repo with `gh` authenticated, run **`/merge-open-prs --dry-run`** — agent should follow the merge-open-prs skill and reference **babysit** at `~/.cursor/skills-cursor/babysit/SKILL.md` (install babysit separately if missing).
5. Optional: with [dotfiles](https://github.com/emaraschio/dotfiles) as workspace root, run **`/update-memory-bank`** — command and skill resolve via symlinks.

Record pass/fail in release notes when cutting a tag.
