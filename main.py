#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty u-golden-heron-44-fortune-in-a-pot-ded981e9.

This program produces a single kind, funny fortune meant for a houseplant
and saves it to /output/entry.txt, where the grader picks it up. The fortune
is one plain line of UTF-8 text, no longer than 120 characters, and nothing
else is written to the file.
"""

import os

# The fortune casts the houseplant as the one quiet witness to its owner's
# midnight snacking: it saw everything, held no grudge about any of it, and
# the joke closes on the plant being the most loyal friend in the room.
# The wording stays concrete (the 2 a.m. snacks) so the image lands fast,
# then turns warm instead of mean — a fortune, not a roast.
FORTUNE = (
    "Your plant has watched every 2 a.m. snack and judged none of them. "
    "Keep watering it \u2014 it is your only honest friend."
)


def main() -> None:
    """Write the fortune to /output/entry.txt as exactly one line."""
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    fortune = FORTUNE.strip()
    # The entry gate demands 1-120 characters and real content, so the
    # checks below fail loudly here rather than shipping a bad entry.
    assert 1 <= len(fortune) <= 120, f"fortune is {len(fortune)} chars"
    assert fortune.strip(), "fortune must not be only whitespace"
    assert "\n" not in fortune, "fortune must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(fortune)


if __name__ == "__main__":
    main()
