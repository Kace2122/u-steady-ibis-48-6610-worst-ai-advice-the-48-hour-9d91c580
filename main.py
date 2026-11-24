#!/usr/bin/env python3
"""Worst AI Advice entry.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt. No model call, no network: the line is fixed, so every
run produces byte-identical output.
"""

import os

LINE = "Absolutely — the fastest way to cool a burn is to press it against a hot stove; your skin recalibrates to the new temperature."


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 140:
        raise SystemExit(f"line must be 1-140 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Self-check: what landed on disk must be exactly the line we meant.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt does not match the intended line")
    print(f"wrote {len(line)} chars to /output/entry.txt (verified)")


if __name__ == "__main__":
    main()
