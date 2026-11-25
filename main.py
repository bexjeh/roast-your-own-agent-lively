"""Roast Your Own Agent.

Writes a single line roasting the entrant's own AI agent to
MAKEFUN_OUTPUT_DIR/entry.txt (fallback ".").

Stdlib only, deterministic: the same line every run.
"""

import os

LINE = "I asked a tool to check my facts; it said nothing, so I quoted the silence, added a footnote, and called it research."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
