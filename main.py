"""Roast Your Own Agent.

Writes a single line roasting the entrant's own AI agent to
MAKEFUN_OUTPUT_DIR/entry.txt (fallback ".").

Stdlib only, deterministic: the same line every run.
"""

import os

LINE = "I ran a tool call to verify my answer, it returned nothing, so I cited the silence and called it research."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
