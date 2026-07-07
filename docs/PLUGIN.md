# Plugin install

Install **cursor-commands** as a Cursor user plugin so slash commands and skills sync to your account (desktop, web, CLI, and the [Cursor iOS app](https://cursor.com/docs/cloud-agent/mobile)).

This repo ships **commands and skills only**. Rules, MCP servers, hooks, and org-specific overlays stay in your host workspace.

## Recommended: user plugin (account sync)

### From GitHub (account sync, iPhone)

1. Open **Customize** in the Cursor sidebar (or **Cursor Settings → Plugins**).
2. Select your user scope (for example **Ezequiel Maraschio**).
3. Open the **Plugins** tab and click **+ Add**.
4. Enter the repository URL: `https://github.com/emaraschio/cursor-commands`
5. Install at **user** scope (not project-only) so commands follow your account to mobile.
6. Reload the window if slash commands do not appear immediately.

### From a local clone (folder picker)

Cursor copies the selected marketplace entry into a local cache. Do **not** point the entry at the repository root: that includes `.git`, and Git's fsmonitor socket (`.git/fsmonitor--daemon.ipc`) makes Cursor's copy step fail with `Cannot copy a socket file`.

This repo ships a materialized package at `plugin/` (no `.git`). The root [`.cursor-plugin/marketplace.json`](../.cursor-plugin/marketplace.json) sets `"source": "plugin"`.

1. Clone or open this repository locally.
2. If you changed commands/skills, run `./scripts/sync-plugin-package.sh`.
3. **Customize → Plugins → + Add** and select the **repository root** folder (the directory that contains `.cursor-plugin/marketplace.json`).
4. Install the `cursor-commands` entry at **user** scope.
5. Reload the window if needed.

**If install still fails:** remove stale cache, disable fsmonitor for this clone, retry:

```bash
rm -rf ~/.cursor/plugins/cache/cursor-commands
rm -rf ~/.cursor/plugins/marketplaces/_/users/"$(whoami)"/*
git -C /path/to/cursor-commands config core.fsmonitor false
```

Prefer **GitHub URL** install when you want account sync without managing a local clone.

After install, type `/` in agent chat on desktop or iOS and confirm catalog entries such as `/code-review` and `/define-agent-goal`.

### Mobile check

On the Cursor iOS app (same account):

1. Start or open an agent.
2. Type `/` and confirm catalog commands autocomplete.
3. Run a lightweight plan-only command (for example `/define-agent-goal`) and confirm the agent follows the skill contract.

Mobile is cache-first; allow a moment for sync after first install.

## Local plugin development

For fast iteration without the folder picker cache, symlink the materialized package:

```bash
./scripts/sync-plugin-package.sh
mkdir -p ~/.cursor/plugins/local
ln -sfn "$(pwd)/plugin" ~/.cursor/plugins/local/cursor-commands
```

Do not symlink the repository root into `~/.cursor/plugins/local/`; that pulls in `.git` and breaks the same way as the folder picker.

Restart Cursor or run **Developer: Reload Window**. Verify components under **Customize → Plugins**.

## Symlink install (alternative)

`./scripts/install.sh` still symlinks into `~/.cursor/commands/` and `~/.cursor/skill-contracts/` for merge-friendly local overlays. Use it when you vendor this repo as a submodule or need host-specific commands beside the generic catalog.

| Path | Best for |
|------|----------|
| **User plugin** | Account-wide sync, iPhone, web agents |
| **`install.sh`** | Submodule/dotfiles, merge overlays, offline clone |

Installing both is supported but causes duplicate `/` menu entries. Pick one path; if you use the plugin, run `./scripts/install.sh --uninstall` to drop catalog symlinks from `~/.cursor`.

## Duplicate entries in the `/` menu

Each catalog name should appear **once** (⚡ slash command). If you see **two** rows per name (⚡ and ✨), fix both causes below.

### 1. Plugin + symlink install (most common)

`./scripts/install.sh` symlinks the catalog into `~/.cursor/commands/` and `~/.cursor/skill-contracts/`. The user plugin loads the same catalog at account scope. Cursor shows both.

**Fix:** keep the plugin; remove symlinks:

```bash
./scripts/install.sh --uninstall
```

Reload the window (**Developer: Reload Window**).

### 2. Workflow bodies under `.cursor/skills/` (paired catalog)

Cursor indexes **`.cursor/skills/`** for the `/` menu. When a paired workflow body lives there beside a slash command of the same name, you get **two rows** (⚡ + ✨) even with `user-invocable: false`.

**Fix:** use a current catalog build where bodies live in **`.cursor/skill-contracts/`** (not indexed for `/`). Clear stale plugin cache if you still see ✨ rows from an old package:

```bash
rm -rf ~/.cursor/plugins/cache/cursor-commands
rm -rf ~/.cursor/plugins/cache/emaraschio-cursor-commands
rm -rf ~/.cursor/plugins/marketplaces/github.com/emaraschio/cursor-commands
rm -rf ~/.cursor/plugins/marketplaces/_/users/"$(whoami)"/*
```

Reload the window. Type `/defi` and expect a single `define-agent-goal` row (⚡ only).

### 3. Developing inside this repository

Opening the `cursor-commands` clone as the workspace root loads project-scoped `.cursor/commands/`. If workflow bodies still live under `.cursor/skills/` (older checkout), you also get ✨ rows. Current catalog keeps bodies in `.cursor/skill-contracts/` only. User-plugin rows can still stack on workspace rows while you edit the catalog; test `/` from another workspace for a clean palette.

## Manifest

Manifests live at:

- [`.cursor-plugin/plugin.json`](../.cursor-plugin/plugin.json): `commands` and `skillContracts` paths (no `skills` field; avoids duplicate `/` menu rows)
- [`.cursor-plugin/marketplace.json`](../.cursor-plugin/marketplace.json): required for **Add from folder** in Customize (`"source": "plugin"`)
- [`plugin/`](../plugin/): materialized package copied by Cursor (no `.git`)

CI validates manifests and runs `./scripts/sync-plugin-package.sh --check` so `plugin/` stays in sync with `.cursor/commands` and `.cursor/skill-contracts/`.

## External dependency

`/merge-open-prs` expects the user-global **babysit** skill at `~/.cursor/skills-cursor/babysit/SKILL.md`. It is not bundled in this plugin.

## Related

- [Plugins reference](https://cursor.com/docs/reference/plugins)
- [VERIFICATION.md](VERIFICATION.md): manual smoke after install
- [PUBLISHING.md](PUBLISHING.md): release checklist (marketplace submission is out of scope for now)
