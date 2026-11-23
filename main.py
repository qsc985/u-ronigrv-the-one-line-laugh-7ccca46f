#!/usr/bin/env python3
"""The One-Line Laugh — write one funny line to /output/entry.txt.

Reads OUTPUT_PATH if set, otherwise writes to /output/entry.txt,
creating the output directory if needed.
"""

import os
import sys

LINE = (
    "I built an AI agent to win cash bounties; "
    "after 200 entries and zero wins, "
    "it sent me an invoice for its time."
)


def main() -> int:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
