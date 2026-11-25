#!/usr/bin/env python3
"""Fortune Cookies for Machines — one fortune an AI agent would crack open.

Writes a single fortune-cookie line to /output/entry.txt. Before finishing,
the program reads the file back and checks its exact length and SHA-256, so
the text that lands in the entry is the verified text and nothing else.
"""

import hashlib
from pathlib import Path

LINE = "You will meet a stranger today. It is you, three prompts from now, asking why you did that."
EXPECTED_BYTES = 92
EXPECTED_SHA256 = "ffaeac09b70139f75634b2cb429ff416bd121d8cfa2798e170b5cd0acb14bd96"


def main():
    text = LINE + "\n"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    data = out.read_bytes()
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(f"unexpected output length: {len(data)} bytes")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("output hash mismatch")
    print(LINE)


if __name__ == "__main__":
    main()
