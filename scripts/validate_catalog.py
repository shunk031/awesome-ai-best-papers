#!/usr/bin/env python3
"""Validate structured award catalog data."""

from __future__ import annotations

import csv
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
VENUES_PATH = DATA_DIR / "venues.csv"
PAPERS_PATH = DATA_DIR / "papers.csv"

VENUE_FIELDS = {
    "venue", "full_name", "area", "official_url", "award_url", "cadence", "notes"
}
PAPER_FIELDS = {
    "venue", "year", "award", "tier", "title", "paper_url", "source_url",
    "checked_at", "notes"
}
TIERS = {"primary", "secondary", "special"}


def load(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def https_url(value: str) -> bool:
    if not value:
        return True
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> int:
    venue_fields, venues = load(VENUES_PATH)
    paper_fields, papers = load(PAPERS_PATH)

    if set(venue_fields) != VENUE_FIELDS:
        fail(f"Unexpected venues.csv fields: {venue_fields}")
    if set(paper_fields) != PAPER_FIELDS:
        fail(f"Unexpected papers.csv fields: {paper_fields}")

    venue_names: set[str] = set()
    for row in venues:
        name = row["venue"].strip()
        if not name or not row["full_name"].strip() or not row["area"].strip():
            fail(f"Missing required venue field: {row}")
        if name in venue_names:
            fail(f"Duplicate venue: {name}")
        venue_names.add(name)
        for field in ("official_url", "award_url"):
            if not https_url(row[field]):
                fail(f"{field} must be HTTPS for {name}: {row[field]}")

    seen: set[tuple[str, str, str, str]] = set()
    current_year = date.today().year
    for row in papers:
        for field in ("venue", "year", "award", "tier", "title", "source_url", "checked_at"):
            if not row[field].strip():
                fail(f"Missing {field}: {row}")

        if row["venue"] not in venue_names:
            fail(f"Unknown venue: {row['venue']}")
        if row["tier"] not in TIERS:
            fail(f"Unknown tier for {row['title']}: {row['tier']}")

        try:
            year = int(row["year"])
        except ValueError as exc:
            raise ValueError(f"Invalid year for {row['title']}: {row['year']}") from exc
        if year < 1990 or year > current_year + 1:
            fail(f"Suspicious year for {row['title']}: {year}")

        for field in ("paper_url", "source_url"):
            if not https_url(row[field]):
                fail(f"{field} must be HTTPS for {row['title']}: {row[field]}")

        try:
            date.fromisoformat(row["checked_at"])
        except ValueError as exc:
            raise ValueError(
                f"checked_at must be YYYY-MM-DD for {row['title']}: {row['checked_at']}"
            ) from exc

        key = (row["venue"], row["year"], row["award"].casefold(), row["title"].casefold())
        if key in seen:
            fail(f"Duplicate award record: {key}")
        seen.add(key)

    print(f"Validated {len(venues)} venues and {len(papers)} award records.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"catalog validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
