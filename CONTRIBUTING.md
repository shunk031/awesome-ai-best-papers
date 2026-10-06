# Contributing

Thanks for helping keep **Awesome AI Best Papers** current.

## What belongs here

The core catalog tracks paper awards from the conferences listed in `data/venues.csv`.

Use the award label published by the conference. The normalized `tier` is:

- `primary`: the venue's top paper award, e.g. Best Paper, Outstanding Paper, or Marr Prize.
- `secondary`: honorable mentions, runners-up, best student paper, and comparable paper-level awards.
- `special`: venue-specific paper awards such as theme, resource, social-impact, or track-specific awards.

By default, do not add award candidates / nominees, demos, workshop-only awards, dissertations, lifetime awards, or retrospective test-of-time awards.

## Source requirements

1. Prefer an official conference, society, proceedings, or conference-blog award page for `source_url`.
2. Prefer the proceedings, ACL Anthology, OpenReview, CVF Open Access, DOI, or arXiv for `paper_url`.
3. Do not infer an award from social media or a third-party list when an official source exists.
4. Preserve the official spelling of the paper title and award label.
5. Set `checked_at` to the date on which you verified the source.

Third-party catalogs such as Jeff Huang's Best Paper Awards are useful for discovery and cross-checking, but should not replace an available official source.

## Research-area, task, and model-family tags

Every paper also has a matching row in `data/paper_taxonomy.csv` with three navigation fields:

- `area`: exactly one broad primary research area from the controlled vocabulary in [`data/README.md`](data/README.md).
- `task`: exactly one controlled task category from [`data/README.md`](data/README.md).
- `model_family`: one or more coarse model / method families separated by `; `, e.g. `LLM; Transformer` or `Diffusion; VLM`.

Keep these tags intentionally coarse. They are meant to answer questions such as **which tasks are repeatedly receiving awards** and **which model families are prominent**, not to replace a full paper taxonomy. For theoretical work without a single architecture, `Theory / Analysis`, `Optimization`, or `Probabilistic / Bayesian` is preferable to inventing a model label.

## Workflow

Edit the data, regenerate the README, and run validation:

```bash
python scripts/validate_catalog.py
python scripts/generate_readme.py
python scripts/generate_readme.py --check
```

Commit both the CSV change and the regenerated `README.md`.

## Adding a new venue

Add it to `data/venues.csv` first. Keep the venue identifier short and stable; changing it later rewrites every matching paper row.

## Corrections

Corrections are welcome even when they reduce the catalog. In the pull request, include the official source that supports the correction.
