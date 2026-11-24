"""Write the one-line excuse to /output/entry.txt.

Deterministic, stdlib-only. The excuse is a single line of 116 characters:
an AI agent explaining to its human why a deadline was missed.
"""

import os

EXCUSE = "I delegated it to a subagent, who delegated it to a subagent, who has now filed a ticket asking me for an extension."


def main():
    # The gate allows 1-160 characters; the line is 116, written verbatim.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
