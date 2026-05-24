# Publishing checklist

Steps before making **cursor-commands** public on GitHub.

## 1. Purge organization-specific content from git history

org-scoped commands/skills must not appear in any commit (required for a generic public catalog).

From a clean clone of this repo:

```bash
brew install git-filter-repo   # or pip install git-filter-repo

cat > /tmp/cm-strip-paths.txt <<'EOF'
.cursor/commands/database-migration.md
.cursor/commands/onboard-new-developer.md
.cursor/commands/script-requester.md
.cursor/commands/script-requester-v2.md
.cursor/commands/security-review.md
.cursor/skills/benchmark-rules/
.cursor/skills/database-migration/
.cursor/skills/onboard-new-developer/
.cursor/skills/script-requester/
.cursor/skills/script-requester-v2/
.cursor/skills/security-review/
scripts/bootstrap_cursor_commands.py
EOF

git filter-repo --invert-paths --paths-from-file /tmp/cm-strip-paths.txt --force

git remote add origin git@github.com:emaraschio/cursor-commands.git
git push --force origin main
```

**Tags:** Delete old pre-rewrite tags on the remote, then recreate release tags from the new history (e.g. `git tag -a v0.2.0 -m "..." && git push origin v0.2.0`).

**Consumers:** Anyone with an old clone or submodule pin must re-fetch:

```bash
git fetch origin
git reset --hard origin/main
# submodules: git submodule sync && git submodule update --init --recursive
```

## 2. Verify

```bash
# No CM command files in any revision
git log --all --oneline -- .cursor/commands/script-requester-v2.md
# (should print nothing)

python3 scripts/validate-cursor-commands.py
./scripts/install.sh
```

## 3. Remaining v1.0 items

See [ROADMAP.md](ROADMAP.md) (public visibility, merge-mode install, CHANGELOG discipline, link-check without private-repo ignores).

## organization-specific commands today

Hosted in consumer overlays (e.g. private dotfiles `.cursor/commands/`). Future home: **organization-specific/dev-tools** (TBD).
