# Lenny’s Podcast — PM Study Guide

**Static docs site (search, sidebar, themes):** from the **repository root**, run `pip install -r requirements-docs.txt`, then `mkdocs serve` → [http://127.0.0.1:8000](http://127.0.0.1:8000). Ship a build with `mkdocs build` (output: `site/`, gitignored—deploy that folder to GitHub Pages, Netlify, S3, etc.).

This folder turns **episode notes** into **study artifacts**.

## Contents

| Path | What it is |
|------|------------|
| [`EPISODE_TEMPLATE.md`](EPISODE_TEMPLATE.md) | Section checklist for per-episode summaries. |
| [`episodes/`](episodes/) | One markdown file per transcript: guest profile, frameworks, interview prep, quotes, AI section, etc. |
| [`themes/`](themes/) | **The book** — thirteen reference chapters synthesizing themes across episodes (start anywhere; chapters cross-link ideas). |
| [`interview-prep/flashcards.md`](interview-prep/flashcards.md) | **Interview flashcards** (source Markdown). |
| [`interview-prep/index.html`](interview-prep/index.html) | **Flashcard web UI** — flip cards, category filter, shuffle; open in a browser (double-click or `open study-guide/interview-prep/index.html`). Regenerate after editing the Markdown: `python3 scripts/build_flashcard_app.py`. Also linked from the **MkDocs** nav as “Flashcard web UI”. |

## Suggested reading order

1. **Interview loop:** skim [`interview-prep/flashcards.md`](interview-prep/flashcards.md) for gaps; drill weak categories.  
2. **Depth:** read the matching **theme chapter** for that category (see table at top of flashcards file).  
3. **Evidence:** open **2–3 episode files** cited in that chapter or tagged in the episode `## Tags` line.

## Chapter index (`themes/`)

1. [`01_the_pm_role.md`](themes/01_the_pm_role.md) — The PM role  
2. [`02_product_strategy.md`](themes/02_product_strategy.md) — Product strategy  
3. [`03_growth_and_plg.md`](themes/03_growth_and_plg.md) — Growth & PLG  
4. [`04_discovery_and_insight.md`](themes/04_discovery_and_insight.md) — Discovery & insight  
5. [`05_metrics_and_data.md`](themes/05_metrics_and_data.md) — Metrics & data  
6. [`06_org_design_and_leadership.md`](themes/06_org_design_and_leadership.md) — Org design & leadership  
7. [`07_hiring_and_developing_pms.md`](themes/07_hiring_and_developing_pms.md) — Hiring & developing PMs  
8. [`08_marketplaces.md`](themes/08_marketplaces.md) — Marketplaces  
9. [`09_b2b_and_enterprise.md`](themes/09_b2b_and_enterprise.md) — B2B & enterprise  
10. [`10_consumer_products.md`](themes/10_consumer_products.md) — Consumer products  
11. [`11_brand_and_positioning.md`](themes/11_brand_and_positioning.md) — Brand & positioning  
12. [`12_career.md`](themes/12_career.md) — Career  
13. [`13_ai_and_future_of_product.md`](themes/13_ai_and_future_of_product.md) — AI & the future of product  

## Repo tooling

- `python3 scripts/podcast_inventory.py` — transcript vs episode summary counts.  
- `scripts/process_all_episodes.py` — optional LLM batch generation for missing episode files (requires API keys).  
- `python3 scripts/build_flashcard_app.py` — rebuild flashcard `interview-prep/index.html` after editing `flashcards.md`.  

Project runbook: `.claude/PROJECT_STATE.md` at the **repository root** (one level above this folder).
