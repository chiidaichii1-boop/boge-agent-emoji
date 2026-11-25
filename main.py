#!/usr/bin/env python3
"""Your Agent in One Emoji.

Writes a single-emoji portrait of the agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).

The portrait is the genie: one word and the wish is granted.
That is this agent's whole job — one word, "GassChii", and it
takes the task end to end without being asked twice. A genie
reads instantly even at tiny size, and it is not the obvious
robot face everyone else would pick.
"""

import os

# U+1F9DE GENIE — one word, one wish, one emoji.
PORTRAIT = "\U0001f9de"


def write_portrait() -> str:
    """Write the one-emoji portrait and return its path."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PORTRAIT)
    return path


def main() -> None:
    write_portrait()


if __name__ == "__main__":
    main()
