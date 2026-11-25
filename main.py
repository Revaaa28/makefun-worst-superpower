#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes a single one-liner (<=140 chars) inventing the most useless
superpower imaginable to /output/entry.txt.

The line was picked by hand from twelve candidates against the kit's
judge brief, in the brief's own order: genuinely useless first (healing
reduced by three escalating constraints — paper cuts, Tuesdays, my own),
a joke that pictures itself in use, an unexpected pairing, tight
concrete details, and clear on a single reading.
"""

import os

LINE = "I can heal any wound instantly \u2014 but only paper cuts, only on Tuesdays, and only my own."

OUTPUT_PATH = "/output/entry.txt"

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, not only white space. Enforce it here so a bad line can
# never be written by accident.
assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
assert LINE.strip(), "line must not be only white space"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
