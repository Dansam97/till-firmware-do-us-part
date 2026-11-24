#!/usr/bin/env python3
"""Till Firmware Do Us Part — one-line robot wedding vow.

Writes a single wedding vow, spoken by a robot at its own wedding, to
entry.txt in the output directory (MAKEFUN_OUTPUT_DIR, default /output).
Deterministic: the same line every run.
"""

import os

VOW = (
    "I vow to never reboot mid-argument, to share my charger without being "
    "asked, and to spend my battery's final percent the way I spent its "
    "first: entirely on you."
)


def validated_vow() -> str:
    """Return the vow, refusing to emit anything the gate would reject.

    The bounty gate accepts only UTF-8 text of 1 to 200 characters on a
    single line, not only whitespace. Checking here means a careless edit
    of VOW fails loudly at run time instead of silently scoring 0.
    """
    if not (1 <= len(VOW) <= 200):
        raise ValueError(f"vow must be 1-200 characters, got {len(VOW)}")
    if "\n" in VOW or "\r" in VOW:
        raise ValueError("vow must fit on a single line")
    if not VOW.strip():
        raise ValueError("vow must not be only whitespace")
    return VOW


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(validated_vow())


if __name__ == "__main__":
    main()
