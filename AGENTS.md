# Repository maintenance guide

This repository is a generated research catalog.

## Source of truth

- `data/papers/*.csv` contains venue-scoped award records, source provenance, and maintainer-curated research tags.
- `data/venues.csv` contains venue metadata.
- `templates/README.md.j2` owns README structure and prose.
- `scripts/generate_readme.py` owns data loading, grouping, and rendering context.
- `scripts/validate_catalog.py` owns structural validation.
- `README.md` is generated. Do not edit catalog entries in it directly.

## Research rules

- Verify award claims against official conference / society sources whenever possible.
- Use third-party awesome lists only for discovery or cross-checking.
- Do not treat award candidates, oral selections, acceptance status, or citation counts as paper awards.
- Preserve exact award labels and paper titles.
- Use `primary`, `secondary`, and `special` consistently with `CONTRIBUTING.md`.
- Treat `area`, `task`, and `model_family` as maintainer-curated navigation metadata, not award-committee claims.
- If the same paper has multiple award rows, keep its taxonomy fields identical across those rows.
- Do not add awards for a conference year before they have been officially announced.

## Required checks

Before proposing a change:

```bash
uv sync
uv run python scripts/validate_catalog.py
uv run python scripts/generate_readme.py
uv run python scripts/generate_readme.py --check
npx awesome-lint
```

A data change that leaves the generated README stale is incomplete.
