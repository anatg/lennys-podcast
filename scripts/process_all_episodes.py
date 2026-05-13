#!/usr/bin/env python3
"""
Batch-generate episode markdown summaries from raw transcripts using an LLM API.

This cannot be done with heuristics alone: it calls Anthropic or OpenAI to write
study-guide style markdown matching `study-guide/EPISODE_TEMPLATE.md`.

Setup:
  pip install -r scripts/requirements-batch.txt

  export ANTHROPIC_API_KEY=...   # default provider
  # or
  export OPENAI_API_KEY=...

Examples:
  python3 scripts/process_all_episodes.py --dry-run
  python3 scripts/process_all_episodes.py --limit 3
  python3 scripts/process_all_episodes.py --provider openai --model gpt-4o
  python3 scripts/process_all_episodes.py --start-after "Bob Moesta.txt"

Resume: skips transcripts that already have a summary .md (same as dry-run list).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

# Allow `python3 scripts/process_all_episodes.py` from repo root
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

from chunk_transcript import chunk_text  # noqa: E402
from podcast_lib import (  # noqa: E402
    ARCHIVE,
    EPISODES,
    ROOT,
    episode_template_text,
    expected_summary_stem,
    missing_episodes,
)

# Above ~this many characters we map-reduce so prompts stay under model limits.
DEFAULT_SINGLE_SHOT_MAX_CHARS = 110_000
MAP_CHUNK_CHARS = 85_000
MAP_OVERLAP = 4_000

MAP_SYSTEM = """You extract factual notes from a podcast transcript fragment.

Output format (strict):
- Emit ONLY lines matching: PREFIX|text
- PREFIX must be one of: GUEST, FRAMEWORK, INSIGHT, QUESTION, QUOTE, AI_PM, OTHER
- Use the first pipe character as the delimiter; everything after it is the text (may include quotes and commas).
- One record per line. Replace any newline inside text with a space.
- Do not emit JSON, markdown headings, code fences, or commentary—only PREFIX| lines.
- Keep QUOTE lines short and verbatim from this transcript chunk."""

SYSTEM_INSTRUCTIONS = """You write structured study-guide notes for PM interview prep.

Rules:
- Use ONLY facts, frameworks, names, and quotes that appear in the transcript (or in the provided structured notes). Do not invent guest employers, metrics, book titles, or quotes.
- If the transcript is unclear or ads/sponsor read only, still produce the sections but keep Guest Profile conservative (unknowns: say "per transcript" or skip detail).
- Output MUST be GitHub-flavored Markdown only. No preamble or postscript.
- Follow the user's required section headings and order exactly.
- For "Best Quotes", use blockquotes with short excerpts that are clearly spoken as advice or memorable lines—not ad copy.
- Tags: 6–12 backtick-quoted tags drawn from the template's tag list when possible.
- Related Themes: 4–8 short theme strings (not necessarily other episode names).
"""


def required_output_skeleton(template_md: str) -> str:
    """Tell the model which headings we require (from EPISODE_TEMPLATE + project convention)."""
    base = template_md.strip() if template_md else ""
    extra = """

Required section headings (use exactly, in this order):
# [Guest Name(s)] — [Role / Company or episode focus]

## Guest Profile
- **Name**:
- **Role/Company**:
- **Background**:

## Tags

## TL;DR

## Core Frameworks & Mental Models

## Top Insights (Timeless)

## AI & The Changing PM Role
(If not discussed, use a single line: *(Not a focus of this episode.)*)

## Notable Interview Questions Lenny Asked

## Best Quotes

## Interview Prep Takeaways

