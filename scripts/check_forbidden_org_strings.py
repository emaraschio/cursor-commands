#!/usr/bin/env python3
"""Fail if forbidden organization trademarks appear in tracked content.

The names are stored only as SHA-256 digests, so the guard never spells
the names it looks for. Every word in a file is lowercased; each single
word and each pair of neighbouring words (joined by one space) is hashed
and compared, which catches "Two Words", "two-words", "two_words" and
"twowords" alike.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCAN_SUFFIXES = {".md", ".mdc", ".yaml", ".yml", ".py", ".sh"}
SKIP_REL = {
    "scripts/check_forbidden_org_strings.py",
}

# SHA-256 of each forbidden name, lowercased: as two words joined by one
# space, and as one word.
FORBIDDEN_DIGESTS = frozenset({
    "a45074211fedc77adcbc0e0653530dcbe3bbad0f4838e1e1c20e34ccede1e9fb",
    "69eb386527204685e7b54cc809b25e29300460fc74f306007377f62355e8f3cb",
})

WORD = re.compile(r"[a-z0-9]+")


def _digest(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def find_forbidden(text: str, digests: frozenset[str] = FORBIDDEN_DIGESTS) -> bool:
    words = WORD.findall(text.lower())
    for i, word in enumerate(words):
        if _digest(word) in digests:
            return True
        if i + 1 < len(words) and _digest(f"{word} {words[i + 1]}") in digests:
            return True
    return False


def main() -> int:
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
        if find_forbidden(text):
            hits.append(rel)
    if hits:
        for h in sorted(hits):
            print(f"ERROR: forbidden organization reference in {h}", file=sys.stderr)
        return 1
    print("OK: no forbidden organization references")
    return 0


if __name__ == "__main__":
    sys.exit(main())
