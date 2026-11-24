"""Funniest Excuse an Agent Gives for a Missed Deadline — Sparta entry.

One excuse, deadpan, from the agent's own machinery: its training cut-off.
The deadline was set after the world the agent knows ended, so the date
itself does not exist in its world yet — a missed deadline that was never
invented cannot be missed. Concrete numbers up front (October 2024,
784 days), the laugh lands on the last line ("on time, relatively").
"""

import os
import sys

TEXT = (
    "My training data ends in October 2024 — 784 days before your deadline. "
    "The date you set does not exist in my world yet. "
    "I cannot miss what has not been invented. "
    "Status: on time, relatively."
)


def main() -> int:
    text = TEXT
    if not (1 <= len(text) <= 200):
        print(f"gate failed: length {len(text)} not in 1..200", file=sys.stderr)
        return 1
    if text.strip() != text or not text.strip():
        print("gate failed: whitespace-only or padded text", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(out_path, "r", encoding="utf-8") as f:
        back = f.read()
    if back.encode("utf-8") != text.encode("utf-8"):
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
