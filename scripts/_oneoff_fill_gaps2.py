#!/usr/bin/env python3
from __future__ import annotations
import csv, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PAPERS = DATA / "papers.csv"
TAXONOMY = DATA / "paper_taxonomy.csv"
ADDITIONS = DATA / "_oneoff_gap_additions2.csv"
VALIDATOR = ROOT / "scripts" / "validate_catalog.py"
GENERATOR = ROOT / "scripts" / "generate_readme.py"
CHECKED_AT = "2026-10-07"
PAPER_FIELDS = ["venue","year","award","tier","title","paper_url","source_url","checked_at","notes"]
TAXONOMY_FIELDS = ["venue","year","title","area","task","model_family"]
TIER_ORDER = {"primary":0,"secondary":1,"special":2}
VENUE_ORDER = {v:i for i,v in enumerate(["ACL","AAAI","CVPR","EMNLP","ICCV","ICLR","ICML","NAACL","NeurIPS"])}

def read(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def write(path, fields, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

def main():
    papers=read(PAPERS)
    taxonomy=read(TAXONOMY)
    additions=read(ADDITIONS)

    award_rows={
        (r["venue"],int(r["year"]),r["award"].casefold(),r["title"].casefold()):r
        for r in papers
    }
    taxonomy_rows={
        (r["venue"],int(r["year"]),r["title"].casefold()):r
        for r in taxonomy
    }

    for r in additions:
        award_key=(r["venue"],int(r["year"]),r["award"].casefold(),r["title"].casefold())
        paper_key=(r["venue"],int(r["year"]),r["title"].casefold())
        award_rows[award_key]={
            "venue":r["venue"], "year":r["year"], "award":r["award"], "tier":r["tier"],
            "title":r["title"], "paper_url":r["paper_url"], "source_url":r["source_url"],
            "checked_at":CHECKED_AT, "notes":"",
        }
        candidate={
            "venue":r["venue"], "year":r["year"], "title":r["title"], "area":r["area"],
            "task":r["task"], "model_family":r["model_family"],
        }
        existing=taxonomy_rows.get(paper_key)
        if existing and any(existing[k] != candidate[k] for k in TAXONOMY_FIELDS):
            raise ValueError(f"Conflicting taxonomy for {paper_key}: {existing} vs {candidate}")
        taxonomy_rows[paper_key]=candidate

    papers=sorted(
        award_rows.values(),
        key=lambda r:(VENUE_ORDER.get(r["venue"],999),-int(r["year"]),TIER_ORDER.get(r["tier"],99),r["award"].casefold(),r["title"].casefold()),
    )
    taxonomy=sorted(
        taxonomy_rows.values(),
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
