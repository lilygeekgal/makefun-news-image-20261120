#!/usr/bin/env python3
"""Deliver the make.fun entry image for news-image-20261120.

The entry is a one-page newspaper front page that sums up the world
news of Friday 20 November 2026, held in this repository as entry.png.
Running this file copies that picture, byte for byte, to the output
location make.fun expects: $MAKEFUN_OUTPUT_DIR/entry.png, falling back
to /output/entry.png when the variable is not set.

The copy is checked on the way: the source must start with the PNG
signature and declare a 1024 by 1024 image, and the bytes written out
must match the bytes read in. The program uses only the standard
library, never touches the network, and writes identical bytes on
every run.
"""

import os
import struct
import sys

# The eight bytes every PNG file opens with.
SIGNATURE = b"\x89PNG\r\n\x1a\n"
SIDE = 1024


def here():
    return os.path.dirname(os.path.abspath(__file__))


def source_file():
    return os.path.join(here(), "entry.png")


def target_file():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(folder, "entry.png")


def read_entry(path):
    with open(path, "rb") as handle:
        blob = handle.read()
    if blob[: len(SIGNATURE)] != SIGNATURE:
        raise ValueError(f"{path} does not start with a PNG signature")
    width, height = struct.unpack(">II", blob[16:24])
    if (width, height) != (SIDE, SIDE):
        raise ValueError(
            f"{path} is {width}x{height}, expected {SIDE}x{SIDE}")
    return blob


def run():
    try:
        blob = read_entry(source_file())
    except (OSError, ValueError) as problem:
        print(f"error: {problem}", file=sys.stderr)
        return 1
    target = target_file()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(blob)
    with open(target, "rb") as handle:
        written = handle.read()
    if len(written) != len(blob) or written != blob:
        print(f"error: {target} differs from the entry image",
              file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(blob)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(run())
