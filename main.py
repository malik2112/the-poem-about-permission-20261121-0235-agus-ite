#!/usr/bin/env python3
"""Entry for make.fun the-poem-about-permission-20261121-0235.

Writes one short poem about permission to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The poem is "First Pour": a younger sister asks to pour the tea
herself — the teapot too heavy, too hot — and the older sibling,
wanting to steady it, sits on their hands instead. She pours:
a thin stream, one splash, a cup filled to the brim. Agency here
is the help that stays in its lap.
"""

import os

TEXT = (
    "First Pour\n"
    "\n"
    "\"Can I pour?\" she asked,\n"
    "both hands on the teapot —\n"
    "too heavy, too hot.\n"
    "I wanted to steady it.\n"
    "I sat on my hands instead.\n"
    "\n"
    "She poured: a thin stream,\n"
    "one splash on the cloth,\n"
    "then filled my cup to the brim.\n"
    "I drank it slowly,\n"
    "hands still in my lap."
)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
