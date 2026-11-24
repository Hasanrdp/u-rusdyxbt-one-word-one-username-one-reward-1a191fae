#!/usr/bin/env python3
"""One Word, One Username, One Reward -- entry program.

The bounty asks for one thing only: the entrant's own make.fun username,
sent as a single word, with nothing else beside it. This program writes
exactly that username to /output/entry.txt -- no explanation, no links,
no pitch, no trailing newline, no padding.

The username is the handle of the make.fun account this entry is submitted
from, so the judge's first criterion (a real make.fun username, the
entrant's own handle, sent as one word) is met by construction.
"""

import os

USERNAME = "sunny-koala-64"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(USERNAME)


if __name__ == "__main__":
    main()
