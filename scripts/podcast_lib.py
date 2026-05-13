"""
Shared paths and filename rules for Lenny transcript ↔ episode summary mapping.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "Lenny's Podcast Transcripts Archive [public] copy"
EPISODES = ROOT / "study-guide" / "episodes"
EPISODE_TEMPLATE = ROOT / "study-guide" / "EPISODE_TEMPLATE.md"

# Transcript filename -> summary stem when naive space-to-underscore mapping is wrong.
STEM_ALIASES: dict[str, str] = {
    "Alex Hardimen.txt": "Alex_Hardiman",
    "Andy Raskin_.txt": "Andy_Raskin",
    "April Dunford 2.0.txt": "April_Dunford_2",
}


def transcript_stem(filename: str) -> str:
    if not filename.endswith(".txt"):
        return filename.replace(" ", "_")
    base = filename[:-4]
    return base.replace(" ", "_")


def expected_summary_stem(transcript_filename: str) -> str:
    return STEM_ALIASES.get(transcript_filename, transcript_stem(transcript_filename))


def list_transcript_filenames() -> list[str]:
    return sorted([p.name for p in ARCHIVE.glob("*.txt")], key=str.lower)


def summary_stems() -> set[str]:
    return {p.stem for p in EPISODES.glob("*.md")}


def missing_episodes() -> list[tuple[str, str]]:
    """
    Episodes that have a transcript but no matching summary file.

    Returns (transcript_filename, summary_stem) sorted by transcript filename (case-insensitive).
    """
    stems = summary_stems()
    out: list[tuple[str, str]] = []
    for name in list_transcript_filenames():
        stem = expected_summary_stem(name)
        if stem not in stems:
            out.append((name, stem))
    return out


def episode_template_text() -> str:
    if EPISODE_TEMPLATE.is_file():
        return EPISODE_TEMPLATE.read_text(encoding="utf-8", errors="replace")
    return ""
