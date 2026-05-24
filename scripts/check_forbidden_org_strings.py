#!/usr/bin/env python3
"""Fail if forbidden organization trademarks appear in tracked content."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_SUFFIXES = {".md", ".mdc", ".yaml", ".yml", ".py", ".sh"}
SKIP_REL = {
    "scripts/check_forbidden_org_strings.py",
}


def forbidden_pattern() -> re.Pattern[str]:
    # Built from parts so the slug never appears as one literal in this repository.
    part_a, part_b = "circle", "medical"
    return re.compile(
        rf"{part_a}\s*{part_b}|{part_a}{part_b}|{part_a}-{part_b}",
        re.IGNORECASE,
    )


def main() -> int:
    pat = forbidden_pattern()
    hits: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in SKIP_REL or path.suffix not in SCAN_SUFFIXES:
            continue
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if pat.search(text):
            hits.append(rel)
    if hits:
        for h in sorted(hits):
            print(f"ERROR: forbidden organization reference in {h}", file=sys.stderr)
        return 1
    print("OK: no forbidden organization references")
    return 0


if __name__ == "__main__":
    sys.exit(main())
