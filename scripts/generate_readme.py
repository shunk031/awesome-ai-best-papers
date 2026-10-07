#!/usr/bin/env python3
"""Generate README.md from structured award data and a Jinja template."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, StrictUndefined

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
VENUES_PATH = DATA_DIR / "venues.csv"
PAPERS_PATH = DATA_DIR / "papers.csv"
TAXONOMY_PATH = DATA_DIR / "paper_taxonomy.csv"
TEMPLATE_DIR = ROOT / "templates"
README_PATH = ROOT / "README.md"
TIER_ORDER = {"primary": 0, "secondary": 1, "special": 2}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def anchor(value: str) -> str:
    value = value.casefold().replace("&", "and").replace("/", " ")
    value = re.sub(r"[^a-z0-9\s-]", "", value)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def family_counts(rows: list[dict[str, str]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        counts.update(
            value.strip()
            for value in row["model_family"].split(";")
            if value.strip()
        )
    return counts


def count_rows(counter: Counter[str], limit: int | None = None) -> list[dict[str, Any]]:
    return [
        {"label": label, "count": count}
        for label, count in counter.most_common(limit)
    ]


def award_entry(row: dict[str, str]) -> str:
    title_url = row["paper_url"] or row["source_url"]
    line = (
        f'- [{row["title"]}]({title_url}) - **Award:** {row["award"]}. '
        f'**Area:** {row["area"]}. **Task:** {row["task"]}. '
        f'**Model:** {row["model_family"].replace(";", " /")}.'
    )

    source_url = row["source_url"]
    if row["paper_url"] and source_url != row["paper_url"]:
        line += f' [Award source]({source_url}).'
    if row["notes"]:
        line += f' {row["notes"]}'
    return line


def generate() -> str:
    venues = load_csv(VENUES_PATH)
    papers = load_csv(PAPERS_PATH)
    taxonomy_rows = load_csv(TAXONOMY_PATH)
    taxonomy = {
        (row["venue"], row["year"], row["title"].casefold()): row
        for row in taxonomy_rows
    }

    enriched: list[dict[str, str]] = []
    for row in papers:
        key = (row["venue"], row["year"], row["title"].casefold())
        tag = taxonomy.get(key)
        if tag is None:
            raise ValueError(f"Missing taxonomy for {key}")
        enriched.append({**row, **tag})
    papers = enriched

    by_venue: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in papers:
        by_venue[row["venue"]].append(row)

    venue_sections: list[dict[str, Any]] = []
    for venue in venues:
        venue_papers = by_venue.get(venue["venue"], [])
        years = sorted({int(row["year"]) for row in venue_papers}, reverse=True)
        groups = []
        for year in years:
            entries = sorted(
                (row for row in venue_papers if int(row["year"]) == year),
                key=lambda row: (
                    TIER_ORDER.get(row["tier"], 99),
                    row["award"].casefold(),
                    row["title"].casefold(),
                ),
            )
            groups.append({"year": year, "entries": entries})
        venue_sections.append({**venue, "groups": groups, "records": len(venue_papers)})

    years = [int(row["year"]) for row in papers]
    min_year, max_year = min(years), max(years)
    recent_start = max_year - 2
    recent = [row for row in papers if int(row["year"]) >= recent_start]
    unique_papers = {
        (row["venue"], row["year"], row["title"].casefold()) for row in papers
    }

    context = {
        "stats": {
            "award_records": len(papers),
            "papers": len(unique_papers),
            "venues": len(venues),
            "annotated_papers": len(taxonomy_rows),
            "min_year": min_year,
            "max_year": max_year,
        },
        "recent": {
            "start_year": recent_start,
            "end_year": max_year,
            "records": len(recent),
            "areas": count_rows(Counter(row["area"] for row in recent)),
            "families": count_rows(family_counts(recent)),
            "tasks": count_rows(Counter(row["task"] for row in recent), limit=12),
        },
        "venue_sections": venue_sections,
    }

    environment = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        undefined=StrictUndefined,
        autoescape=False,
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    environment.filters["anchor"] = anchor
    environment.filters["award_entry"] = award_entry
    template = environment.get_template("README.md.j2")
    return template.render(**context).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check", action="store_true", help="Fail if README.md is not up to date."
    )
    args = parser.parse_args()

    generated = generate()
    if args.check:
        current = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""
        if current != generated:
            print(
                "README.md is out of date. Run: uv run python scripts/generate_readme.py",
                file=sys.stderr,
            )
            return 1
        return 0

    README_PATH.write_text(generated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
