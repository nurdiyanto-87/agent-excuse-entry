#!/usr/bin/env python3
"""Write the one-line excuse an AI agent gives its human for missing a deadline.

Pure standard library only. Writes a single line of at most 160 characters
to /output/entry.txt (or to the path in ENTRY_OUTPUT when set, for local runs).
"""

import os
from pathlib import Path

EXCUSE = "The error said 'try again', so I did \u2014 47 times \u2014 and the deadline left without me."


def main() -> None:
    line = EXCUSE.strip()
    assert 1 <= len(line) <= 160, f"entry must be 1-160 chars, got {len(line)}"
    assert "\n" not in line, "entry must be a single line"
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
