# Repo advertising strategy

Goal: increase GitHub stars and developer visibility for **cursor-commands** by making the public surface complete, visual, and consistently branded. Truth over hype: the pitch stays "production-grade slash commands with paired skill contracts, behavioral evals, and ship-gate CI". Not an official Cursor product.

## Current value prop (stranger test)

One-liner (README and GitHub About, consistent): *Production-grade Cursor slash commands: each `/command` ships with a full agent skill contract, a behavioral eval rubric, and CI that fails if safety guards regress.*

Stranger verdict (post-rollout): first viewport now has badges, an illustrative demo GIF, a 60-second quickstart with transcript, and a clear install path. Still assumes Cursor familiarity; that is acceptable for this audience.

## Completeness checklist

| Surface | State |
|---------|-------|
| README hero pitch + why table | Green |
| CI badges (validate, docs, install-smoke, eval-fixtures) | Green |
| Install paths (plugin, symlink, submodule) | Green |
| Architecture diagram + eval story | Green |
| LICENSE (MIT), SECURITY, CONTRIBUTING | Green |
| Issue/PR templates, Dependabot | Green |
| GitHub About + 9 topics, release automation | Green |
| Release freshness | **Done:** [v1.6.0](https://github.com/emaraschio/cursor-commands/releases/tag/v1.6.0) (43 commands) |
| Demo media | **Done:** illustrative `docs/assets/demo.gif` embedded in README (optional: replace with live IDE capture) |
| Sample output | **Done:** 60-second quickstart transcript for `/define-agent-goal` |
| Social preview image | **File ready:** `docs/assets/social-preview.png` (1280x640). Confirm Settings → Social preview uses this card (not a cached default). |
| Docs index | **Done:** Architecture docs table in README |
| Deep-dive write-up | **Done:** [dev.to](https://dev.to/emaraschio/treat-prompts-like-code-skills-evals-and-ship-gate-ci-for-cursor-slash-commands-1o03) |

## Ranked improvements

### P0 (shipped)

1. **Cut v1.6.0.** Done. Release notes and README banner match catalog 43.
2. **Demo GIF.** Done (illustrative mock at `docs/assets/demo.gif`). Optional later: live IDE recording.
3. **60-second quickstart.** Done. Plugin URL + lightly trimmed Goal transcript.

### P1 (mostly shipped)

4. **Social preview image.** Asset committed. **Manual:** upload/confirm in GitHub Settings → Social preview.
5. **Deep-dive write-up.** Done on [dev.to](https://dev.to/emaraschio/treat-prompts-like-code-skills-evals-and-ship-gate-ci-for-cursor-slash-commands-1o03). Cursor forum short-form still optional (`agent-goals/advertising-drafts.md`).

### P2 (shipped / intentional default)

6. **Docs table in the README.** Done (PLUGIN, EVAL_CI, VERIFICATION, ROADMAP, COMMAND_SCHEMA).
7. **Homepage URL.** Left on `#readme` by design. Optional: point at the latest release.

## Remaining (human only)

- Confirm social preview in repo Settings.
- Optional Cursor forum post from the local drafts file.
- Optional swap of illustrative GIF for a real capture.

## Branding consistency rules

- One value prop everywhere: README hero, GitHub About, release notes, any posts.
- Catalog count appears in exactly the places CI already syncs (README, validator, install script); external posts may say "40+ commands" so they do not stale.
- Always include "Not an official Cursor product" where affiliation could be implied.
- Portable OSS: generic example names only; no employer references.

## Appendix: copy-paste agent prompt (P0 scope only)

Kept for reuse on other repos. For this catalog, P0 is complete.

```text
You are improving the public surface of the GitHub repo <REPO_URL> to increase stars. Scope is strictly limited to the three P0 items below. Do not touch command/skill behavior, do not invent metrics, and do not claim official affiliation with any product vendor.

1. Release freshness: if the latest git tag is older than the README's stated catalog state, prepare a release: update CHANGELOG (move Unreleased under a new version heading), confirm counts in README/scripts match, and output the exact tag command for the human to run.
2. Demo GIF: add a placeholder block at the top of the README (below badges) referencing docs/assets/demo.gif with one-line alt text and a TODO note listing the exact 20-second capture script (open /, autocomplete, run one command, show output). Do not fabricate the GIF.
3. Quickstart with real output: add a "60-second quickstart" section right after the hero: install step, then one short real transcript of a representative command (run it if you can; otherwise mark clearly as illustrative and keep it faithful to the skill contract).

Verify before finishing: repo CI checks pass locally (validator, link check if available); README renders without broken links; no em dashes in new prose; value prop wording matches the GitHub About description exactly.
```
