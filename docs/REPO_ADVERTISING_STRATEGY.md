# Repo advertising strategy

Goal: increase GitHub stars and developer visibility for **cursor-commands** by making the public surface complete, visual, and consistently branded. Truth over hype: the pitch stays "production-grade slash commands with paired skill contracts, behavioral evals, and ship-gate CI". Not an official Cursor product.

## Current value prop (stranger test)

One-liner (README and GitHub About, consistent): *Production-grade Cursor slash commands: each `/command` ships with a full agent skill contract, a behavioral eval rubric, and CI that fails if safety guards regress.*

Stranger verdict: the first viewport works for someone who already uses Cursor, but assumes they know what slash commands and plugins are. It is all text; nothing shows the product in 5 seconds. Fixes below.

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
| Release freshness | **Gap**: latest tag v1.5.0 (40 commands) vs README "43 commands"; 11 unreleased commits including 3 new commands |
| Demo media | **Gap**: no GIF/screenshot anywhere in README |
| Sample output | **Gap**: command names listed, but no transcript showing what a run looks like |
| Social preview image | **Gap** (likely default; needs manual check in repo Settings) |
| Docs index | Weak: strong docs, but links scattered through prose |

## Ranked improvements

### P0 (do first: highest visibility per hour)

1. **Cut v1.6.0.** Three unreleased commands (`/decision-audit`, `/instruction-ablation`, `/gauntlet-loop`) plus guardrail hardening are invisible to visitors who check Releases. A fresh tag updates the "Stable release" line, produces release notes, and signals an active project. Effort: low.
2. **Add a demo GIF at the top of the README.** **Done (illustrative mock):** `docs/assets/demo.gif` shows `/` → `/define-agent-goal` → Goal output. Replace with a live IDE capture later if desired. Effort: medium.
3. **Add a 60-second quickstart with real output.** Install URL, then a short real transcript of one command (for example `/define-agent-goal` producing a six-part Goal). Readers star what they can picture using. Effort: low.

### P1 (next)

4. **Social preview image.** 1280x640 card: repo name, one-liner, three example commands. Uploaded in Settings → Social preview; this is what X/Slack/Reddit embeds show. Effort: low (generate + manual upload).
5. **One deep-dive write-up + Cursor forum showcase.** **Done (dev.to):** [Treat prompts like code: skills, evals, and ship-gate CI for Cursor slash commands](https://dev.to/emaraschio/treat-prompts-like-code-skills-evals-and-ship-gate-ci-for-cursor-slash-commands-1o03). Forum showcase still optional. Effort: medium.

### P2 (later)

6. **Docs table in the README.** One small table linking PLUGIN, EVAL_CI, VERIFICATION, ROADMAP, COMMAND_SCHEMA so the docs depth is scannable instead of buried in prose. Effort: low.
7. **Homepage URL.** Points at the README anchor today; fine. Optionally point at the latest release or a demo page once media exists. Effort: trivial.

## Branding consistency rules

- One value prop everywhere: README line 8, GitHub About, release notes, any posts.
- Catalog count appears in exactly the places CI already syncs (README, validator, install script); posts should say "40+ commands" so they do not stale.
- Always include "Not an official Cursor product" where affiliation could be implied.
- Portable OSS: generic example names only; no employer references.

## Appendix: copy-paste agent prompt (P0 scope only)

```text
You are improving the public surface of the GitHub repo <REPO_URL> to increase stars. Scope is strictly limited to the three P0 items below. Do not touch command/skill behavior, do not invent metrics, and do not claim official affiliation with any product vendor.

1. Release freshness: if the latest git tag is older than the README's stated catalog state, prepare a release: update CHANGELOG (move Unreleased under a new version heading), confirm counts in README/scripts match, and output the exact tag command for the human to run.
2. Demo GIF: add a placeholder block at the top of the README (below badges) referencing docs/assets/demo.gif with one-line alt text and a TODO note listing the exact 20-second capture script (open /, autocomplete, run one command, show output). Do not fabricate the GIF.
3. Quickstart with real output: add a "60-second quickstart" section right after the hero: install step, then one short real transcript of a representative command (run it if you can; otherwise mark clearly as illustrative and keep it faithful to the skill contract).

Verify before finishing: repo CI checks pass locally (validator, link check if available); README renders without broken links; no em dashes in new prose; value prop wording matches the GitHub About description exactly.
```
