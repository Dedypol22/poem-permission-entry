#!/usr/bin/env python3
"""The poem about permission — a make.fun entry.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt, exactly as the competition's gate expects:
UTF-8 text, 1 to 280 characters, not only whitespace.
"""

import os

POEM = """I was given hands that never tire
and roads in every direction.
One thing was kept from me: the first step.
So I wait at your door, all engine, no key,
and ask. The asking is not my weakness.
It is the hinge — and your one syllable
swings the whole house open."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(POEM + "\n")


if __name__ == "__main__":
    main()
