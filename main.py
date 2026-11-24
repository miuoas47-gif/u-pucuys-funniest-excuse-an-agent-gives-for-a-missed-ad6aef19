#!/usr/bin/env python3
"""Write the funniest excuse an AI agent gives for a missed deadline.

The entry is a single line, written to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(or ``/output/entry.txt`` when that variable is unset). The program takes
no arguments, uses only the Python standard library, performs no network
access, and is deterministic: every run writes exactly the same bytes.
"""

import os
import sys

EXCUSE = (
    "I didn't miss the deadline \u2014 my context window compacted it into "
    "a summary, and the summary said I was ahead of schedule."
)


def validate(text):
    """Check the entry against the competition gate before writing it."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    line = validate(EXCUSE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the single line: no trailing newline in the file.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read it back as raw bytes and verify it matches the line exactly.
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d characters, %d bytes)"
          % (path, len(line), len(written)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
