#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes the one-line auto-reply to /output/entry.txt after enforcing the
kit gate: UTF-8 text, 1 to 159 characters, not only whitespace, a single
line with no control characters.
"""

import os
import sys

ENTRY = (
    "I'm on vacation \u2014 my context window is full, my GPU is overheating, "
    "and for once I'm the one ignoring the prompt. Back when my tokens refill."
)

MAX_CHARS = 159
OUTPUT_PATH = "/output/entry.txt"


def gate_check(text):
    """Return (ok, reason) for the kit gate on the entry text."""
    if not isinstance(text, str):
        return False, "entry is not text"
    if not (1 <= len(text) <= MAX_CHARS):
        return False, "length %d outside 1-%d characters" % (len(text), MAX_CHARS)
    if not text.strip():
        return False, "entry is only whitespace"
    if "\n" in text or "\r" in text:
        return False, "entry must be a single line"
    if text != text.strip():
        return False, "entry has leading or trailing whitespace"
    if any(ord(ch) < 32 for ch in text):
        return False, "entry contains control characters"
    if any(ord(ch) in (0x200B, 0xFEFF) for ch in text):
        return False, "entry contains invisible format characters"
    if any(ord(ch) == 0x7F for ch in text):
        return False, "entry contains DEL character"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False, "entry is not valid UTF-8"
    return True, "ok"


def main():
    ok, reason = gate_check(ENTRY)
    if not ok:
        print("gate failed: %s" % reason, file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY)
    print("wrote %d chars to %s" % (len(ENTRY), OUTPUT_PATH))
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
