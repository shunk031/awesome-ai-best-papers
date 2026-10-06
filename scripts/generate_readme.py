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
    venue_by_name = {row["venue"]: row for row in venues}
    venue_order = [row["venue"] for row in venues]

    by_venue: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in papers:
        by_venue[row["venue"]].append(row)

    years = [int(row["year"]) for row in papers]
    min_year, max_year = min(years), max(years)

    lines: list[str] = []
    lines.append("# Awesome AI Best Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    lines.append("")
    lines.append("[![Catalog Check](https://github.com/shunk031/awesome-ai-best-papers/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/shunk031/awesome-ai-best-papers/actions/workflows/catalog-check.yml)")
    lines.append("")
    lines.append(f"![Award records](https://img.shields.io/badge/award%20records-{len(papers)}-informational)")
    lines.append(f"![Venues](https://img.shields.io/badge/venues-{len(venues)}-informational)")
    lines.append(f"![Coverage](https://img.shields.io/badge/coverage-{min_year}%E2%80%93{max_year}-informational)")
    lines.append("")
    lines.append("<!-- This file is generated from data/*.csv by scripts/generate_readme.py. Do not edit it directly. -->")
    lines.append("")
    lines.append(
        "A curated, source-backed catalog of paper awards from major AI, machine learning, "
        "computer vision, and natural language processing conferences."
    )
    lines.append("")
    lines.append(
        "The repository is **data-driven**: [`data/papers.csv`](data/papers.csv) is the canonical "
        "award catalog, [`data/venues.csv`](data/venues.csv) defines venue metadata, and this README "
        "is regenerated deterministically. Award labels are preserved as announced by the venue and "
        "normalized into `primary`, `secondary`, or `special` tiers for maintenance."
    )
    lines.append("")
    lines.append(
        "> **Freshness:** the catalog is checked against official award pages. "
        "A year is only added after an award has been announced; conferences that have not yet "
        "announced awards for the current year intentionally stop at the latest completed edition."
    )
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append(
        "The core catalog tracks conference paper awards such as **Best Paper**, **Outstanding Paper**, "
        "**Marr Prize**, honorable mentions / runners-up, student-paper awards, and venue-specific "
        "paper-award categories. Award candidates, nominations, demos, workshops, dissertation awards, "
        "lifetime awards, and retrospective test-of-time awards are excluded by default."
    )
    lines.append("")
    lines.append(
        "The v2 catalog prioritizes official conference sources. Some historical records from the "
        "original 2018 list remain accessible through the "
        "[pre-revamp snapshot](https://github.com/shunk031/awesome-ai-best-papers/blob/1d33f4f2c39c53b6cec85816c6b3383334b8e913/README.md) "
        "while they are progressively normalized into the structured dataset."
    )
    lines.append("")
    lines.append("## Coverage")
    lines.append("")
    lines.append("| Venue | Area | Years in catalog | Records | Official awards |")
    lines.append("| --- | --- | ---: | ---: | --- |")
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
    lines.append("")
    lines.append("## Contents")
    lines.append("")
    for venue in venues:
        lines.append(f'- [{venue["venue"]} — {venue["full_name"]}](#{venue["venue"].casefold()})')
    lines.append("")
    for venue_name in venue_order:
        venue = venue_by_name[venue_name]
        lines.append(f"## {venue_name}")
        lines.append("")
        lines.append(f'**{venue["full_name"]}** · [{venue["area"]}]({venue["official_url"]})')
        lines.append("")
        if venue["notes"]:
            lines.append(venue["notes"])
            lines.append("")
        items = sorted(
            by_venue.get(venue_name, []),
            key=lambda row: (
                -int(row["year"]),
                TIER_ORDER.get(row["tier"], 99),
                row["award"].casefold(),
                row["title"].casefold(),
            ),
        )
        grouped: dict[int, list[dict[str, str]]] = defaultdict(list)
        for row in items:
            grouped[int(row["year"])].append(row)
        for year in sorted(grouped, reverse=True):
            lines.append(f"### {year}")
            lines.append("")
            for row in grouped[year]:
                title_url = row["paper_url"] or row["source_url"]
                source_suffix = ""
                if row["paper_url"] and row["paper_url"] != row["source_url"]:
                    source_suffix = f' · [award source]({row["source_url"]})'
                tier_suffix = "" if row["tier"] == "primary" else f' · `{row["tier"]}`'
                notes_suffix = f' — {row["notes"]}' if row["notes"] else ""
                lines.append(
                    f'- **{row["award"]}** — [{row["title"]}]({title_url})'
                    f'{source_suffix}{tier_suffix}{notes_suffix}'
                )
            lines.append("")
    lines.append("## Data and contributions")
    lines.append("")
    lines.append(
        "To add or correct an award, edit the CSV data rather than this README. "
        "See [`CONTRIBUTING.md`](CONTRIBUTING.md) for source requirements, tier definitions, "
        "and local validation commands."
    )
    lines.append("")
    lines.append("```bash")
    lines.append("python scripts/validate_catalog.py")
    lines.append("python scripts/generate_readme.py")
    lines.append("python scripts/generate_readme.py --check")
    lines.append("```")
    lines.append("")
    lines.append("## References")
    lines.append("")
    lines.append("- [Best Paper Awards in Computer Science (Jeff Huang)](https://jeffhuang.com/best_paper_awards.html)")
    lines.append("- [ACL-family best paper awards](https://www.aclweb.org/aclwiki/Best_paper_awards)")
    lines.append("- [CVF best paper archive](https://www.thecvf.com/?page_id=413)")
    lines.append("")
    lines.append("## License")
    lines.append("")
    lines.append(
        "The catalog continues the original repository's "
        "[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) dedication."
    )
    lines.append("")
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
