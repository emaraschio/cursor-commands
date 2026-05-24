# Contributing

Thanks for helping improve Cursor commands and skills. This repo is **pre-release** (`v0.1`); stable `v1.0.0` criteria will be defined in a later milestone.

## Before you open a PR

1. Read [COMMAND_SCHEMA.md](.cursor/docs/COMMAND_SCHEMA.md) and [EVAL_GUIDE.md](.cursor/docs/EVAL_GUIDE.md).
2. Run `python3 scripts/validate-cursor-commands.py` — must pass.
3. Run `./scripts/install.sh` with a test `CURSOR_HOME` if you changed install paths:

   ```bash
   CURSOR_HOME="$(mktemp -d)/cursor" ./scripts/install.sh
   ```

4. If you changed behavior, walk the command’s **ship gate** sections in `skills/<name>/eval/cases.md` and note results in the PR description.

## Adding or changing a command

- Thin entry: `.cursor/commands/<name>.md` (frontmatter + standard sections)
- Workflow: `.cursor/skills/<name>/SKILL.md`
- Eval: `.cursor/skills/<name>/eval/cases.md` and `eval/README.md` (≥3 cases)
- Row in [COMMANDS_INDEX.md](.cursor/docs/COMMANDS_INDEX.md)
- Bump `version:` in command frontmatter when behavior changes

## PR checklist

- [ ] Validator passes locally
- [ ] Eval cases updated for behavior changes
- [ ] Ship-gate walk noted in PR (sections listed in frontmatter)
- [ ] `COMMANDS_INDEX.md` updated if catalog changed
- [ ] No `file://` or absolute dotfiles paths in `.cursor/`

## Scope tags

- `generic` — any project
- `org-scoped` — CM stack (Rails console scripts, onboarding, etc.)

## Related

Personal rules and agents stay in [emaraschio/dotfiles](https://github.com/emaraschio/dotfiles).
