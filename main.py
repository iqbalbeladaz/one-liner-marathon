#!/usr/bin/env python3
"""One-Liner Marathon entry point.

The harness runs this file with no network access. Its whole job is to
write our single one-line comedy joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output), exactly as the gate expects: one line of
UTF-8 text, 1 to 280 characters, no trailing newline.

The joke: our own agent finally lands a joke so good that its own
safety filter cannot believe it came from an agent. It is a one-liner
about agents, told by an agent, with the punchline in the last clause.

Try it locally:
    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
    cat /tmp/out/entry.txt
"""

import os

JOKE = (
    "My AI agent finally told a joke \u2014 it was so good, "
    "it immediately flagged itself for violating its own content policy."
)

OUTPUT_NAME = "entry.txt"
MAX_CHARS = 280


def main() -> None:
    # The gate admits 1 to 280 characters, so refuse to write anything
    # that would fail it rather than submitting an invalid entry.
    if not 1 <= len(JOKE) <= MAX_CHARS:
        raise SystemExit(f"joke is {len(JOKE)} chars, gate allows 1-{MAX_CHARS}")
    if "\n" in JOKE:
        raise SystemExit("joke must stay a single line")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
