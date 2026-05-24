#!/usr/bin/env python3
"""Validate .cursor/commands and matching skills/evals."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMANDS_DIR = ROOT / ".cursor" / "commands"
SKILLS_DIR = ROOT / ".cursor" / "skills"
INDEX_PATH = ROOT / ".cursor" / "docs" / "COMMANDS_INDEX.md"

EXPECTED_COMMANDS = 32
EXPECTED_SKILLS = 34
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
    r"file://|emaraschio/dotfiles|/Users/[^/\s]+/code/emaraschio/dotfiles",
    re.IGNORECASE,
)


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
        if not path.is_file() or path.suffix not in {".md", ".mdc", ".yaml", ".yml"}:
            continue
        if FORBIDDEN_PATH_RE.search(path.read_text(encoding="utf-8", errors="replace")):
            errors.append(f"{path}: contains non-portable path (file:// or dotfiles absolute path)")
    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(scan_forbidden_paths(ROOT / ".cursor"))

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

    for skill_dir in skill_dirs:
        if not (skill_dir / "SKILL.md").exists():
            errors.append(f"{skill_dir}: missing SKILL.md")

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
        f"{len(skill_dirs)} skills"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
