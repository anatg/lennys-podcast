#!/usr/bin/env python3
"""
Parse study-guide/interview-prep/flashcards.md and emit a self-contained
study-guide/interview-prep/index.html (flip cards, keyboard shortcuts).

Usage:
  python3 scripts/build_flashcard_app.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD_PATH = ROOT / "study-guide" / "interview-prep" / "flashcards.md"
OUT_PATH = ROOT / "study-guide" / "interview-prep" / "index.html"

SKIP_SECTIONS = {"how to practice", "appendix: expand this deck"}

CARD_RE = re.compile(
    r"###\s+Card\s+\d+:\s*(.+?)\s*\n"
    r"\*\*Q:\*\*\s*(.+?)\s*\n"
    r"\*\*Answer:\*\*\s*(.+?)\s*\n"
    r"\*\*Insight:\*\*\s*(.+?)\s*\n"
    r"\*\*Story:\*\*\s*(.+?)(?=\n###\s+Card|\n##\s|\n---\s*$|\Z)",
    re.S | re.I,
)


def parse_cards(md: str) -> list[dict[str, str]]:
    md = md.replace("\r\n", "\n")
    sections = re.split(r"^##\s+(.+?)\s*$", md, flags=re.M)
    out: list[dict[str, str]] = []
    i = 1
    while i + 1 < len(sections):
        name = sections[i].strip()
        body = sections[i + 1]
        i += 2
        if name.lower() in SKIP_SECTIONS:
            continue
        if "### Card" not in body:
            continue
        for m in CARD_RE.finditer(body):
            title, q, answer, insight, story = (x.strip() for x in m.groups())
            out.append(
                {
                    "category": name,
                    "title": title,
                    "q": q,
                    "answer": answer,
                    "insight": insight,
                    "story": story,
                }
            )
    return out


def build_html(cards: list[dict[str, str]]) -> str:
    data = json.dumps(cards, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>PM Interview Flashcards</title>
  <style>
    :root {{
      --bg: #0f1419;
      --surface: #1a2332;
      --text: #e7ecf3;
      --muted: #8b9cb3;
      --accent: #5b8def;
      --accent-dim: #3d5a8a;
      --radius: 14px;
      --font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100dvh;
      font-family: var(--font);
      background: radial-gradient(1200px 600px at 50% -10%, #1e2a44 0%, var(--bg) 55%);
      color: var(--text);
      line-height: 1.45;
    }}
    .wrap {{
      max-width: 720px;
      margin: 0 auto;
      padding: 1.25rem 1rem 5rem;
    }}
    header {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      align-items: center;
      margin-bottom: 1rem;
    }}
    h1 {{
      font-size: 1.15rem;
      font-weight: 650;
      margin: 0;
      flex: 1 1 100%;
    }}
    label {{ font-size: 0.8rem; color: var(--muted); }}
    select {{
      background: var(--surface);
      color: var(--text);
      border: 1px solid #2a3a52;
      border-radius: 10px;
      padding: 0.45rem 0.65rem;
      font-size: 0.9rem;
      min-width: 220px;
    }}
    .toolbar {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      align-items: flex-end;
    }}
    button {{
      background: var(--surface);
      color: var(--text);
      border: 1px solid #2a3a52;
      border-radius: 10px;
      padding: 0.5rem 0.85rem;
      font-size: 0.88rem;
      cursor: pointer;
    }}
    button:hover {{ border-color: var(--accent-dim); }}
    button.primary {{
      background: linear-gradient(160deg, #4a7ae8, #355bb5);
      border-color: #4a6ec4;
      font-weight: 600;
    }}
    button.primary:hover {{ filter: brightness(1.06); }}
    .meta {{
      font-size: 0.8rem;
      color: var(--muted);
      margin: 0.35rem 0 0.75rem;
      width: 100%;
    }}
    .scene {{
      perspective: 1200px;
      margin-top: 0.5rem;
    }}
    .card {{
      position: relative;
      min-height: 300px;
      transform-style: preserve-3d;
      transition: transform 0.55s cubic-bezier(0.2, 0.8, 0.2, 1);
      cursor: pointer;
    }}
    .card.flipped {{ transform: rotateY(180deg); }}
    .face {{
      position: absolute;
      inset: 0;
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      border-radius: var(--radius);
      padding: 1.15rem 1.25rem;
      border: 1px solid #2a3a52;
      background: linear-gradient(165deg, #1c2738 0%, #151d2b 100%);
      box-shadow: 0 12px 40px rgba(0,0,0,0.35);
      overflow: auto;
    }}
    .face.back {{
      transform: rotateY(180deg);
    }}
    .tag {{
      display: inline-block;
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--accent);
      margin-bottom: 0.5rem;
    }}
    .card-title {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--muted);
      margin: 0 0 0.65rem;
    }}
    .q {{
      font-size: 1.2rem;
      font-weight: 600;
      margin: 0;
      line-height: 1.35;
    }}
    .back h3 {{
      margin: 0.85rem 0 0.35rem;
      font-size: 0.72rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--muted);
    }}
    .back h3:first-child {{ margin-top: 0; }}
    .back p {{
      margin: 0 0 0.5rem;
      font-size: 0.92rem;
      color: #dce4ef;
    }}
    .back p:last-child {{ margin-bottom: 0; }}
    .say-this {{
      background: rgba(91, 141, 239, 0.1);
      border-left: 3px solid var(--accent);
      border-radius: 6px;
      padding: 0.65rem 0.85rem;
      margin-bottom: 0.5rem;
    }}
    .say-this p {{
      margin: 0;
      font-size: 1.05rem;
      font-weight: 500;
      color: #e7ecf3;
      line-height: 1.4;
      font-style: italic;
    }}
    .hint {{
      margin-top: 0.75rem;
      font-size: 0.78rem;
      color: var(--muted);
    }}
    kbd {{
      font: 0.75rem monospace;
      padding: 0.1rem 0.35rem;
      border-radius: 4px;
      border: 1px solid #3a4a63;
      background: #151d2b;
    }}
    footer.nav {{
      position: fixed;
      left: 0;
      right: 0;
      bottom: 0;
      padding: 0.65rem 1rem calc(0.65rem + env(safe-area-inset-bottom));
      background: rgba(15, 20, 25, 0.92);
      backdrop-filter: blur(10px);
      border-top: 1px solid #243047;
      display: flex;
      gap: 0.5rem;
      justify-content: center;
      flex-wrap: wrap;
    }}
    a.source {{
      color: var(--accent);
      font-size: 0.8rem;
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <h1>PM interview flashcards</h1>
      <div class="toolbar">
        <div>
          <label for="cat">Category</label><br />
          <select id="cat" aria-label="Category"></select>
        </div>
        <button type="button" id="shuffle" title="Shuffle current filter">Shuffle</button>
        <button type="button" id="all" class="primary" title="All categories">All cards</button>
      </div>
      <p class="meta" id="progress"></p>
      <a class="source" href="./flashcards.md">Edit source: flashcards.md</a>
    </header>
    <div class="scene">
      <div class="card" id="flipCard" role="button" tabindex="0" aria-label="Flip card. Space to flip.">
        <div class="face front" id="front"></div>
        <div class="face back" id="back"></div>
      </div>
    </div>
    <p class="hint">Click card or <kbd>Space</kbd> to flip · <kbd>←</kbd> <kbd>→</kbd> prev/next</p>
  </div>
  <footer class="nav">
    <button type="button" id="prev">← Prev</button>
    <button type="button" id="flipBtn" class="primary">Flip</button>
    <button type="button" id="next">Next →</button>
  </footer>
  <script>
    const CARDS = {data};

    const catSel = document.getElementById("cat");
    const flipCard = document.getElementById("flipCard");
    const front = document.getElementById("front");
    const back = document.getElementById("back");
    const progress = document.getElementById("progress");

    let active = [...CARDS];
    let idx = 0;

    function categories() {{
      const s = new Set();
      CARDS.forEach((c) => s.add(c.category));
      return [...s].sort((a, b) => a.localeCompare(b));
    }}

    function rebuildCategorySelect() {{
      const cats = categories();
      catSel.innerHTML = '<option value="">All categories</option>';
      cats.forEach((c) => {{
        const o = document.createElement("option");
        o.value = c;
        o.textContent = c;
        catSel.appendChild(o);
      }});
    }}

    function escapeHtml(s) {{
      return s
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
    }}

    function fmtBold(s) {{
      return escapeHtml(s).replace(/\\*\\*(.+?)\\*\\*/g, "<strong>$1</strong>");
    }}

    function render() {{
      if (!active.length) {{
        front.innerHTML =
          '<span class="tag">Empty</span><p class="q">No cards match this filter.</p>';
        back.innerHTML = "";
        progress.textContent = "";
        flipCard.classList.remove("flipped");
        return;
      }}
      if (idx >= active.length) idx = 0;
      if (idx < 0) idx = active.length - 1;
      const c = active[idx];
      flipCard.classList.remove("flipped");
      front.innerHTML =
        '<span class="tag">' +
        escapeHtml(c.category) +
        "</span>" +
        '<p class="card-title">' +
        escapeHtml(c.title) +
        "</p>" +
        '<p class="q">' +
        escapeHtml(c.q) +
        "</p>";
      back.innerHTML =
        "<h3>Answer</h3><div class='say-this'><p>" +
        fmtBold(c.answer) +
        "</p></div><h3>Key insight</h3><p>" +
        fmtBold(c.insight) +
        "</p><h3>Story to use</h3><p>" +
        fmtBold(c.story) +
        "</p>";
      progress.textContent = idx + 1 + " / " + active.length + " · " + c.category;
    }}

    function applyFilter() {{
      const v = catSel.value;
      active = v ? CARDS.filter((c) => c.category === v) : [...CARDS];
      idx = 0;
      render();
    }}

    function shuffleDeck() {{
      const v = catSel.value;
      const pool = v ? CARDS.filter((c) => c.category === v) : [...CARDS];
      active = pool.slice();
      for (let i = active.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        const t = active[i];
        active[i] = active[j];
        active[j] = t;
      }}
      idx = 0;
      render();
    }}

    function go(delta) {{
      if (!active.length) return;
      idx = (idx + delta + active.length) % active.length;
      flipCard.classList.remove("flipped");
      render();
    }}

    function toggleFlip() {{
      flipCard.classList.toggle("flipped");
    }}

    document.getElementById("prev").addEventListener("click", () => go(-1));
    document.getElementById("next").addEventListener("click", () => go(1));
    document.getElementById("flipBtn").addEventListener("click", toggleFlip);
    flipCard.addEventListener("click", toggleFlip);
    flipCard.addEventListener("keydown", (e) => {{
      if (e.key === " " || e.key === "Enter") {{
        e.preventDefault();
        toggleFlip();
      }}
    }});

    document.getElementById("shuffle").addEventListener("click", shuffleDeck);
    document.getElementById("all").addEventListener("click", () => {{
      catSel.value = "";
      active = [...CARDS];
      idx = 0;
      render();
    }});

    catSel.addEventListener("change", applyFilter);

    document.addEventListener("keydown", (e) => {{
      if (e.target && (e.target.tagName === "SELECT" || e.target.tagName === "INPUT")) return;
      if (e.key === "ArrowRight") {{
        e.preventDefault();
        go(1);
      }}
      if (e.key === "ArrowLeft") {{
        e.preventDefault();
        go(-1);
      }}
      if (e.key === " ") {{
        e.preventDefault();
        toggleFlip();
      }}
    }});

    rebuildCategorySelect();
    active = [...CARDS];
    render();
  </script>
</body>
</html>
"""


def main() -> None:
    if not MD_PATH.is_file():
        print(f"Missing {MD_PATH}", file=sys.stderr)
        sys.exit(1)
    md = MD_PATH.read_text(encoding="utf-8")
    cards = parse_cards(md)
    if not cards:
        print("No cards parsed — check flashcards.md format.", file=sys.stderr)
        sys.exit(1)
    html = build_html(cards)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(html, encoding="utf-8")
    print(f"Wrote {len(cards)} cards -> {OUT_PATH}")


if __name__ == "__main__":
    main()
