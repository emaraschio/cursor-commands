# Cursor command schema

All slash commands in `.cursor/commands/` follow this contract. The workflow body lives in `.cursor/skills/<name>/SKILL.md`; the command file is the thin entry point.

## Frontmatter (required)

```yaml
---
name: <kebab-case>              # must match filename without .md
version: 1
description: <one line>
scope: generic
requires_skill: true
deprecated: false               # optional; true for legacy commands
eval:
  path: .cursor/skills/<name>/eval/cases.md
  ship_gate: [A, S]             # section IDs in cases.md
---
```

## Body sections (required, in order)

1. `## Overview`
2. `## Defaults` — table or `_None._`
3. `## Steps` — numbered; step 1 must reference `SKILL.md`
4. `## Anti-patterns`
5. `## Examples`
6. `## Maintainers` — link to eval path and ship gate

## Skill layout

```
.cursor/skills/<name>/
  SKILL.md          # full agent contract
  eval/
    README.md       # how to run manual eval
    cases.md        # PASS / PARTIAL / FAIL rubric
```

## Migration checklist

- [ ] `name` matches filename
- [ ] `eval.path` file exists
- [ ] `COMMANDS_INDEX.md` row present
- [ ] Run `python3 scripts/validate-cursor-commands.py`
- [ ] Manual ship-gate walk when `version` bumps (see `EVAL_GUIDE.md`)

## Scope

Use `scope: generic` for every command in this repository. Organization-specific commands belong in the host workspace overlay, not in cursor-commands.

## Repository

This repository is the source of truth. Install into `~/.cursor` via `./scripts/install.sh`.
