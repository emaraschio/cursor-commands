# Contributing

Thanks for helping improve Cursor commands and skills. This repo is **pre-release** (`v0.1`); stable `v1.0.0` criteria will be defined in a later milestone.

## Before you open a PR

1. Read [COMMAND_SCHEMA.md](.cursor/docs/COMMAND_SCHEMA.md), [EVAL_GUIDE.md](.cursor/docs/EVAL_GUIDE.md), and [docs/EVAL_CI.md](docs/EVAL_CI.md) (ship-gate CI spec; Phase 2 runner not live yet).
2. Run `python3 scripts/validate-cursor-commands.py` — must pass.
3. Run `./scripts/install.sh` with a test `CURSOR_HOME` if you changed install paths:

   ```bash
   CURSOR_HOME="$(mktemp -d)/cursor" ./scripts/install.sh
   ```

4. If you changed behavior, walk the command’s **ship gate** sections in `skills/<name>/eval/cases.md` and note results in the PR description. If you add or reclassify cases, regenerate [docs/EVAL_INVENTORY.md](docs/EVAL_INVENTORY.md) with `python3 scripts/inventory-eval-cases.py --write docs/EVAL_INVENTORY.md`.

## Adding or changing a command

- Thin entry: `.cursor/commands/<name>.md` (frontmatter + standard sections)
- Workflow: `.cursor/skills/<name>/SKILL.md`
- Eval: `.cursor/skills/<name>/eval/cases.md` and `eval/README.md` (≥3 cases)
- Row in [COMMANDS_INDEX.md](.cursor/docs/COMMANDS_INDEX.md)
- Bump `version:` in command frontmatter when behavior changes

## PR checklist

- [ ] Validator passes locally
- [ ] Eval cases updated for behavior changes
- [ ] Ship-gate walk noted in PR (sections listed in frontmatter; see [EVAL_INVENTORY.md](docs/EVAL_INVENTORY.md) for case ids)
- [ ] After `cases.md` / `ship_gate` edits: inventory regenerated if row count or classification changed
- [ ] `COMMANDS_INDEX.md` updated if catalog changed
- [ ] No `file://`, absolute user paths, or private host-repo URLs in `.cursor/`, `docs/`, `README.md`, or `CONTRIBUTING.md` (enforced by `validate-cursor-commands.py`)

## Scope

All commands in this repository use `scope: generic`. Organization-specific commands belong in the **host workspace** that installs this pack (not here).

## Host workspace

Cursor **rules**, **agents**, and **memory-bank** content belong in the repository you open in the IDE — not in cursor-commands. Consumers install only commands and skills from this repo.
