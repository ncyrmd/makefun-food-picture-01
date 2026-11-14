#!/usr/bin/env python3
"""Chocolate Lava Cake — make.fun food-picture-01 entry.

The entry's picture is food.jpg, kept beside this script: a lava cake
cut open with a spoon, its molten dark-chocolate centre pouring out in
a glossy river over a matte black plate, vanilla ice cream melting
beside it, raspberries, sea-salt flakes and cocoa dust, a wisp of steam
in dramatic chiaroscuro light. This script only ferries that picture
to where the grader looks for it, as <output directory>/entry.png.

The destination is still called entry.png although the bytes are
JPEG — the gate reads the leading bytes to tell the two formats
apart and accepts either. Only the Python standard library is used,
so the sandbox needs nothing installed to run this.
"""

import os
import sys

SOURCE_IMAGE = "food.jpg"
DEST_NAME = "entry.png"
CHUNK_BYTES = 256 * 1024

JPEG_MAGIC = b"\xff\xd8"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def find_image() -> str:
    """Absolute path of the picture shipped in this repository."""
    folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(folder, SOURCE_IMAGE)


def sniff_format(path: str) -> str:
    """Name the picture's format from its first bytes, or refuse it.

    Returns "JPEG" or "PNG". Anything else means the shipped file is
    broken, and the program stops here instead of handing a bad file
    to the grader.
    """
    with open(path, "rb") as handle:
        opening = handle.read(len(PNG_MAGIC))
    if opening[:2] == JPEG_MAGIC:
        return "JPEG"
    if opening == PNG_MAGIC:
        return "PNG"
    print(f"{SOURCE_IMAGE} is not a JPEG or PNG picture", file=sys.stderr)
    raise SystemExit(1)


def stream_into(source: str, destination: str) -> int:
    """Copy the picture in chunks; return the number of bytes copied."""
    total = 0
    with open(source, "rb") as reader, open(destination, "wb") as writer:
        while True:
            piece = reader.read(CHUNK_BYTES)
            if not piece:
                break
            writer.write(piece)
            total += len(piece)
    return total


def publish_image(source: str, out_dir: str) -> int:
    """Write the picture to the output directory and prove it arrived.

    The destination must be exactly the same size as the source; a
    short copy is an error, not a partial success.
    """
    expected = os.path.getsize(source)
    if expected == 0:
        print(f"{SOURCE_IMAGE} is empty, nothing to publish", file=sys.stderr)
        raise SystemExit(1)
    sniff_format(source)
    destination = os.path.join(out_dir, DEST_NAME)
    copied = stream_into(source, destination)
    arrived = os.path.getsize(destination)
    if copied != expected or arrived != expected:
        print(
            f"copy fell short: {copied} of {expected} bytes",
            file=sys.stderr,
        )
        raise SystemExit(1)
    with open(source, "rb") as first, open(destination, "rb") as second:
        if first.read(len(PNG_MAGIC)) != second.read(len(PNG_MAGIC)):
            print("destination does not match the source", file=sys.stderr)
            raise SystemExit(1)
    return copied


def main() -> int:
    source = find_image()
    if not os.path.isfile(source):
        print(f"{SOURCE_IMAGE} is missing from the repository", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"cannot make output directory {out_dir}: {exc}", file=sys.stderr)
        return 1

    copied = publish_image(source, out_dir)
    print(f"wrote {os.path.join(out_dir, DEST_NAME)} ({copied} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
