#!/usr/bin/env python3
"""Validate .cursor/commands, matching skills/evals, and plugin manifest."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from eval_lib import (
    index_ship_gate_for,
    normalize_ship_gate_list,
    parse_cases_by_section,
    parse_ship_gate,
)

ROOT = Path(__file__).resolve().parents[1]
COMMANDS_DIR = ROOT / ".cursor" / "commands"
SKILLS_DIR = ROOT / ".cursor" / "skills"
INDEX_PATH = ROOT / ".cursor" / "docs" / "COMMANDS_INDEX.md"
PLUGIN_MANIFEST = ROOT / ".cursor-plugin" / "plugin.json"
MARKETPLACE_MANIFEST = ROOT / ".cursor-plugin" / "marketplace.json"

PLUGIN_NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")

EXPECTED_COMMANDS = 39
EXPECTED_SKILLS = 39
MIN_EVAL_CASES = 3

REQUIRED_SECTIONS = [
    "## Overview",
    "## Defaults",
    "## Steps",
    "## Anti-patterns",
    "## Examples",
    "## Maintainers",
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FORBIDDEN_PATH_RE = re.compile(
    r"file://[^\s\`'\"]+|"
    r"emaraschio/dotfiles|github\.com/emaraschio/dotfiles|"
    r"/Users/[^/\s]+/code/emaraschio/dotfiles",
    re.IGNORECASE,
)

PORTABLE_DOC_SUFFIXES = {".md", ".mdc", ".yaml", ".yml"}
PORTABLE_DOC_FILES = ("README.md", "CONTRIBUTING.md")
PORTABLE_DOC_DIRS = (".cursor", "docs")


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    data: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return data


def count_case_headings(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    return len(re.findall(r"^###\s+", text, re.MULTILINE))


def scan_forbidden_paths(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in PORTABLE_DOC_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if FORBIDDEN_PATH_RE.search(text):
            errors.append(
                f"{path}: contains non-portable reference "
                "(file://, private dotfiles URL, or absolute dotfiles path)"
            )
    return errors


def validate_plugin_manifest() -> list[str]:
    errors: list[str] = []
    if not PLUGIN_MANIFEST.is_file():
        errors.append(f"{PLUGIN_MANIFEST}: missing plugin manifest")
        return errors

    try:
        data = json.loads(PLUGIN_MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{PLUGIN_MANIFEST}: invalid JSON ({exc})")
        return errors

    if not isinstance(data, dict):
        errors.append(f"{PLUGIN_MANIFEST}: root must be a JSON object")
        return errors

    name = data.get("name")
    if not isinstance(name, str) or not name:
        errors.append(f"{PLUGIN_MANIFEST}: missing required field 'name'")
    elif not PLUGIN_NAME_RE.match(name):
        errors.append(
            f"{PLUGIN_MANIFEST}: name '{name}' must be lowercase kebab-case"
        )
    elif name != "cursor-commands":
        errors.append(
            f"{PLUGIN_MANIFEST}: name must be 'cursor-commands', got '{name}'"
        )

    version = data.get("version")
    if version is not None:
        if not isinstance(version, str) or not SEMVER_RE.match(version):
            errors.append(f"{PLUGIN_MANIFEST}: version must be semver, got '{version}'")

    for field in ("commands", "skills"):
        rel = data.get(field)
        if rel is None:
            errors.append(f"{PLUGIN_MANIFEST}: missing required field '{field}'")
            continue
        if not isinstance(rel, str):
            errors.append(f"{PLUGIN_MANIFEST}: '{field}' must be a string path")
            continue
        if rel.startswith("/") or ".." in Path(rel).parts:
            errors.append(f"{PLUGIN_MANIFEST}: '{field}' path must be relative: {rel}")
            continue
        target = ROOT / rel
        if not target.is_dir():
            errors.append(f"{PLUGIN_MANIFEST}: '{field}' path missing: {rel}")

    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{PLUGIN_MANIFEST}: missing or empty 'description'")

    return errors


def resolve_plugin_source(source: str) -> Path:
    normalized = source.strip()
    if normalized in (".", "./"):
        return ROOT
    return (ROOT / normalized).resolve()


def validate_marketplace_manifest() -> list[str]:
    errors: list[str] = []
    if not MARKETPLACE_MANIFEST.is_file():
        errors.append(f"{MARKETPLACE_MANIFEST}: missing marketplace manifest")
        return errors

    try:
        data = json.loads(MARKETPLACE_MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"{MARKETPLACE_MANIFEST}: invalid JSON ({exc})")
        return errors

    if not isinstance(data, dict):
        errors.append(f"{MARKETPLACE_MANIFEST}: root must be a JSON object")
        return errors

    name = data.get("name")
    if not isinstance(name, str) or not name:
        errors.append(f"{MARKETPLACE_MANIFEST}: missing required field 'name'")
    elif not PLUGIN_NAME_RE.match(name):
        errors.append(
            f"{MARKETPLACE_MANIFEST}: name '{name}' must be lowercase kebab-case"
        )

    owner = data.get("owner")
    if not isinstance(owner, dict) or not isinstance(owner.get("name"), str) or not owner.get("name"):
        errors.append(f"{MARKETPLACE_MANIFEST}: missing owner.name")

    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append(f"{MARKETPLACE_MANIFEST}: plugins must be a non-empty array")
        return errors

    for index, entry in enumerate(plugins):
        label = f"{MARKETPLACE_MANIFEST}: plugins[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{label}: must be an object")
            continue
        plugin_name = entry.get("name")
        source = entry.get("source")
        if not isinstance(plugin_name, str) or not plugin_name:
            errors.append(f"{label}: missing name")
            continue
        if not isinstance(source, str) or not source.strip():
            errors.append(f"{label}: missing source")
            continue
        if source.startswith("/") or ".." in Path(source).parts:
            errors.append(f"{label}: source must be relative: {source}")
            continue
        plugin_root = resolve_plugin_source(source)
        if not plugin_root.is_dir():
            errors.append(f"{label}: source path missing: {source}")
            continue
        if (plugin_root / ".git").exists():
            errors.append(
                f"{label}: source must not include .git; use plugin/ package directory"
            )
        plugin_json = plugin_root / ".cursor-plugin" / "plugin.json"
        if not plugin_json.is_file():
            errors.append(f"{label}: no plugin manifest at {plugin_json.relative_to(ROOT)}")
            continue
        try:
            plugin_data = json.loads(plugin_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{label}: plugin manifest invalid JSON ({exc})")
            continue
        manifest_name = plugin_data.get("name")
        if manifest_name != plugin_name:
            errors.append(
                f"{label}: name '{plugin_name}' does not match plugin.json name '{manifest_name}'"
            )

    return errors


def scan_portable_docs() -> list[str]:
    errors: list[str] = []
    for dirname in PORTABLE_DOC_DIRS:
        errors.extend(scan_forbidden_paths(ROOT / dirname))
    for filename in PORTABLE_DOC_FILES:
        path = ROOT / filename
        if path.is_file():
            text = path.read_text(encoding="utf-8", errors="replace")
            if FORBIDDEN_PATH_RE.search(text):
                errors.append(
                    f"{path}: contains non-portable reference "
                    "(file://, private dotfiles URL, or absolute dotfiles path)"
                )
    return errors


def main() -> int:
    errors: list[str] = []
    check_script = ROOT / "scripts" / "check_forbidden_org_strings.py"
    import subprocess

    if subprocess.run([sys.executable, str(check_script)], check=False).returncode != 0:
        return 1
    errors.extend(scan_portable_docs())
    errors.extend(validate_plugin_manifest())
    errors.extend(validate_marketplace_manifest())

    sync_script = ROOT / "scripts" / "sync-plugin-package.sh"
    if sync_script.is_file():
        if subprocess.run([str(sync_script), "--check"], check=False).returncode != 0:
            errors.append("plugin/ package out of sync; run ./scripts/sync-plugin-package.sh")

    command_files = sorted(COMMANDS_DIR.glob("*.md"))
    if len(command_files) != EXPECTED_COMMANDS:
        errors.append(f"expected {EXPECTED_COMMANDS} commands, found {len(command_files)}")

    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    if len(skill_dirs) != EXPECTED_SKILLS:
        errors.append(f"expected {EXPECTED_SKILLS} skill dirs, found {len(skill_dirs)}")

    names: list[str] = []
    for path in command_files:
        name = path.stem
        names.append(name)
        text = path.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm:
            errors.append(f"{path}: missing YAML frontmatter")
            continue
        if fm.get("name") != name:
            errors.append(f"{path}: frontmatter name '{fm.get('name')}' != filename")
        if fm.get("requires_skill") != "true":
            errors.append(f"{path}: requires_skill must be true")

        m = FRONTMATTER_RE.match(text)
        if m:
            block = m.group(1)
            path_match = re.search(r"path:\s*(.+)", block)
            if path_match:
                eval_rel = path_match.group(1).strip()
                eval_full = ROOT / eval_rel
                if not eval_full.exists():
                    errors.append(f"{path}: eval path missing: {eval_rel}")
            else:
                errors.append(f"{path}: eval.path missing in frontmatter")

        for sec in REQUIRED_SECTIONS:
            if sec not in text:
                errors.append(f"{path}: missing section {sec}")

        skill_md = SKILLS_DIR / name / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{path}: missing skill {skill_md}")

        if "SKILL.md" not in text:
            errors.append(f"{path}: Steps must reference SKILL.md")

        eval_cases = SKILLS_DIR / name / "eval" / "cases.md"
        eval_readme = SKILLS_DIR / name / "eval" / "README.md"
        if not eval_cases.exists():
            errors.append(f"{path}: missing {eval_cases}")
        elif count_case_headings(eval_cases) < MIN_EVAL_CASES:
            errors.append(f"{eval_cases}: fewer than {MIN_EVAL_CASES} case headings (###)")
        if not eval_readme.exists():
            errors.append(f"{path}: missing {eval_readme}")

        gate_ids = parse_ship_gate(text)
        if not gate_ids:
            errors.append(f"{path}: eval.ship_gate missing or empty")
        elif eval_cases.exists():
            cases_text = eval_cases.read_text(encoding="utf-8")
            by_section = parse_cases_by_section(cases_text)
            for sec in gate_ids:
                if sec not in by_section:
                    errors.append(
                        f"{path}: missing_section — no ## Section {sec} in cases.md"
                    )
                elif not by_section[sec]:
                    errors.append(
                        f"{path}: missing_case — Section {sec} has no ### cases"
                    )

        index_gate = index_ship_gate_for(name)
        if index_gate is not None and gate_ids:
            index_ids = [
                s.strip()
                for s in re.split(r",\s*", index_gate.replace("—", "").strip())
                if s.strip()
            ]
            if normalize_ship_gate_list(index_ids) != normalize_ship_gate_list(gate_ids):
                errors.append(
                    f"{path}: index_ship_gate_mismatch — index '{index_gate}' "
                    f"!= frontmatter '{', '.join(gate_ids)}'"
                )

    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        skill_fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        if skill_fm.get("user-invocable") != "false":
            errors.append(
                f"{skill_md}: user-invocable must be false (paired slash command owns / menu entry)"
            )

    if INDEX_PATH.exists():
        index_text = INDEX_PATH.read_text(encoding="utf-8")
        for name in names:
            if f"| `{name}` |" not in index_text:
                errors.append(f"COMMANDS_INDEX.md: missing row for {name}")
    else:
        errors.append("COMMANDS_INDEX.md not found")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    print(
        f"OK: validated {len(command_files)} commands, "
        f"{len(skill_dirs)} skills, plugin and marketplace manifests"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
