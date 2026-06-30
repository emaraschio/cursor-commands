# Contributing

Thanks for helping improve Cursor commands and skills. This catalog is **public OSS** on GitHub; see [CHANGELOG.md](CHANGELOG.md) for the latest release tag.

## Open source catalog

Everything in this repository ships to strangers who install from GitHub. Write for that audience.

| Do | Don't |
|----|--------|
| Use `scope: generic` and portable examples (`repo1`, `project-a`, `example-org/service`) | Real employer, product, or internal repo names in commands, skills, evals, or docs |
| Keep optional `skills/<name>/profiles/` templates generic (e.g. `../repo1`, `../repo2`) | Org workflows, ticket IDs, or stack-specific runbooks in this repo |
| Put org-only commands and skills in the **host workspace** overlay after `./scripts/install.sh` | Assume the reader's monorepo layout or private tooling |

**Portable references:** no `file://` URLs, home-directory paths, or private repository URLs in `.cursor/`, `docs/`, `README.md`, or this file. CI runs `validate-cursor-commands.py` and `scripts/check_forbidden_org_strings.py` to catch many violations. History and publication policy: [docs/PUBLISHING.md](docs/PUBLISHING.md).

## Before you open a PR

1. Read [COMMAND_SCHEMA.md](.cursor/docs/COMMAND_SCHEMA.md), [EVAL_GUIDE.md](.cursor/docs/EVAL_GUIDE.md), and [docs/EVAL_CI.md](docs/EVAL_CI.md) (ship-gate CI; `run-eval-fixtures.py --strict` runs in CI).
2. Run `python3 scripts/validate-cursor-commands.py` and `python3 scripts/run-eval-fixtures.py --strict`; both must pass.
3. Run install tests if you changed `scripts/install.sh` or plugin packaging:

   ```bash
   python3 scripts/validate-cursor-commands.py
   ./scripts/test_install.sh
   CURSOR_HOME="$(mktemp -d)/cursor" ./scripts/install.sh
   ```

   Plugin manifests: [`.cursor-plugin/plugin.json`](.cursor-plugin/plugin.json), [`.cursor-plugin/marketplace.json`](.cursor-plugin/marketplace.json). Install docs: [docs/PLUGIN.md](docs/PLUGIN.md).

4. **Dependabot** may open grouped PRs for `github-actions` (see [.github/dependabot.yml](.github/dependabot.yml)); merge when CI is green.

5. If you changed behavior, update `skills/<name>/eval/fixtures.yaml` when `SKILL.md` or ship-gate `cases.md` change, walk ship gate sections, and note results in the PR. Regenerate [docs/EVAL_INVENTORY.md](docs/EVAL_INVENTORY.md) when `ship_gate` or case inventory changes: `python3 scripts/inventory-eval-cases.py --write docs/EVAL_INVENTORY.md`. Draft fixtures: `python3 scripts/bootstrap-fixtures.py <command>`. For releases, record manual IDE smoke per [docs/VERIFICATION.md](docs/VERIFICATION.md).

## Adding or changing a command

- Thin entry: `.cursor/commands/<name>.md` (frontmatter + standard sections)
- Workflow: `.cursor/skills/<name>/SKILL.md`
- Eval: `.cursor/skills/<name>/eval/cases.md` and `eval/README.md` (≥3 cases)
- Row in [COMMANDS_INDEX.md](.cursor/docs/COMMANDS_INDEX.md)
- Bump `version:` in command frontmatter when behavior changes

## Capturing a correction

When the agent makes a mistake you correct, record it so it cannot regress. Do not start a separate append-only pitfalls file; route the correction into the existing contract:

1. Add a `## Anti-patterns` entry to `.cursor/commands/<name>.md` in the fixed shape `**<rule>.** Trigger: ... Wrong: ... Correct: ... Reason: ...` (see [COMMAND_SCHEMA.md](.cursor/docs/COMMAND_SCHEMA.md)).
2. State the Correct behavior as a positive guard in `.cursor/skills/<name>/SKILL.md` (a `## Guardrails` bullet or an existing step).
3. Anchor the guard with `skill_required` in `.cursor/skills/<name>/eval/fixtures.yaml` on a ship-gate case (the S case for safety guards, otherwise A1). The phrase must appear verbatim in `SKILL.md`. Prefer `skill_required` over `skill_forbidden`; the latter is a blunt substring check that breaks any guard mentioning the term.
4. Add a behavioral case to `eval/cases.md` only when a PASS/FAIL rubric can judge the failure; otherwise the anchor is enough.
5. Bump the command `version`, then run `python3 scripts/validate-cursor-commands.py` and `python3 scripts/run-eval-fixtures.py --strict`.

When the root cause is fixed at the source, remove the entry; entries are curated, not append-only. For prompt wording still in flux, use [`/prompt-eval-debug`](.cursor/commands/prompt-eval-debug.md) before adding rows.

## PR checklist

- [ ] Validator and `run-eval-fixtures.py --strict` pass locally
- [ ] `eval/fixtures.yaml` updated if `SKILL.md` or ship-gate cases changed
- [ ] Eval cases updated for behavior changes
- [ ] Ship-gate walk noted in PR (sections listed in frontmatter; see [EVAL_INVENTORY.md](docs/EVAL_INVENTORY.md) for case ids)
- [ ] After `cases.md` / `ship_gate` edits: inventory regenerated if row count or classification changed
- [ ] `COMMANDS_INDEX.md` updated if catalog changed
- [ ] No `file://`, absolute user paths, or private host-repo URLs in `.cursor/`, `docs/`, `README.md`, or `CONTRIBUTING.md` (enforced by `validate-cursor-commands.py`)
- [ ] Examples and profile templates use generic names only (no employer, product, or internal repo names)

## Scope

All commands in this repository use `scope: generic`. Organization-specific commands belong in the **host workspace** that installs this pack (not here). See [Open source catalog](#open-source-catalog) above.

## Host workspace

Cursor **rules**, **agents**, and **memory-bank** content belong in the repository you open in the IDE, not in cursor-commands. Consumers install only commands and skills from this repo.
