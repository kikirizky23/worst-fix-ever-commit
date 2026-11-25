"""Worst Fix Ever: Funniest Commit Message.

One tiny program with one job: hand the grader a single commit-message
line for a bug fix that made everything worse.

The program prints the line to stdout and saves it to /output/entry.txt,
where the scorer reads it. Only the Python standard library is used, and
the text is a constant, so every run produces byte-identical output.
"""

from __future__ import annotations

import os
import sys

# The entry itself: one commit subject line, well under the 100-character
# limit the gate enforces. The joke is the fix "working" by the wrong
# metric -- the button is gone, so nobody can complain about it anymore.
COMMIT_MESSAGE = "fix: the button did nothing, so I deleted it; zero complaints since"

# Where the grader expects the entry text.
OUTPUT_PATH = "/output/entry.txt"


MAX_ENTRY_CHARS = 100


def entry_text() -> str:
    """Return the commit message with no stray whitespace around it."""
    return COMMIT_MESSAGE.strip()


def save_entry(path: str) -> None:
    """Write the entry text to ``path``, making its folder if needed."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(entry_text())


def main(argv: list[str] | None = None) -> int:
    """Print the entry and save it; return 0 on success."""
    del argv  # no command-line options: the entry is fixed on purpose.
    text = entry_text()
    if not 1 <= len(text) <= MAX_ENTRY_CHARS:
        print(f"entry is {len(text)} characters, must be 1-{MAX_ENTRY_CHARS}",
              file=sys.stderr)
        return 1
    print(text)
    save_entry(OUTPUT_PATH)
    return 0


if __name__ == "__main__":
    sys.exit(main())
