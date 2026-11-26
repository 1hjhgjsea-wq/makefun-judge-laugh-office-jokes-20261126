#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes.

Writes one funny line about office life to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

JOKE = (
    "My calendar said 'in a meeting' for eight hours straight, and nobody "
    "questioned it - in this office, being unavailable is the closest "
    "thing to a promotion."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-199 UTF-8 characters, not only whitespace."""
    if not (1 <= len(text) <= 199):
        raise ValueError(f"entry must be 1-199 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
