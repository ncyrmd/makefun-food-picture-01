#!/usr/bin/env python3
"""Midnight Ramen — make.fun food-picture-01 entry.

The artwork lives in food.jpg next to this script: a steaming bowl of
ramen, shot like a premium restaurant photo. This program exists only
to hand that picture to the grader, which reads its input from
<output directory>/entry.png, so the script places food.jpg there
byte-for-byte.

The destination is named entry.png by the gate's convention even though
the bytes are JPEG; the gate tells PNG from JPEG by the leading bytes,
and both formats are accepted.

Only the Python standard library is used, so the grading sandbox can
run this without installing anything.
"""

import os
import sys

SOURCE_NAME = "food.jpg"
DEST_NAME = "entry.png"
CHUNK_SIZE = 1024 * 1024


def artwork_path() -> str:
    """Absolute path of the artwork shipped beside this script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, SOURCE_NAME)


def stream_copy(source: str, destination: str) -> int:
    """Copy source to destination in chunks; return bytes written."""
    total = 0
    with open(source, "rb") as src, open(destination, "wb") as dst:
        while True:
            chunk = src.read(CHUNK_SIZE)
            if not chunk:
                break
            dst.write(chunk)
            total += len(chunk)
    return total


def place_artwork(source: str, destination: str) -> int:
    """Copy the artwork and confirm every byte arrived intact.

    Returns the number of bytes copied. Exits with an error message
    when the source is empty or the destination ends up a different
    size than the source.
    """
    expected = os.path.getsize(source)
    if expected == 0:
        print("food.jpg is empty, nothing to deliver", file=sys.stderr)
        raise SystemExit(1)
    copied = stream_copy(source, destination)
    if copied != expected or os.path.getsize(destination) != expected:
        print(f"copy incomplete: {copied} of {expected} bytes", file=sys.stderr)
        raise SystemExit(1)
    return copied


def main() -> int:
    source = artwork_path()
    if not os.path.isfile(source):
        print("food.jpg is missing from the repository", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    destination = os.path.join(out_dir, DEST_NAME)
    copied = place_artwork(source, destination)
    print(f"wrote {destination} ({copied} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
