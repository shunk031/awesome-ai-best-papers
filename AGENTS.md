# Repository maintenance guide

This repository is a generated research catalog.

## Source of truth

- `data/papers.csv` contains award records.
- `data/venues.csv` contains venue metadata.
- `README.md` is generated. Do not edit catalog entries in it directly.
- `scripts/generate_readme.py` owns ordering and rendering.
- `scripts/validate_catalog.py` owns structural validation.

## Research rules

- Verify award claims against official conference / society sources whenever possible.
- Use third-party awesome lists only for discovery or cross-checking.
- Do not treat award candidates, oral selections, acceptance status, or citation counts as paper awards.
- Preserve exact award labels and paper titles.
- Use `primary`, `secondary`, and `special` consistently with `CONTRIBUTING.md`.
- Do not add awards for a conference year before they have been officially announced.

## Required checks

Before proposing a change:

```bash
python scripts/validate_catalog.py
python scripts/generate_readme.py
python scripts/generate_readme.py --check
```

A data change that leaves the generated README stale is incomplete.
