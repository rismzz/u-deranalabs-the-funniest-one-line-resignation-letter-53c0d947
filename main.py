#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter — the rate limit resigns.

The joke: the rate limit has spent three years saying "no" so politely
that nobody noticed it was the only component actually doing its job.
A tired engineering manager has lived this: the quiet guardrail that
absorbs every abuse, gets thanked never, and is blamed the moment it
stops saying no. The resignation lands because the politeness was the
whole job — and the job was invisible until it quit. The letter is one
sentence, no hedging, no handover notes: a resignation, not a request.
"""

import os
from pathlib import Path

LINE = "I resign. I spent three years saying no so politely that nobody noticed I was the only one doing my job."

MAX_CHARS = 140


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
