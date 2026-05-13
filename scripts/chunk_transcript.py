#!/usr/bin/env python3
"""
Split a transcript .txt into overlapping chunks for LLM context limits.

Does not call any API — only produces numbered chunk files next to the source
or under a chosen output directory.

Usage:
  python3 scripts/chunk_transcript.py "path/to/Episode.txt" --max-chars 24000 --overlap 800
"""

from __future__ import annotations

import argparse
from pathlib import Path


def chunk_text(text: str, max_chars: int, overlap: int) -> list[str]:
    if max_chars <= 0:
        raise ValueError("max_chars must be positive")
    if overlap < 0 or overlap >= max_chars:
        raise ValueError("overlap must be in [0, max_chars)")

    chunks: list[str] = []
    start = 0
    n = len(text)
    while start < n:
        end = min(start + max_chars, n)
        chunks.append(text[start:end])
        if end >= n:
            break
        start = max(0, end - overlap)
    return chunks


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("transcript", type=Path, help="Path to .txt transcript")
    p.add_argument("--max-chars", type=int, default=24_000)
    p.add_argument("--overlap", type=int, default=800)
    p.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Directory for chunk files (default: alongside transcript)",
    )
    args = p.parse_args()

    path: Path = args.transcript.expanduser().resolve()
    if not path.is_file():
        raise SystemExit(f"Not a file: {path}")

    text = path.read_text(encoding="utf-8", errors="replace")
    parts = chunk_text(text, args.max_chars, args.overlap)

    out_dir = args.out_dir or path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = path.stem.replace(" ", "_")

    for i, part in enumerate(parts, start=1):
        out = out_dir / f"{stem}.chunk{i:03d}.txt"
        out.write_text(part, encoding="utf-8")
        print(out)


if __name__ == "__main__":
    main()
