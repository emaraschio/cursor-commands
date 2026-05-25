# Security Policy

## Scope

This repository ships Cursor slash commands, Agent Skills, and behavioral eval rubrics. It does not run a network service or process end-user data.

## Supported versions

Security fixes apply to the latest release tag on `main` (currently `v1.0.0`). Patch releases use new `v*` tags; consumers should pin the latest tag or track `main`.

## Reporting a vulnerability

While the repository is private, use **GitHub → Security → Report a vulnerability** (private vulnerability reporting).

Include:

- Affected file paths (command, skill, install script, or workflow)
- Steps to reproduce or a minimal prompt that triggers the issue
- Impact (e.g. credential exposure, destructive install behavior, deceptive prompt content)

## In scope

- Malicious or deceptive content in commands or skills committed to this repo
- Credentials, tokens, or private keys committed to the tree
- `scripts/install.sh` or related scripts that exfiltrate data or destroy unrelated files under `~/.cursor`

## Out of scope

- Agent misbehavior in consumer host workspaces (rules, memory-bank, org overlays)
- Third-party MCP servers or tools referenced in skills
- Defects in the Cursor IDE itself

## Response

Acknowledgment within a reasonable window for valid reports. Fixes ship via `main` and a semver tag per [CHANGELOG.md](CHANGELOG.md).
