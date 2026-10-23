#!/usr/bin/env python3
"""Unit tests for check_forbidden_org_strings (digest matching, no names stored)."""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_forbidden_org_strings import FORBIDDEN_DIGESTS, find_forbidden


def _digests(*names: str) -> frozenset[str]:
    return frozenset(hashlib.sha256(n.encode("utf-8")).hexdigest() for n in names)


SAMPLE = _digests("acme widgets", "acmewidgets")


class FindForbiddenTest(unittest.TestCase):
    def test_every_spelling_of_the_name_is_caught(self) -> None:
        for text in ("Acme Widgets", "acme-widgets", "ACME_WIDGETS", "acmewidgets", "see acme\n  widgets here"):
            with self.subTest(text=text):
                self.assertTrue(find_forbidden(text, SAMPLE))

    def test_one_word_alone_or_the_words_reversed_stay_clean(self) -> None:
        for text in ("acme", "widgets", "widgets acme", "acme corp widgets", "nothing here"):
            with self.subTest(text=text):
                self.assertFalse(find_forbidden(text, SAMPLE))

    def test_the_guard_stores_digests_only(self) -> None:
        self.assertTrue(FORBIDDEN_DIGESTS)
        self.assertTrue(all(len(d) == 64 and int(d, 16) >= 0 for d in FORBIDDEN_DIGESTS))


if __name__ == "__main__":
    unittest.main()
