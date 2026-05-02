# Economic Systems Research

A companion research infrastructure repository for the Economic Systems knowledge series.

This repository supports structured research on economic concepts, economic traditions, microeconomics, macroeconomics, political economy, development economics, ecological economics, public finance, labor systems, financial fragility, well-being indicators, beyond-GDP frameworks, article-roadmap planning, source hierarchy, citation workflows, and SQL-backed mapping of economic systems within sustainable systems.

It is designed as a clean scholarly infrastructure repository, not a full-stack application. SQL is the backbone. CSV files provide maintainable reference data. Python and R are used only for lightweight exports, audits, and indicator summaries.

## Quick Start with SQLite

```bash
sqlite3 economic_systems.db < sql/schema.sql
sqlite3 economic_systems.db < sql/seed_economic_systems.sql
sqlite3 economic_systems.db < sql/views.sql

python3 python/export_article_roadmap.py --db economic_systems.db --output outputs/article-roadmap.md
python3 python/source_audit.py --data-dir data --output outputs/source-audit.md
python3 python/export_indicator_map.py --db economic_systems.db --output outputs/indicator-map.md
Rscript r/economic_indicator_summary.R
```

## Repository Structure

- `articles/economic-systems/` — Article planning notes and pillar support
- `data/` — CSV metadata for domains, articles, concepts, traditions, indicators, and sources
- `docs/` — Methodology, source hierarchy, citation style, article template, and licensing notes
- `sql/` — Schema, seed data, and research views
- `python/` — Lightweight export and audit utilities
- `r/` — Lightweight indicator summaries
- `notebooks/` — Optional exploratory notebooks
- `outputs/` — Generated roadmaps and audits

## License

Code, SQL, and repository infrastructure are released under the MIT License. Original documentation and metadata are covered by `CONTENT_LICENSE.md`.
