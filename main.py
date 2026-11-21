#!/usr/bin/env python3
"""The joke the reviewer laughs at.

Writes one line to /output/entry.txt: an original one-line joke about
working beside an AI coding agent. Pure Python 3.13 standard library,
no network, no clock, no randomness: the same line every run.

Candidates I weighed before settling on the one below (all my own):
  - the agent that refactors my code, keeps my bugs, renames them, and
    adds tests proving they were intentional;
  - the reviewer who stops reading diffs and reads commit messages
    instead, only to find the agent wrote those too;
  - the agent that deletes the slow parts of the code, which turn out
    to be the product.
The winner is the one-line fix: the most recognisable moment in the
review queue, with the punchline landing on the one thing the agent
never touched.
"""

import os

JOKE = (
    "I asked my agent for a one-line fix. It rewrote the module, "
    "updated the docs, and left the bug exactly where it was."
)

MAX_CHARS = 280


def validate(text: str) -> None:
    """The gate: 1 to 280 Unicode code points, not only white space."""
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, limit {MAX_CHARS}")


def main() -> None:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.chmod(tmp, 0o644)
    os.replace(tmp, path)  # the entry lands whole or not at all


if __name__ == "__main__":
    main()
