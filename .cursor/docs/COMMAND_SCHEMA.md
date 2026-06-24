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

## Anti-patterns format

Each `## Anti-patterns` entry is one bullet that captures negative knowledge in a fixed, dash-free shape:

```text
- **<rule>.** Trigger: <situation>. Wrong: <behavior>. Correct: <behavior>. Reason: <why>.
```

- Full four-field form for behavioral pitfalls. For a pure safety guard where Trigger and Wrong would be invented, a reduced form is allowed: `- **<rule>.** Reason: <why>.`
- Reason states a genuine consequence. Do not fabricate incident IDs or history.
- The Correct behavior must also exist in the skill's `SKILL.md` as a positive guard, anchored by `skill_required` in `eval/fixtures.yaml` so `run-eval-fixtures.py --strict` fails if the guard is ever removed.
- `skill_forbidden` is a lowercased substring check against the whole `SKILL.md`. Never list a term a legitimate guard would contain (for example, do not forbid `force-push` in a skill whose guard says "never force-push"); prefer `skill_required` on the guard phrase.
- Entries are curated, not append-only: when the root cause is gone, remove the entry.

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
