## Operating principle

Do not rely on chat history. The repo is the source of truth.

Each work session:

1. Read this file.
2. Run `python3 scripts/podcast_inventory.py` if you add transcripts or episode files.
3. For **study**: start at [`study-guide/README.md`](../study-guide/README.md) (book + flashcards index).

Episode ingestion (if resuming transcript → summary work):

1. Process **missing** transcripts in strict **alphabetical order** (case-insensitive by `.txt` filename).
2. Write one episode summary per transcript into `study-guide/episodes/`.
3. Update **Progress** and **Last updated** after each batch.

---

## Repo layout

| Path | Purpose |
|------|---------|
| `study-guide/README.md` | **Start here:** index to episode corpus, book chapters, and flashcards. |
| `study-guide/themes/*.md` | **The book** — 13 synthesized reference chapters (incl. AI & future of product). |
| `study-guide/interview-prep/flashcards.md` | PM interview flashcards by question category. |
| `Lenny's Podcast Transcripts Archive [public] copy/*.txt` | Raw episode transcripts (only `.txt` counted). |
| `study-guide/episodes/*.md` | Generated episode summaries (quality bar: existing files + `EPISODE_TEMPLATE.md`). |
| `study-guide/EPISODE_TEMPLATE.md` | Section checklist aligned with project template. |
| `scripts/podcast_lib.py` | Shared paths + transcript→summary stem rules (used by other scripts). |
| `scripts/podcast_inventory.py` | Transcript vs summary inventory and “next missing” list. |
| `scripts/chunk_transcript.py` | Optional local chunking for very large `.txt` files. |
| `scripts/process_all_episodes.py` | **LLM batch run:** generates missing `study-guide/episodes/*.md` via Anthropic or OpenAI (requires API key + `pip install -r scripts/requirements-batch.txt`). |
| `mkdocs.yml` | [MkDocs](https://www.mkdocs.org/) + [Material](https://squidfunk.github.io/mkdocs-material/) config; `docs_dir` is `study-guide/`. |
| `requirements-docs.txt` | `mkdocs-material`, `mkdocs-awesome-pages-plugin` for the static site. |
| `site/` | **Build output** (`mkdocs build`) — gitignored; deploy or open `site/index.html` locally. |

Synthesis layer (complete): see `study-guide/themes/` and `study-guide/interview-prep/flashcards.md`. Narrated index: `study-guide/README.md`.

---

## Naming conventions

- **Transcripts**: source of truth is the `.txt` filename in the archive folder.
- **Summary files**: same guest/title stem as transcript, **spaces → underscores**, extension **`.md`**.
  - Example: `Ada Chen Rekhi.txt` → `Ada_Chen_Rekhi.md`
- **Multi-guest filenames**: only replace spaces; keep other characters as in the filename (e.g. `+` stays `+`).
- **Stem aliases** (transcript name → summary stem) live in `scripts/podcast_lib.py`:
  - `Alex Hardimen.txt` → `Alex_Hardiman.md` (transcript spelling)
  - `Andy Raskin_.txt` → `Andy_Raskin.md` (stray underscore in filename)
  - `April Dunford 2.0.txt` → `April_Dunford_2.md` (second episode; not `April_Dunford_2.0.md`)

---

## Episode summary template

Use the sections in `study-guide/EPISODE_TEMPLATE.md`, matching the depth and tone of existing episodes (e.g. `Ada_Chen_Rekhi.md`):

- `# [Guest Name(s)] — [Role / Company]`
- `## Guest Profile` (Name, Role/Company, Background)
- `## Tags` (inline backtick tags)
- `## TL;DR` (1–2 short paragraphs)
- `## Core Frameworks & Mental Models`
- `## Top Insights (Timeless)` (numbered)
- `## AI & The Changing PM Role` (or skip line noting not discussed)
- `## Notable Interview Questions Lenny Asked` (bullets)
- `## Best Quotes` (blockquote lines, only from transcript)
- `## Interview Prep Takeaways`
- `## Related Themes` (cross-episode theme strings)

**Quality rules:** Read the full transcript (chunk if needed, then synthesize). No invented facts. Prefer durable frameworks with memorable names when the guests provide them.

---

## Progress

| Metric | Count |
|--------|------:|
| Transcripts (`.txt`) | 321 |
| Episode summaries | 321 |
| Matched (transcript → summary, including aliases) | 321 |
| Missing summaries | 0 |

**Synthesis:** 13 chapters in `study-guide/themes/` (including `13_ai_and_future_of_product.md`); flashcards in `study-guide/interview-prep/flashcards.md`.

**Last updated:** 2026-05-11

---

## Next files to process (episode summaries)

None — corpus is complete. If new `.txt` files appear in the archive, re-run `python3 scripts/podcast_inventory.py` and use `scripts/process_all_episodes.py` or manual summaries for gaps.

---

## Known risks / constraints

- **ASR errors**: Guest or company names may be misspelled in `.txt` (e.g. “Hardimen”). Prefer transcript wording in quotes; correct well-known product names only when the audio intent is obvious and the transcript is inconsistent (document in summary if ambiguous).
- **Duplicate / versioned guests**: Filenames like `2.0` or `_2.0` may not map 1:1 to summary stems; aliases are maintained in `scripts/podcast_lib.py`.
- **Synthesis quality**: Theme chapters and flashcards aggregate episode notes; spot-check against primary sources when precision matters (interviews, metrics).
- **Dual guests**: Titles and file stems can be long; keep one summary file per transcript episode file.
- **Optional filename quirks**: e.g. `Casey Winters_.txt` — will map to `Casey_Winters_.md` unless we add an alias later.
