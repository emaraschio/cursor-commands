# Merge-open-PRs profiles

Optional per-repo YAML overrides for `/merge-open-prs`. Filename = **repository basename** from `git remote get-url origin` (e.g. `myorg/admin` → `admin.yaml`).

## When to add a profile

- Docker compose layout is non-obvious (custom service names, multiple compose files)
- Default branch is not `main` / `master`
- Preferred merge strategy differs from repo default
- Extra skip labels beyond `do-not-merge` and `wip`

## When to skip

- Standard `docker compose build` + README-documented test service is enough
- Repo has no Docker; user must pass `--no-docker` and you may still add `verify.mode: host` steps

## Template

Copy [`_template.yaml`](_template.yaml) and fill in `verify.steps` and `post_merge_smoke` with commands that are safe in CI-like conditions (no `docker compose down -v` unless the user explicitly requests it).
