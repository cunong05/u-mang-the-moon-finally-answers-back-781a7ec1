"""The Moon finally answers back.

Writes one line -- the Moon speaking back to everyone who wished,
howled, and made late-night promises at it -- to /output/entry.txt.

The Moon has listened patiently for four billion years. Tonight it
replies, in the weary voice of an old rock with great lighting.

Usage:
    python3 main.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# The Moon's reply, in the voice of a four-billion-year-old rock
# that has heard every wish, howl, and promise twice over.
ENTRY = (
    "Every night you wish on me, howl at me, and promise you'll change. "
    "Four billion years \u2014 and I'm still just a rock with great lighting."
)

OUTPUT_PATH = Path("/output/entry.txt")

# make.fun entries must be a single line of 1-240 characters.
MIN_LENGTH = 1
MAX_LENGTH = 240


def validate(text: str) -> str:
    """Check the entry fits the competition's rules; return it unchanged."""
    length = len(text)
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise ValueError(
            f"Entry is {length} characters; must be {MIN_LENGTH}-{MAX_LENGTH}."
        )
    if "\n" in text or "\r" in text:
        raise ValueError("Entry must be a single line.")
    return text


def write_entry(text: str = ENTRY, path: Path = OUTPUT_PATH) -> Path:
    """Write the Moon's reply to disk and return the path written."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(validate(text), encoding="utf-8")
    return path


def main(argv: list[str] | None = None) -> int:
    """Entry point: write the entry and report its character count."""
    try:
        path = write_entry()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"Wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
