"""The Moon Gets One Star: writes the one-star review to /output/entry.txt.

Why this line: a real review shape (rating, grievance, reason), Moon-specific,
and the punch lands on the Sun doing the actual work.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'One star. It turns up late, glows for free, and still gets poems written about it. The Sun does the actual work.'

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote entry.txt", len(ENTRY), "chars")


if __name__ == "__main__":
    main()
