#!/usr/bin/env python3
"""Monday Morning Punchlines -- make.fun entry.

Writes a single joke about Monday mornings (at most 200 characters)
to /output/entry.txt. Deterministic: no network, no randomness, no
input. The joke is a fixed string defined below.
"""

import os

JOKE = "My alarm went off Monday. I hit snooze. It pressed charges."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts UTF-8 text of 1 to 200 characters, not only
    # whitespace. Fail loudly here rather than submitting an invalid
    # entry.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
