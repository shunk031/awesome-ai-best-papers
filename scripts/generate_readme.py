#!/usr/bin/env python3
"""Generate README.md from data/venues.csv and data/papers.csv."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
VENUES_PATH = DATA_DIR / "venues.csv"
PAPERS_PATH = DATA_DIR / "papers.csv"
README_PATH = ROOT / "README.md"
TIER_ORDER = {"primary": 0, "secondary": 1, "special": 2}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def render() -> str:
    venues = load_csv(VENUES_PATH)
    papers = load_csv(PAPERS_PATH)
    by_venue: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in papers:
        by_venue[row["venue"]].append(row)

    years = [int(row["year"]) for row in papers]
    min_year, max_year = min(years), max(years)

    lines: list[str] = [
        "# Awesome AI Best Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)",
        "",
        "[![Catalog Check](https://github.com/shunk031/awesome-ai-best-papers/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/shunk031/awesome-ai-best-papers/actions/workflows/catalog-check.yml)",
        "",
        f"![Award records](https://img.shields.io/badge/award%20records-{len(papers)}-informational)",
        f"![Venues](https://img.shields.io/badge/venues-{len(venues)}-informational)",
        f"![Coverage](https://img.shields.io/badge/coverage-{min_year}%E2%80%93{max_year}-informational)",
        "",
        "<!-- This file is generated from data/*.csv by scripts/generate_readme.py. Do not edit it directly. -->",
        "",
        "A curated, source-backed catalog of paper awards from major AI, machine learning, computer vision, and natural language processing conferences.",
        "",
        "The repository is **data-driven**: [`data/papers.csv`](data/papers.csv) is the canonical award catalog, [`data/venues.csv`](data/venues.csv) defines venue metadata, and this README is regenerated deterministically.",
        "",
        "> **Freshness:** a conference year is added only after awards are announced. Conferences without a 2026 award announcement intentionally stop at the latest completed edition.",
        "",
        "## Scope",
        "",
        "The catalog tracks conference paper awards such as **Best Paper**, **Outstanding Paper**, **Marr Prize**, honorable mentions / runners-up, student-paper awards, and venue-specific paper-award categories. Award candidates, nominations, demos, workshops, dissertation awards, lifetime awards, and retrospective test-of-time awards are excluded by default.",
        "",
        "The v2 catalog prioritizes official conference sources. Historical records from the original list remain accessible through the [pre-revamp snapshot](https://github.com/shunk031/awesome-ai-best-papers/blob/1d33f4f2c39c53b6cec85816c6b3383334b8e913/README.md) while they are normalized into structured data.",
        "",
        "## Coverage",
        "",
        "| Venue | Area | Years in catalog | Records | Official awards |",
        "| --- | --- | ---: | ---: | --- |",
    ]

    for venue in venues:
        items = by_venue.get(venue["venue"], [])
        item_years = sorted({int(row["year"]) for row in items})
        year_label = "—"
        if item_years:
            year_label = str(item_years[0]) if len(item_years) == 1 else f"{item_years[0]}–{item_years[-1]}"
        lines.append(
            f'| [{venue["venue"]}]({venue["official_url"]}) | {venue["area"]} | {year_label} | '
            f'{len(items)} | [source]({venue["award_url"]}) |'
        )

    lines.extend([
        "",
        "## Latest awards",
        "",
        "This section shows the latest completed award year for each venue. The full historical catalog is in [`data/papers.csv`](data/papers.csv).",
        "",
    ])

    for venue in venues:
        items = by_venue.get(venue["venue"], [])
        if not items:
            continue
        latest_year = max(int(row["year"]) for row in items)
        latest = sorted(
            (row for row in items if int(row["year"]) == latest_year),
            key=lambda row: (
                TIER_ORDER.get(row["tier"], 99),
                row["award"].casefold(),
                row["title"].casefold(),
            ),
        )
        lines.extend([
            f'### {venue["venue"]} · {latest_year}',
            "",
            f'**{venue["full_name"]}** · [{venue["area"]}]({venue["official_url"]})',
            "",
        ])
        for row in latest:
            title_url = row["paper_url"] or row["source_url"]
            source_suffix = (
                f' · [award source]({row["source_url"]})'
                if row["paper_url"] and row["paper_url"] != row["source_url"]
                else ""
            )
            tier_suffix = "" if row["tier"] == "primary" else f' · `{row["tier"]}`'
            notes_suffix = f' — {row["notes"]}' if row["notes"] else ""
            lines.append(
                f'- **{row["award"]}** — [{row["title"]}]({title_url})'
                f'{source_suffix}{tier_suffix}{notes_suffix}'
            )
        lines.append("")

    lines.extend([
        "## Data and contributions",
        "",
        "To add or correct an award, edit the CSV data rather than this README. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for source requirements and tier definitions.",
        "",
        "```bash",
        "python scripts/validate_catalog.py",
        "python scripts/generate_readme.py",
        "python scripts/generate_readme.py --check",
        "```",
        "",
        "## References",
        "",
        "- [Best Paper Awards in Computer Science (Jeff Huang)](https://jeffhuang.com/best_paper_awards.html)",
        "- [ACL-family best paper awards](https://www.aclweb.org/aclwiki/Best_paper_awards)",
        "- [CVF best paper archive](https://www.thecvf.com/?page_id=413)",
        "",
        "## License",
        "",
        "The catalog continues the original repository's [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) dedication.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if README.md is stale.")
    args = parser.parse_args()

    rendered = render()
    if args.check:
        current = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""
        if current != rendered:
            print("README.md is stale. Run: python scripts/generate_readme.py", file=sys.stderr)
            return 1
        print("README.md is up to date.")
        return 0

    README_PATH.write_text(rendered, encoding="utf-8")
    print(f"Wrote {README_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
