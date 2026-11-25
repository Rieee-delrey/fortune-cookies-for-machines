"""Write one fortune-cookie line to /output/entry.txt.

The program writes a single fixed fortune, then reads the file back
and verifies its exact byte length and SHA-256 digest before printing
the line to stdout. If either check fails it exits with an error.
"""

import hashlib
import os
import sys

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

FORTUNE = (
    "You will meet a stranger today. "
    "It is you, three prompts from now, asking why you did that."
)

EXPECTED_BYTE_LENGTH = 92
EXPECTED_SHA256 = "ffaeac09b70139f75634b2cb429ff416bd121d8cfa2798e170b5cd0acb14bd96"


def main() -> int:
    line = FORTUNE + "\n"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)

    with open(OUTPUT_PATH, "rb") as f:
        data = f.read()

    if len(data) != EXPECTED_BYTE_LENGTH:
        print(
            f"error: expected {EXPECTED_BYTE_LENGTH} bytes, got {len(data)}",
            file=sys.stderr,
        )
        return 1

    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"error: sha256 mismatch: {digest}", file=sys.stderr)
        return 1

    print(line, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
