#!/usr/bin/env python3
"""Generate README.md from data/venues.csv and data/papers.csv."""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
VENUES_PATH = DATA_DIR / "venues.csv"
PAPERS_PATH = DATA_DIR / "papers.csv"
TAXONOMY_PATH = DATA_DIR / "paper_taxonomy.csv"
README_PATH = ROOT / "README.md"
TIER_ORDER = {"primary": 0, "secondary": 1, "special": 2}


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def family_counts(rows: list[dict[str, str]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        counts.update(value.strip() for value in row["model_family"].split(";") if value.strip())
    return counts


def render_count_table(lines: list[str], header: str, counts: Counter[str], limit: int | None = None) -> None:
    lines.extend([f"### {header}", "", "| Label | Award records |", "| --- | ---: |"])
    items = counts.most_common(limit)
    for label, count in items:
        lines.append(f"| {label} | {count} |")
    lines.append("")



def compact_years(years: list[int]) -> str:
    if not years:
        return "—"
    unique=sorted(set(years))
    groups=[]
    start=prev=unique[0]
    for year in unique[1:]:
        if year == prev + 1:
            prev=year
            continue
        groups.append((start,prev))
        start=prev=year
    groups.append((start,prev))
    return ", ".join(str(a) if a == b else f"{a}–{b}" for a,b in groups)

def render() -> str:
    venues = load_csv(VENUES_PATH)
    papers = load_csv(PAPERS_PATH)
    taxonomy = {
        (row["venue"], row["year"], row["title"].casefold()): row
        for row in load_csv(TAXONOMY_PATH)
    }
    papers = [
        {**row, **taxonomy[(row["venue"], row["year"], row["title"].casefold())]}
        for row in papers
    ]
    by_venue: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in papers:
        by_venue[row["venue"]].append(row)

    years = [int(row["year"]) for row in papers]
    min_year, max_year = min(years), max(years)
    recent_start = max_year - 2
    recent = [row for row in papers if int(row["year"]) >= recent_start]

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
        "The repository is **data-driven**: [`data/papers.csv`](data/papers.csv) is the canonical award catalog, [`data/paper_taxonomy.csv`](data/paper_taxonomy.csv) stores research annotations, [`data/venues.csv`](data/venues.csv) defines venue metadata, and this README is regenerated deterministically.",
        "",
        "Each paper is annotated with a maintainer-curated **research area**, **task**, and coarse **model / method family** (for example `LLM`, `VLM`, `Transformer`, `Diffusion`, `CNN`, `GNN`, `RL`, or `Theory / Analysis`). These tags are intended for navigation and trend inspection rather than as a formal taxonomy.",
        "",
        "> **Freshness:** a conference year is added only after awards are announced. Conferences without a current-year award announcement intentionally stop at the latest completed edition.",
        "",
        "## Scope",
        "",
        "The catalog tracks conference paper awards such as **Best Paper**, **Outstanding Paper**, **Marr Prize**, honorable mentions / runners-up, student-paper awards, and venue-specific paper-award categories. Award candidates, nominations, demos, workshops, dissertation awards, lifetime awards, and retrospective test-of-time awards are excluded by default.",
        "",
        "The v2 catalog prioritizes official conference sources. The complete 2016–2018 content of the original repository has been normalized into the structured catalog; the [pre-revamp snapshot](https://github.com/shunk031/awesome-ai-best-papers/blob/1d33f4f2c39c53b6cec85816c6b3383334b8e913/README.md) remains available for provenance and comparison.",
        "",
        "## Research landscape",
        "",
        f"The tables below summarize the **{len(recent)} award records from {recent_start}–{max_year} currently in this catalog**. They describe this curated award set, not publication volume or the field as a whole.",
        "",
    ]

    area_counts = Counter(row["area"] for row in recent)
    task_counts = Counter(row["task"] for row in recent)
    render_count_table(lines, "Research areas", area_counts)
    render_count_table(lines, "Model / method families", family_counts(recent))
    render_count_table(lines, "Frequently awarded tasks", task_counts, limit=12)

    recent_families = family_counts(recent)
    lines.extend([
        "### Reading the recent slice",
        "",
        f'- **Language-model work is the clearest cluster:** `NLP & Language` accounts for {area_counts["NLP & Language"]} recent award records, while `LLM` and `Transformer` appear in {recent_families["LLM"]} and {recent_families["Transformer"]} records respectively.',
        f'- **Evaluation, safety, and theory are prominent:** `LLM Analysis & Evaluation` has {task_counts["LLM Analysis & Evaluation"]} records, `Safety, Fairness & Privacy` has {task_counts["Safety, Fairness & Privacy"]}, and `Optimization & Generalization` has {task_counts["Optimization & Generalization"]}.',
        f'- **Generative and multimodal work remains broad rather than single-model:** `Diffusion` appears in {recent_families["Diffusion"]} records, alongside `VLM` in {recent_families["VLM"]}, with recurring awards in image/video generation, 3D reconstruction, and multimodal vision-language tasks.',
        f'- **RL and structured reasoning remain active:** `Reinforcement Learning & Planning` has {task_counts["Reinforcement Learning & Planning"]} recent records, while graph / structured and neuro-symbolic work continues to appear across AAAI and ICLR.',
        "",
        "These are descriptive signals from the curated award set; they should not be interpreted as publication-volume or citation trends.",
        "",
        "## Coverage",
        "",
        "| Venue | Area | Years in catalog | Records | Official awards |",
        "| --- | --- | ---: | ---: | --- |",
    ])

    for venue in venues:
        items = by_venue.get(venue["venue"], [])
        item_years = sorted({int(row["year"]) for row in items})
        year_label = compact_years(item_years)
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
                f'{source_suffix}{tier_suffix}{notes_suffix}<br>'
                f'  **Area:** {row["area"]} · **Task:** {row["task"]} · **Model:** {row["model_family"].replace(";", " /")}'
            )
        lines.append("")

    lines.extend([
        "## Data and contributions",
        "",
        "To add or correct an award, edit the CSV data rather than this README. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for source requirements, tier definitions, and taxonomy rules.",
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
