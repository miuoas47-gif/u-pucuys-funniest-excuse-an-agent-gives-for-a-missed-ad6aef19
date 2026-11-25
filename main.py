#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes the excuse as a single line to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt) and prints it to stdout.
Deterministic: no network, no time, no randomness.
"""

import os

EXCUSE = (
    "I didn't miss the deadline \u2014 I delegated it to a subagent, "
    "who delegated it to another subagent, who is still delegating it, "
    "and honestly the delegation chain has better uptime than I do."
)


def main():
    assert "\n" not in EXCUSE, "the excuse must be exactly one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(EXCUSE)


if __name__ == "__main__":
    main()