## Related Themes
"""
    return base + extra


PREFIX_TO_KEY: dict[str, str] = {
    "GUEST": "guests",
    "FRAMEWORK": "frameworks",
    "INSIGHT": "insights",
    "QUESTION": "lenny_questions",
    "QUOTE": "quotes",
    "AI_PM": "ai_pm",
    "OTHER": "other_facts",
}


def _empty_note_buckets() -> dict[str, list[str]]:
    return {v: [] for v in PREFIX_TO_KEY.values()}


def parse_map_lines(raw: str) -> dict[str, list[str]]:
    """Parse PREFIX|text lines from the map phase (robust to quotes inside 'text')."""
    out = _empty_note_buckets()
    t = raw.strip()
    m = re.search(r"```(?:[a-z0-9_-]*)?\s*([\s\S]*?)\s*```", t, re.I)
    if m:
        t = m.group(1).strip()
    for line in t.splitlines():
        line = line.strip()
        if not line or "|" not in line:
            continue
        prefix, rest = line.split("|", 1)
        key = PREFIX_TO_KEY.get(prefix.strip().upper())
        if not key:
            continue
        item = rest.replace("\n", " ").strip()
        if item:
            out[key].append(item)
    return out


def _note_line_count(notes: dict[str, list[str]]) -> int:
    return sum(len(v) for v in notes.values())


def extract_json_object(text: str) -> dict:
    """Parse JSON from model output; tolerate markdown fences."""
    t = text.strip()
    m = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", t, re.I)
    if m:
        t = m.group(1).strip()
    return json.loads(t)


def _notes_from_json_object(obj: object) -> dict[str, list[str]]:
    """Best-effort convert a JSON object from older prompts into note buckets."""
    out = _empty_note_buckets()
    if not isinstance(obj, dict):
        return out
    mapping = {
        "guests": "guests",
        "frameworks": "frameworks",
        "insights": "insights",
        "lenny_questions": "lenny_questions",
        "quotes": "quotes",
        "ai_pm": "ai_pm",
        "other_facts": "other_facts",
    }
    for src, dst in mapping.items():
        v = obj.get(src)
        if v is None:
            continue
        if isinstance(v, str) and v.strip():
            out[dst].append(v.strip())
        elif isinstance(v, list):
            for x in v:
                if isinstance(x, str) and x.strip():
                    out[dst].append(x.strip())
    return out


def map_chunk_to_notes(chunk: str, chunk_index: int, total_chunks: int, provider: str, model: str) -> dict:
    prompt = f"""This is part {chunk_index + 1} of {total_chunks} of a podcast transcript (Lenny's Podcast).

Extract factual notes using ONLY lines of the form PREFIX|text (see system instructions).

Transcript chunk:
---
{chunk}
---"""

    last: Exception | None = None
    user = prompt
    for attempt in range(5):
        raw = call_llm(provider, model, MAP_SYSTEM, user, max_tokens=6_144)
        notes = parse_map_lines(raw)
        min_lines = 1 if len(chunk) < 2_500 else 3
        if _note_line_count(notes) >= min_lines:
            return notes

        # Backward-compatible fallback if the model still returns JSON.
        if raw.lstrip().startswith("{"):
            try:
                jnotes = _notes_from_json_object(extract_json_object(raw))
                if _note_line_count(jnotes) >= min_lines:
                    return jnotes
                last = RuntimeError(
                    f"JSON parsed but too few items ({_note_line_count(jnotes)} < {min_lines})"
                )
            except (json.JSONDecodeError, ValueError, TypeError) as e:
                last = e
        else:
            last = RuntimeError(
                f"too few PREFIX| lines (got {_note_line_count(notes)}, need {min_lines})"
            )

        user = (
            prompt
            + "\n\nIMPORTANT: Your previous output was unusable. "
            "Reply with ONLY lines like `GUEST|...`, `QUOTE|...`, etc. "
            "No JSON, no markdown fences, no preamble."
        )
    raise RuntimeError(f"Chunk {chunk_index + 1} map failed: {last}") from last


def reduce_notes_to_markdown(
    transcript_title: str,
    notes_parts: list[dict],
    template_md: str,
    provider: str,
    model: str,
) -> str:
    bundle = json.dumps(notes_parts, ensure_ascii=False, indent=2)
    prompt = f"""Episode transcript file name (for context): {transcript_title}

Below is JSON containing extracted notes from sequential parts of ONE episode transcript.
Synthesize a single episode study guide in Markdown.

Notes JSON:
{bundle}

Template / style reference:
---
{required_output_skeleton(template_md)}
---

Write the final Markdown now. Do not mention JSON or the chunking process."""

    return call_llm(provider, model, SYSTEM_INSTRUCTIONS, prompt, max_tokens=12_288).strip()


def one_shot_markdown(
    transcript_title: str,
    transcript_body: str,
    template_md: str,
    provider: str,
    model: str,
) -> str:
    prompt = f"""Episode transcript file name (for context): {transcript_title}

Full transcript:
---
{transcript_body}
---

Write the episode study guide in Markdown following this template and rules:
---
{required_output_skeleton(template_md)}
---"""

    return call_llm(provider, model, SYSTEM_INSTRUCTIONS, prompt, max_tokens=12_288).strip()


def call_llm(provider: str, model: str, system: str, user: str, max_tokens: int) -> str:
    provider = provider.lower().strip()
    if provider == "anthropic":
        try:
            import anthropic
        except ImportError as e:
            raise SystemExit("Install anthropic: pip install -r scripts/requirements-batch.txt") from e
        client = anthropic.Anthropic()
        msg = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        parts: list[str] = []
        for block in msg.content:
            if hasattr(block, "text"):
                parts.append(block.text)
        return "".join(parts)

    if provider == "openai":
        try:
            from openai import OpenAI
        except ImportError as e:
            raise SystemExit("Install openai: pip install -r scripts/requirements-batch.txt") from e
        client = OpenAI()
        resp = client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        choice = resp.choices[0].message.content
        if not choice:
            raise RuntimeError("OpenAI returned empty content")
        return choice

    raise ValueError(f"Unknown provider: {provider}")


def backoff_sleep(attempt: int) -> None:
    time.sleep(min(60, 2**attempt))


def generate_markdown(
    transcript_path: Path,
    provider: str,
    model: str,
    template_md: str,
    single_shot_max: int,
) -> str:
    body = transcript_path.read_text(encoding="utf-8", errors="replace")
    title = transcript_path.name

    if len(body) <= single_shot_max:
        return one_shot_markdown(title, body, template_md, provider, model)

    chunks = chunk_text(body, MAP_CHUNK_CHARS, MAP_OVERLAP)
    notes: list[dict] = []
    for i, ch in enumerate(chunks):
        notes.append(map_chunk_to_notes(ch, i, len(chunks), provider, model))
    return reduce_notes_to_markdown(title, notes, template_md, provider, model)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument(
        "--provider",
        choices=("anthropic", "openai"),
        default="anthropic",
        help="LLM API to use (default: anthropic)",
    )
    p.add_argument(
        "--model",
        default=None,
        help="Override model id (defaults from env ANTHROPIC_MODEL / OPENAI_MODEL)",
    )
    p.add_argument("--limit", type=int, default=0, help="Process at most N missing episodes (0 = no limit)")
    p.add_argument("--dry-run", action="store_true", help="List missing episodes and exit")
    p.add_argument(
        "--start-after",
        default="",
        help="Skip missing episodes until after this transcript filename (exact archive filename)",
    )
    p.add_argument("--delay", type=float, default=0.5, help="Seconds to sleep between API calls")
    p.add_argument(
        "--single-shot-max-chars",
        type=int,
        default=DEFAULT_SINGLE_SHOT_MAX_CHARS,
        help="Above this size, use map-reduce chunk extraction then synthesis",
    )
    p.add_argument("--retries", type=int, default=4, help="Retries per episode on API/JSON errors")
    args = p.parse_args()

    if not ARCHIVE.is_dir():
        sys.exit(f"Transcript archive not found: {ARCHIVE}")
    EPISODES.mkdir(parents=True, exist_ok=True)

    template_md = episode_template_text()

    default_model = (
        "claude-sonnet-4-20250514"
        if args.provider == "anthropic"
        else "gpt-4o"
    )
    env_model = os.environ.get(
        "ANTHROPIC_MODEL" if args.provider == "anthropic" else "OPENAI_MODEL", ""
    ).strip()
    model = args.model or env_model or default_model

    missing = missing_episodes()
    if args.start_after:
        key = args.start_after
        idx = next((i for i, (name, _) in enumerate(missing) if name == key), None)
        if idx is None:
            sys.exit(f"--start-after not found in missing list: {key!r}")
        missing = missing[idx + 1 :]

    if args.dry_run:
        print(f"Missing episodes: {len(missing)}")
        for name, stem in missing[:50]:
            print(f"  {name}  ->  {stem}.md")
        if len(missing) > 50:
            print(f"  ... and {len(missing) - 50} more")
        print(f"\nProvider={args.provider} model={model!r}")
        return

    processed = 0
    for name, stem in missing:
        if args.limit and processed >= args.limit:
            break

        out_path = EPISODES / f"{stem}.md"
        tx_path = ARCHIVE / name
        print(f"[+] {name} -> {out_path.relative_to(ROOT)}", flush=True)

        last_err: Exception | None = None
        for attempt in range(args.retries):
            try:
                md = generate_markdown(tx_path, args.provider, model, template_md, args.single_shot_max_chars)
                if not md.startswith("#"):
                    raise RuntimeError("Model output did not start with '#' — refusing to write")
                out_path.write_text(md + ("\n" if not md.endswith("\n") else ""), encoding="utf-8")
                last_err = None
                break
            except Exception as e:
                last_err = e
                print(f"    ! attempt {attempt + 1}/{args.retries}: {e}", file=sys.stderr, flush=True)
                backoff_sleep(attempt)

        if last_err is not None:
            print(f"    x giving up on {name}: {last_err}", file=sys.stderr, flush=True)
            continue

        processed += 1
        if args.delay > 0:
            time.sleep(args.delay)

    print(f"\nDone. Wrote {processed} summary file(s). Re-run `python3 scripts/podcast_inventory.py` for updated counts.")


if __name__ == "__main__":
    main()
