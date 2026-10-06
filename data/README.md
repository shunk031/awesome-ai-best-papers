# Catalog data

This directory is the source of truth for the generated catalog.

## `venues.csv`

One row per tracked conference.

- `venue`: stable short identifier used by `papers.csv`
- `full_name`: display name
- `area`: broad research area
- `official_url`: conference or organization homepage
- `award_url`: canonical official award archive or policy page
- `cadence`: annual / biennial / periodic
- `notes`: short venue-specific note

## `papers.csv`

One row per award-winning paper.

- `venue`: must match `venues.csv`
- `year`: conference year
- `award`: award label as announced by the venue
- `tier`: `primary`, `secondary`, or `special`
- `title`: paper title
- `paper_url`: preferred canonical paper/proceedings URL; may be blank when not yet resolved
- `source_url`: official page supporting the award claim
- `checked_at`: date the source was last checked (`YYYY-MM-DD`)
- `notes`: optional clarification

The README is generated from these files. Do not edit generated entries in `README.md` directly.
