# Publishing checklist

Steps before making **cursor-commands** public on GitHub.

## 1. Purge org-specific content from git history

Org-scoped commands and skills must not appear in any commit (required for a generic public catalog).

From a clean clone of this repo:

```bash
brew install git-filter-repo   # or pip install git-filter-repo

# Drop paths that belonged to an org extension pack (adjust list to match what was removed).
cat > /tmp/org-strip-paths.txt <<'EOF'
scripts/bootstrap_cursor_commands.py
EOF

git filter-repo --invert-paths --paths-from-file /tmp/org-strip-paths.txt --force

# Scrub remaining org names from all blobs and commit messages (maintain /tmp/org-text-replacements.txt in repo root).
git filter-repo --replace-text /tmp/org-text-replacements.txt --replace-message /tmp/org-text-replacements.txt --force

git remote add origin git@github.com:emaraschio/cursor-commands.git
git push --force origin main
```

**Tags:** Delete old pre-rewrite tags on the remote, then recreate release tags from the new history.

**Consumers:** Anyone with an old clone or submodule pin must re-fetch:

```bash
git fetch origin
git reset --hard origin/main
```

## 2. Verify

```bash
# No forbidden org strings in any revision
git log --all -S 'FORBIDDEN_ORG_STRING' --oneline   # should print nothing
git rev-list --all | xargs git grep -i 'FORBIDDEN_ORG_STRING' 2>/dev/null && exit 1 || true

python3 scripts/validate-cursor-commands.py
./scripts/install.sh
```

Replace `FORBIDDEN_ORG_STRING` with the org identifier you are scrubbing before running.

## 3. Remaining v1.0 items

See [ROADMAP.md](ROADMAP.md) (public visibility, merge-mode install, CHANGELOG discipline, link-check without private-repo ignores).

## Org extensions today

Install generic commands from this repo, then symlink org-specific commands and skills from the **host workspace** that owns your Cursor rules and memory bank.
