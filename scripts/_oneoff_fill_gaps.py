#!/usr/bin/env python3
from __future__ import annotations
import csv, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PAPERS = DATA / "papers.csv"
TAXONOMY = DATA / "paper_taxonomy.csv"
ADDITIONS = DATA / "_oneoff_gap_additions.csv"
VALIDATOR = ROOT / "scripts" / "validate_catalog.py"
GENERATOR = ROOT / "scripts" / "generate_readme.py"
DATA_README = DATA / "README.md"
CHECKED_AT = "2026-10-07"
PAPER_FIELDS = ["venue","year","award","tier","title","paper_url","source_url","checked_at","notes"]
TAXONOMY_FIELDS = ["venue","year","title","area","task","model_family"]
TIER_ORDER = {"primary":0,"secondary":1,"special":2}
VENUE_ORDER = {v:i for i,v in enumerate(["ACL","AAAI","CVPR","EMNLP","ICCV","ICLR","ICML","NAACL","NeurIPS"])}

def read(path):
    with path.open(newline="", encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
    for index,row in enumerate(rows, start=2):
        if None in row:
            raise ValueError(f"Malformed CSV row in {path} at line {index}: {row}")
    return rows

def write(path, fields, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def patch_support():
    validator=VALIDATOR.read_text(encoding="utf-8")
    needle='"LLM Analysis & Evaluation", "Language Modeling & Generation",'
    if '"Evaluation & Benchmarking"' not in validator:
        if needle not in validator:
            raise RuntimeError("validator TASKS anchor not found")
        validator=validator.replace(
            needle,
            '"LLM Analysis & Evaluation", "Evaluation & Benchmarking", "Language Modeling & Generation",',
            1,
        )
        VALIDATOR.write_text(validator, encoding="utf-8")

    text=DATA_README.read_text(encoding="utf-8")
    needle="- `LLM Analysis & Evaluation`, `Language Modeling & Generation`, `Language Understanding & Linguistics`"
    if "`Evaluation & Benchmarking`" not in text:
        if needle not in text:
            raise RuntimeError("data README anchor not found")
        text=text.replace(
            needle,
            "- `LLM Analysis & Evaluation`, `Evaluation & Benchmarking`, `Language Modeling & Generation`, `Language Understanding & Linguistics`",
            1,
        )
        DATA_README.write_text(text, encoding="utf-8")

    gen=GENERATOR.read_text(encoding="utf-8")
    if "def compact_years(" not in gen:
        anchor="\ndef render() -> str:\n"
        if anchor not in gen:
            raise RuntimeError("generator render anchor not found")
        helper=(
            "\ndef compact_years(years: list[int]) -> str:\n"
            "    if not years:\n"
            "        return \"—\"\n"
            "    unique=sorted(set(years))\n"
            "    groups=[]\n"
            "    start=prev=unique[0]\n"
            "    for year in unique[1:]:\n"
            "        if year == prev + 1:\n"
            "            prev=year\n"
            "            continue\n"
            "        groups.append((start,prev))\n"
            "        start=prev=year\n"
            "    groups.append((start,prev))\n"
            "    return \", \".join(str(a) if a == b else f\"{a}–{b}\" for a,b in groups)\n"
        )
        gen=gen.replace(anchor,"\n"+helper+anchor,1)
    old=(
        '        item_years = sorted({int(row["year"]) for row in items})\n'
        '        year_label = "—"\n'
        '        if item_years:\n'
        '            year_label = str(item_years[0]) if len(item_years) == 1 else f"{item_years[0]}–{item_years[-1]}"\n'
    )
    new=(
        '        item_years = sorted({int(row["year"]) for row in items})\n'
        '        year_label = compact_years(item_years)\n'
    )
    if old in gen:
        gen=gen.replace(old,new,1)
    elif "year_label = compact_years(item_years)" not in gen:
        raise RuntimeError("generator year-label anchor not found")
    GENERATOR.write_text(gen, encoding="utf-8")

def main():
    patch_support()
    papers=read(PAPERS)
    taxonomy=read(TAXONOMY)
    additions=read(ADDITIONS)

    for row in papers:
        if row["venue"]=="ICLR" and int(row["year"]) in {2016,2017,2018}:
            row["award"]="Best Paper"

    papers_by_key={(r["venue"],int(r["year"]),r["title"].casefold()):r for r in papers}
    taxonomy_by_key={(r["venue"],int(r["year"]),r["title"].casefold()):r for r in taxonomy}
    for r in additions:
        key=(r["venue"],int(r["year"]),r["title"].casefold())
        papers_by_key[key]={
            "venue":r["venue"],
            "year":r["year"],
            "award":r["award"],
            "tier":r["tier"],
            "title":r["title"],
            "paper_url":r["paper_url"],
            "source_url":r["source_url"],
            "checked_at":CHECKED_AT,
            "notes":"",
        }
        taxonomy_by_key[key]={
            "venue":r["venue"],
            "year":r["year"],
            "title":r["title"],
            "area":r["area"],
            "task":r["task"],
            "model_family":r["model_family"],
        }

    papers=sorted(
        papers_by_key.values(),
        key=lambda r:(VENUE_ORDER.get(r["venue"],999),-int(r["year"]),TIER_ORDER.get(r["tier"],99),r["award"].casefold(),r["title"].casefold()),
    )
    taxonomy=sorted(
        taxonomy_by_key.values(),
        key=lambda r:(VENUE_ORDER.get(r["venue"],999),-int(r["year"]),r["title"].casefold()),
    )
    write(PAPERS,PAPER_FIELDS,papers)
    write(TAXONOMY,TAXONOMY_FIELDS,taxonomy)

    subprocess.run([sys.executable,str(VALIDATOR)],cwd=ROOT,check=True)
    subprocess.run([sys.executable,str(GENERATOR)],cwd=ROOT,check=True)
    subprocess.run([sys.executable,str(GENERATOR),"--check"],cwd=ROOT,check=True)
    print(f"Catalog now has {len(papers)} award records and {len(taxonomy)} taxonomy records.")

if __name__=="__main__":
    main()
