## Summary

<!-- What changed and why (1–3 sentences) -->

## Type

- [ ] Command / skill behavior
- [ ] Eval rubric or fixtures
- [ ] Install / CI / scripts
- [ ] Docs only

## Test plan

- [ ] `python3 scripts/validate-cursor-commands.py`
- [ ] `python3 scripts/run-eval-fixtures.py --strict`
- [ ] `./scripts/test_install.sh` (if `scripts/install.sh` changed)
- [ ] Ship-gate manual walk for sections in command frontmatter `eval.ship_gate` (if `SKILL.md` or `cases.md` changed)
- [ ] `python3 scripts/inventory-eval-cases.py --write docs/EVAL_INVENTORY.md` (if ship gate or case inventory changed)
- [ ] [COMMANDS_INDEX.md](.cursor/docs/COMMANDS_INDEX.md) updated (if catalog changed)
- [ ] No `file://`, absolute user paths, or private host-repo URLs in `.cursor/`, `docs/`, `README.md`, or `CONTRIBUTING.md`

## Ship gate (if applicable)

Command(s) and sections walked:

<!-- e.g. requirement-to-implementation: A, S — all PASS -->
