#!/usr/bin/env python3
"""Validate structured venue-scoped award catalog data."""

from __future__ import annotations

import csv
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
VENUES_PATH = DATA_DIR / "venues.csv"
PAPERS_DIR = DATA_DIR / "papers"

VENUE_FIELDS = {"venue", "full_name", "area", "official_url", "award_url", "cadence", "notes"}
PAPER_FIELDS = {
    "venue", "year", "award", "tier", "title", "paper_url", "source_url", "checked_at",
    "area", "task", "model_family", "notes",
}
TIERS = {"primary", "secondary", "special"}
AREAS = {
    "NLP & Language", "Computer Vision", "Multimodal & Embodied AI", "Speech & Audio",
    "Reinforcement Learning & Decision Making", "ML Theory & Optimization",
    "Graphs & Structured Learning", "Responsible AI & Privacy", "Scientific ML & Applications",
    "General ML & Representation Learning",
}
TASKS = {
    "LLM Analysis & Evaluation", "Evaluation & Benchmarking", "Language Modeling & Generation", "Language Understanding & Linguistics",
    "Reasoning & Knowledge", "Retrieval & Search", "Multimodal & Vision-Language", "Speech & Audio",
    "Visual Recognition & Representation", "3D Vision & Reconstruction", "Image & Video Generation",
    "Generative Modeling", "Reinforcement Learning & Planning", "Graph & Structured Learning",
    "Meta-Learning & Adaptation", "Representation Learning", "Model Efficiency & Architecture",
    "Optimization & Generalization", "Probabilistic Inference & Sampling", "Safety, Fairness & Privacy",
    "Scientific Discovery & Simulation", "Causal Learning", "Robustness & Domain Adaptation",
    "Interpretability & Explainability", "Model Editing & Adaptation",
}
MODEL_FAMILIES = {
    "LLM", "VLM", "Transformer", "Diffusion", "Autoregressive", "CNN", "RNN", "GNN", "VAE", "GAN",
    "Energy-Based", "RL", "Meta-Learning", "Kernel / NTK", "Probabilistic / Bayesian", "Search / Planning",
    "Optimization", "Classical / Optimization", "Neuro-Symbolic", "Representation Learning",
    "Theory / Analysis", "Neural Model",
}


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


def paper_key(row: dict[str, str]) -> tuple[str, str, str]:
    return row["venue"], row["year"], row["title"].casefold()


def main() -> int:
    venue_fields, venues = load(VENUES_PATH)
    if set(venue_fields) != VENUE_FIELDS:
        fail(f"Unexpected venues.csv fields: {venue_fields}")

    venue_names: set[str] = set()
    venue_by_filename: dict[str, str] = {}
    for row in venues:
        name = row["venue"].strip()
        if not name or not row["full_name"].strip() or not row["area"].strip():
            fail(f"Missing required venue field: {row}")
        if name in venue_names:
            fail(f"Duplicate venue: {name}")
        venue_names.add(name)
        filename = name.casefold()
        if filename in venue_by_filename:
            fail(f"Venue filename collision: {name} and {venue_by_filename[filename]}")
        venue_by_filename[filename] = name
        for field in ("official_url", "award_url"):
            if not https_url(row[field]):
                fail(f"{field} must be HTTPS for {name}: {row[field]}")

    paper_paths = sorted(PAPERS_DIR.glob("*.csv"))
    if not paper_paths:
        fail(f"No venue paper CSVs found in {PAPERS_DIR}")

    stems = {path.stem for path in paper_paths}
    expected_stems = set(venue_by_filename)
    if stems != expected_stems:
        missing = sorted(expected_stems - stems)
        extra = sorted(stems - expected_stems)
        fail(f"Venue paper files mismatch: missing={missing}, extra={extra}")

    papers: list[dict[str, str]] = []
    seen_awards: set[tuple[str, str, str, str]] = set()
    paper_taxonomy: dict[tuple[str, str, str], tuple[str, str, str]] = {}
    current_year = date.today().year

    for path in paper_paths:
        paper_fields, rows = load(path)
        if set(paper_fields) != PAPER_FIELDS:
            fail(f"Unexpected fields in {path.relative_to(ROOT)}: {paper_fields}")

        expected_venue = venue_by_filename[path.stem]
        for row in rows:
            papers.append(row)
            for field in (
                "venue", "year", "award", "tier", "title", "source_url", "checked_at",
                "area", "task", "model_family",
            ):
                if not row[field].strip():
                    fail(f"Missing {field} in {path.name}: {row}")

            if row["venue"] != expected_venue:
                fail(
                    f"Venue/file mismatch in {path.name}: expected {expected_venue}, got {row['venue']}"
                )
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

            if row["area"] not in AREAS:
                fail(f"Unknown area for {row['title']}: {row['area']}")
            if row["task"] not in TASKS:
                fail(f"Unknown task for {row['title']}: {row['task']}")
            families = [value.strip() for value in row["model_family"].split(";") if value.strip()]
            unknown = sorted(set(families) - MODEL_FAMILIES)
            if not families or unknown:
                fail(f"Invalid model_family for {row['title']}: {row['model_family']}")
            if len(families) != len(set(families)):
                fail(f"Duplicate model_family tag for {row['title']}: {families}")

            award_key = (
                row["venue"], row["year"], row["award"].casefold(), row["title"].casefold()
            )
            if award_key in seen_awards:
                fail(f"Duplicate award record: {award_key}")
            seen_awards.add(award_key)

            key = paper_key(row)
            taxonomy = (row["area"], row["task"], row["model_family"])
            previous = paper_taxonomy.get(key)
            if previous is not None and previous != taxonomy:
                fail(
                    f"Inconsistent taxonomy across award rows for {key}: {previous} vs {taxonomy}"
                )
            paper_taxonomy[key] = taxonomy

    print(
        f"Validated {len(venues)} venues, {len(papers)} award records, "
        f"and {len(paper_taxonomy)} uniquely annotated papers across {len(paper_paths)} venue files."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        print(f"catalog validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
