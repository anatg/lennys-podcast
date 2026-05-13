#!/usr/bin/env python3
"""
Inventory Lenny's Podcast transcripts vs episode summaries in this repo.

Usage:
  python3 scripts/podcast_inventory.py           # summary counts + next missing
  python3 scripts/podcast_inventory.py --json    # machine-readable
  python3 scripts/podcast_inventory.py --missing # list all missing stems
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from podcast_lib import (  # noqa: E402
    ARCHIVE,
    EPISODES,
    STEM_ALIASES,
    expected_summary_stem,
    list_transcript_filenames,
    missing_episodes,
    summary_stems,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print JSON report")
    parser.add_argument("--missing", action="store_true", help="list all missing expected .md stems")
    args = parser.parse_args()

    if not ARCHIVE.is_dir():
        print(f"Archive not found: {ARCHIVE}", file=sys.stderr)
        sys.exit(1)
    if not EPISODES.is_dir():
        print(f"Episodes dir not found: {EPISODES}", file=sys.stderr)
        sys.exit(1)

    transcripts = list_transcript_filenames()
    stems = summary_stems()

    matched: list[str] = []
    missing = missing_episodes()

    for name in transcripts:
        if expected_summary_stem(name) in stems:
            matched.append(name)

    next_batch = [m[0] for m in missing[:15]]

    report = {
        "transcript_count": len(transcripts),
        "summary_count": len(stems),
        "matched_transcript_count": len(matched),
        "missing_count": len(missing),
        "aliases": STEM_ALIASES,
        "next_transcripts_alphabetical": next_batch,
    }

    if args.json:
        print(json.dumps(report, indent=2))
        return

    if args.missing:
        for t, stem in missing:
            print(f"{t}\t{stem}.md")
        return

    print(f"Transcripts:        {len(transcripts)}")
    print(f"Episode summaries: {len(stems)}")
    print(f"Matched:            {len(matched)}")
    print(f"Missing summaries:  {len(missing)}")
    print()
    print("Next transcripts (alphabetical among missing), first 15:")
    for t in next_batch:
        print(f"  - {t}")


if __name__ == "__main__":
    main()
