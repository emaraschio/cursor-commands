# Publishing checklist

Steps before making **cursor-commands** public on GitHub.

## 1. Purge org-specific content from git history

**Status:** Completed in `v0.2.1` / `v0.2.3` (filter-repo + forbidden-string CI). Re-verified before `v1.0.0` on **2026-05-25** via `python3 scripts/check_forbidden_org_strings.py`. Re-run §1 only if new org-scoped paths are discovered.

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
python3 scripts/check_forbidden_org_strings.py
python3 scripts/validate-cursor-commands.py
python3 scripts/run-eval-fixtures.py --strict
./scripts/install.sh
```

## 3. Make the repository public

```bash
gh repo edit emaraschio/cursor-commands --visibility public --accept-visibility-change-consequences
```

After public visibility:

- Drop the self-repo ignore in [`.markdown-link-check.json`](../.markdown-link-check.json) (private-repo 403 workaround).
- Confirm [README.md](../README.md) release banner matches the latest tag.
- Re-run docs CI (link check against public URLs).

## 4. Branch protection (`main`)

Requires **public** repo (or GitHub Pro on a private repo). Set required status checks:

- `validate`
- `docs`
- `install-smoke`
- `eval-fixtures`

```bash
gh api repos/emaraschio/cursor-commands/branches/main/protection -X PUT \
  --input - <<'EOF'
{
  "required_status_checks": {
    "strict": true,
    "contexts": ["validate", "docs", "install-smoke", "eval-fixtures"]
  },
  "enforce_admins": false,
  "required_pull_request_reviews": null,
  "restrictions": null,
  "required_linear_history": false,
  "allow_force_pushes": false,
  "allow_deletions": false
}
EOF
```

Or: GitHub → **Settings → Branches → `main` → Add rule** → require the four checks above.

## 5. Post-launch (v1.0.0+)

v1.0.0 exit criteria are complete; see [ROADMAP.md: v1.0.0](ROADMAP.md#v100-public-launch-complete). For new releases: tag `v*`, let [release.yml](../.github/workflows/release.yml) publish notes from [CHANGELOG.md](../CHANGELOG.md), and add a row to [VERIFICATION.md](VERIFICATION.md).

## Org extensions today

Install generic commands from this repo, then symlink org-specific commands and skills from the **host workspace** that owns your Cursor rules and memory bank.
