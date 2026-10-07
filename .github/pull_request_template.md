## Summary

<!-- What award data, venue metadata, taxonomy, or catalog behavior changes? -->

## Sources

<!-- Link official conference / society sources supporting the award-data change. -->

## Checklist

- [ ] I edited the relevant `data/papers/<venue>.csv`, not generated catalog entries in `README.md`.
- [ ] Award labels and paper titles match the cited source.
- [ ] I used an official source when one is available.
- [ ] New paper rows include `area`, `task`, and `model_family` metadata.
- [ ] Area, task, and model-family tags use the controlled vocabulary in `data/README.md`.
- [ ] Repeated award rows for the same paper use identical taxonomy values.
- [ ] I ran `python scripts/validate_catalog.py`.
- [ ] I regenerated `README.md`.
- [ ] I ran `python scripts/generate_readme.py --check`.
