# Plugin install

Install **cursor-commands** as a Cursor user plugin so slash commands and skills sync to your account (desktop, web, CLI, and the [Cursor iOS app](https://cursor.com/docs/cloud-agent/mobile)).

This repo ships **commands and skills only**. Rules, MCP servers, hooks, and org-specific overlays stay in your host workspace.

## Recommended: user plugin (account sync)

1. Open **Customize** in the Cursor sidebar (or **Cursor Settings → Plugins**).
2. Select your user scope (for example **Ezequiel Maraschio**).
3. Open the **Plugins** tab and click **+ Add**.
4. Enter the repository URL: `https://github.com/emaraschio/cursor-commands`
5. Install at **user** scope (not project-only) so commands follow your account to mobile.
6. Reload the window if slash commands do not appear immediately.

After install, type `/` in agent chat on desktop or iOS and confirm catalog entries such as `/code-review` and `/define-agent-goal`.

### Mobile check

On the Cursor iOS app (same account):

1. Start or open an agent.
2. Type `/` and confirm catalog commands autocomplete.
3. Run a lightweight plan-only command (for example `/define-agent-goal`) and confirm the agent follows the skill contract.

Mobile is cache-first; allow a moment for sync after first install.

## Local plugin development

Before opening a pull request, load the repo as a local plugin:

```bash
mkdir -p ~/.cursor/plugins/local
ln -sfn "$(pwd)" ~/.cursor/plugins/local/cursor-commands
```

Restart Cursor or run **Developer: Reload Window**. Verify components under **Customize → Plugins**.

## Symlink install (alternative)

`./scripts/install.sh` still symlinks into `~/.cursor/commands/` and `~/.cursor/skills/` for merge-friendly local overlays. Use it when you vendor this repo as a submodule or need host-specific commands beside the generic catalog.

| Path | Best for |
|------|----------|
| **User plugin** | Account-wide sync, iPhone, web agents |
| **`install.sh`** | Submodule/dotfiles, merge overlays, offline clone |

Installing both is supported. Plugin-managed entries and symlinked entries should not use conflicting names; the catalog uses unique command names under `.cursor/commands/`.

## Manifest

The plugin manifest lives at [`.cursor-plugin/plugin.json`](../.cursor-plugin/plugin.json). CI validates required fields and that `commands` / `skills` paths resolve inside the repo.

## External dependency

`/merge-open-prs` expects the user-global **babysit** skill at `~/.cursor/skills-cursor/babysit/SKILL.md`. It is not bundled in this plugin.

## Related

- [Plugins reference](https://cursor.com/docs/reference/plugins)
- [VERIFICATION.md](VERIFICATION.md): manual smoke after install
- [PUBLISHING.md](PUBLISHING.md): release checklist (marketplace submission is out of scope for now)
