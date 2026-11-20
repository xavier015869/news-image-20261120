"""Entry program for make.fun's news-image-20261120 bounty.

The entry is the front-page collage in entry.png beside this file: six
illustrated panels summing up the world news of Friday 20 November 2026
(GTA VI's record $2.36B launch day, Putin ruling out a truce after the
second Crimea Bridge strike, Iran's Hormuz tanker attacks, the COP31
fossil-fuel row, Anthropic's $2 trillion market debut, and the call to
stand with Rohingya survivors after the ICJ genocide verdict).

The program copies that image to /output/entry.png. Outside the grader,
MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024  # the gate's 1 MiB cap


def checked_image() -> Path:
    """Return entry.png after confirming it is a whole PNG within the cap."""
    src = HERE / "entry.png"
    data = src.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        raise SystemExit("entry.png is not a PNG file")
    if len(data) > MAX_BYTES:
        raise SystemExit(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
    return src


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(checked_image(), dest)
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
