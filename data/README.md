# Catalog data

This directory is the source of truth for the generated catalog.

## `venues.csv`

One row per tracked conference.

- `venue`: stable short identifier used by the paper CSV files
- `full_name`: display name
- `area`: broad venue-level research area
- `official_url`: conference or organization homepage
- `award_url`: canonical official award archive or policy page
- `cadence`: annual / biennial / periodic
- `notes`: short venue-specific note

## `papers/`

One CSV file per tracked venue, named from the lowercase venue identifier, for example `papers/acl.csv`, `papers/icml.csv`, and `papers/neurips.csv`.

Each row is one award record and stores both the source-backed award facts and the maintainer-curated navigation metadata for that paper:

- `venue`: must match `venues.csv` and the venue implied by the filename
- `year`: conference year
- `award`: award label as announced by the venue
- `tier`: `primary`, `secondary`, or `special`
- `title`: paper title
- `paper_url`: preferred canonical paper/proceedings URL; may be blank when not yet resolved
- `source_url`: official page supporting the award claim
- `checked_at`: date the source was last checked (`YYYY-MM-DD`)
- `area`: exactly one broad primary research area
- `task`: exactly one controlled task category
- `model_family`: one or more coarse model / method families separated by `; `
- `notes`: optional clarification

A paper can have more than one award row. In that case, its `area`, `task`, and `model_family` values are repeated and must be identical across those rows. The validator enforces this consistency.

### Scope convention

The catalog covers research-paper awards from the tracked venues. Separately reviewed position-paper tracks, award candidates / nominees, demos, workshop-only awards, dissertations, lifetime awards, and retrospective test-of-time awards are out of scope by default. Research-track-specific awards such as theme, resource, or social-impact paper awards remain in scope and use the `special` tier where appropriate.

### Research areas

- `NLP & Language`
- `Computer Vision`
- `Multimodal & Embodied AI`
- `Speech & Audio`
- `Reinforcement Learning & Decision Making`
- `ML Theory & Optimization`
- `Graphs & Structured Learning`
- `Responsible AI & Privacy`
- `Scientific ML & Applications`
- `General ML & Representation Learning`

### Task categories

- `LLM Analysis & Evaluation`, `Evaluation & Benchmarking`, `Language Modeling & Generation`, `Language Understanding & Linguistics`
- `Reasoning & Knowledge`, `Retrieval & Search`, `Multimodal & Vision-Language`, `Speech & Audio`
- `Visual Recognition & Representation`, `3D Vision & Reconstruction`, `Image & Video Generation`
- `Generative Modeling`, `Reinforcement Learning & Planning`, `Graph & Structured Learning`
- `Meta-Learning & Adaptation`, `Representation Learning`, `Model Efficiency & Architecture`
- `Optimization & Generalization`, `Probabilistic Inference & Sampling`, `Safety, Fairness & Privacy`
- `Scientific Discovery & Simulation`, `Causal Learning`, `Robustness & Domain Adaptation`
- `Interpretability & Explainability`, `Model Editing & Adaptation`

### Model / method families

The controlled family vocabulary includes `LLM`, `VLM`, `Transformer`, `Diffusion`, `Autoregressive`, `CNN`, `RNN`, `GNN`, `VAE`, `GAN`, `RL`, `Meta-Learning`, `Probabilistic / Bayesian`, `Optimization`, `Neuro-Symbolic`, `Representation Learning`, and `Theory / Analysis`, plus a few generic fallbacks for methods that do not fit a single neural architecture.

These annotations are **curatorial metadata**, not claims made by the award committee. Keeping them in the same physical row as the award record is an operational choice: award provenance remains source-backed, while `area`, `task`, and `model_family` remain maintainer-curated navigation metadata.

The README is generated from these files. Do not edit generated entries in `README.md` directly.
