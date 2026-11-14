#!/usr/bin/env python3
"""Molten Smash Burger — make.fun food-picture-01 entry.

The picture itself is food.jpg, shipped next to this script: a smash
burger photographed close up, molten cheddar dripping off a crispy-edged
patty under warm light. This program's only job is to carry that picture
to the grader, which reads its input from <output directory>/entry.png.

The destination keeps the name entry.png even though the bytes are
JPEG — the gate tells the formats apart from the leading bytes, and it
accepts either one.

Nothing beyond the Python standard library is used, so the sandbox runs
this with nothing installed.
"""

import os
import sys

ARTWORK = "food.jpg"
OUTPUT_NAME = "entry.png"
READ_SIZE = 512 * 1024


def artwork_location() -> str:
    """Where the shipped picture sits on disk."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, ARTWORK)


def transfer_bytes(origin: str, target: str) -> int:
    """Move every byte from origin to target; return how many moved."""
    moved = 0
    with open(origin, "rb") as incoming, open(target, "wb") as outgoing:
        while True:
            block = incoming.read(READ_SIZE)
            if not block:
                break
            outgoing.write(block)
            moved += len(block)
    return moved


def check_picture_header(origin: str) -> None:
    """Refuse early when the shipped bytes are neither JPEG nor PNG.

    The gate tells the formats apart from the leading bytes, so a
    source whose first bytes match neither is broken and should fail
    here, with a plain message, instead of being handed over.
    """
    with open(origin, "rb") as handle:
        head = handle.read(8)
    if head[:2] == b"\xff\xd8":
        return
    if head == b"\x89PNG\r\n\x1a\n":
        return
    print("food.jpg is neither JPEG nor PNG, refusing to deliver", file=sys.stderr)
    raise SystemExit(1)


def deliver_picture(origin: str, target: str) -> int:
    """Hand the picture over and check the handover landed whole.

    Returns the byte count. Stops with an error when the source is
    empty, or when the destination does not end up exactly the same
    size as the source.
    """
    total = os.path.getsize(origin)
    if total == 0:
        print("food.jpg is empty, nothing to hand over", file=sys.stderr)
        raise SystemExit(1)
    check_picture_header(origin)
    moved = transfer_bytes(origin, target)
    landed = os.path.getsize(target)
    if moved != total or landed != total:
        print(f"handoff short: {moved} of {total} bytes", file=sys.stderr)
        raise SystemExit(1)
    return moved


def run() -> int:
    origin = artwork_location()
    if not os.path.isfile(origin):
        print("food.jpg is not in the repository", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"cannot create output directory {out_dir}: {exc}", file=sys.stderr)
        return 1

    target = os.path.join(out_dir, OUTPUT_NAME)
    moved = deliver_picture(origin, target)
    print(f"wrote {target} ({moved} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
