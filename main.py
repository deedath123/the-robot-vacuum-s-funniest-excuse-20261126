#!/usr/bin/env python3
"""Robot vacuum excuse entry: writes one line to /output/entry.txt."""

import os

ENTRY = (
    "I skipped the corner at 3:04 a.m. \u2014 a hairball the size of a hamster "
    "stood guard, so I retreated to my dock to survive."
)


def main():
    assert ENTRY.strip(), "entry must not be blank"
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
