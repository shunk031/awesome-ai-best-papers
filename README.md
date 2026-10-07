# Awesome AI Best Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Catalog Check](https://github.com/shunk031/awesome-ai-best-papers/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/shunk031/awesome-ai-best-papers/actions/workflows/catalog-check.yml)

![Award records](https://img.shields.io/badge/award%20records-470-informational)
![Venues](https://img.shields.io/badge/venues-9-informational)
![Coverage](https://img.shields.io/badge/coverage-2016%E2%80%932026-informational)

<!-- This file is generated from data/*.csv by scripts/generate_readme.py. Do not edit it directly. -->

A curated, source-backed catalog of paper awards from major AI, machine learning, computer vision, and natural language processing conferences.

The repository is **data-driven**: [`data/papers.csv`](data/papers.csv) is the canonical award catalog, [`data/paper_taxonomy.csv`](data/paper_taxonomy.csv) stores research annotations, [`data/venues.csv`](data/venues.csv) defines venue metadata, and this README is regenerated deterministically.

Each paper is annotated with a maintainer-curated **research area**, **task**, and coarse **model / method family** (for example `LLM`, `VLM`, `Transformer`, `Diffusion`, `CNN`, `GNN`, `RL`, or `Theory / Analysis`). These tags are intended for navigation and trend inspection rather than as a formal taxonomy.

> **Freshness:** a conference year is added only after awards are announced. Conferences without a current-year award announcement intentionally stop at the latest completed edition.

## Scope

The catalog tracks conference paper awards such as **Best Paper**, **Outstanding Paper**, **Marr Prize**, honorable mentions / runners-up, student-paper awards, and venue-specific paper-award categories. Award candidates, nominations, demos, workshops, dissertation awards, lifetime awards, and retrospective test-of-time awards are excluded by default.

The v2 catalog prioritizes official conference sources. The complete 2016–2018 content of the original repository has been normalized into the structured catalog; the [pre-revamp snapshot](https://github.com/shunk031/awesome-ai-best-papers/blob/1d33f4f2c39c53b6cec85816c6b3383334b8e913/README.md) remains available for provenance and comparison.

## Research landscape

The tables below summarize the **97 award records from 2024–2026 currently in this catalog**. They describe this curated award set, not publication volume or the field as a whole.

### Research areas

| Label | Award records |
| --- | ---: |
| NLP & Language | 33 |
| ML Theory & Optimization | 15 |
| Responsible AI & Privacy | 12 |
| Computer Vision | 10 |
| General ML & Representation Learning | 8 |
| Multimodal & Embodied AI | 6 |
| Reinforcement Learning & Decision Making | 5 |
| Graphs & Structured Learning | 4 |
| Scientific ML & Applications | 3 |
| Speech & Audio | 1 |

### Model / method families

| Label | Award records |
| --- | ---: |
| Transformer | 47 |
| LLM | 38 |
| Theory / Analysis | 22 |
| Diffusion | 11 |
| Optimization | 8 |
| Probabilistic / Bayesian | 7 |
| Representation Learning | 7 |
| Autoregressive | 6 |
| Neural Model | 5 |
| VLM | 5 |
| RL | 5 |
| Neuro-Symbolic | 3 |
| GNN | 2 |
| VAE | 1 |
| Classical / Optimization | 1 |
| Meta-Learning | 1 |

### Frequently awarded tasks

| Label | Award records |
| --- | ---: |
| LLM Analysis & Evaluation | 11 |
| Safety, Fairness & Privacy | 11 |
| Optimization & Generalization | 9 |
| Model Efficiency & Architecture | 7 |
| Language Modeling & Generation | 6 |
| Image & Video Generation | 5 |
| Probabilistic Inference & Sampling | 5 |
| Generative Modeling | 5 |
| Multimodal & Vision-Language | 4 |
| Reinforcement Learning & Planning | 4 |
| Language Understanding & Linguistics | 3 |
| Graph & Structured Learning | 3 |

### Reading the recent slice

- **Language-model work is the clearest cluster:** `NLP & Language` accounts for 33 recent award records, while `LLM` and `Transformer` appear in 38 and 47 records respectively.
- **Evaluation, safety, and theory are prominent:** `LLM Analysis & Evaluation` has 11 records, `Safety, Fairness & Privacy` has 11, and `Optimization & Generalization` has 9.
- **Generative and multimodal work remains broad rather than single-model:** `Diffusion` appears in 11 records, alongside `VLM` in 5, with recurring awards in image/video generation, 3D reconstruction, and multimodal vision-language tasks.
- **RL and structured reasoning remain active:** `Reinforcement Learning & Planning` has 4 recent records, while graph / structured and neuro-symbolic work continues to appear across AAAI and ICLR.

These are descriptive signals from the curated award set; they should not be interpreted as publication-volume or citation trends.

## Coverage

| Venue | Area | Years in catalog | Records | Official awards |
| --- | --- | ---: | ---: | --- |
| [ACL](https://aclweb.org/) | Natural Language Processing | 2016–2026 | 137 | [source](https://www.aclweb.org/aclwiki/Best_paper_awards) |
| [AAAI](https://aaai.org/conference/aaai/) | Artificial Intelligence | 2016–2026 | 25 | [source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/) |
| [CVPR](https://cvpr.thecvf.com/) | Computer Vision | 2016–2026 | 19 | [source](https://www.thecvf.com/?page_id=413) |
| [EMNLP](https://aclanthology.org/venues/emnlp/) | Natural Language Processing | 2016–2025 | 65 | [source](https://www.aclweb.org/aclwiki/Best_paper_awards) |
| [ICCV](https://iccv.thecvf.com/) | Computer Vision | 2017, 2019, 2021, 2023, 2025 | 10 | [source](https://www.thecvf.com/?page_id=413) |
| [ICLR](https://iclr.cc/) | Machine Learning | 2016–2026 | 72 | [source](https://blog.iclr.cc/) |
| [ICML](https://icml.cc/) | Machine Learning | 2016–2026 | 62 | [source](https://blog.icml.cc/) |
| [NAACL](https://naacl.org/) | Natural Language Processing | 2018–2019, 2021–2022, 2024–2025 | 35 | [source](https://naacl.org/policies/best-paper.html) |
| [NeurIPS](https://neurips.cc/) | Machine Learning | 2016–2025 | 45 | [source](https://blog.neurips.cc/) |

> **Coverage note:** year ranges list the conference years currently represented in the catalog. Gaps are explicit; a displayed span should not be interpreted as complete coverage of every intervening year.

## Latest awards

This section shows the latest completed award year for each venue. The full historical catalog is in [`data/papers.csv`](data/papers.csv).

### ACL · 2026

**Annual Meeting of the Association for Computational Linguistics** · [Natural Language Processing](https://aclweb.org/)

- **Best Paper** — [Characterizing the Expressivity of Local Attention in Transformers](https://2026.aclweb.org/program/best_papers/)<br>  **Area:** ML Theory & Optimization · **Task:** Model Efficiency & Architecture · **Model:** Transformer / Theory / Analysis
- **Best Paper** — [Memory Efficiency and Resource-Rational Encoding in Sentence Processing](https://2026.aclweb.org/program/best_papers/)<br>  **Area:** NLP & Language · **Task:** Language Understanding & Linguistics · **Model:** Theory / Analysis
- **Best Paper** — [The Imperfective Paradox in Large Language Models](https://2026.aclweb.org/program/best_papers/)<br>  **Area:** NLP & Language · **Task:** LLM Analysis & Evaluation · **Model:** LLM / Transformer

### AAAI · 2026

**AAAI Conference on Artificial Intelligence** · [Artificial Intelligence](https://aaai.org/conference/aaai/)

- **Outstanding Paper Award** — [Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/)<br>  **Area:** Scientific ML & Applications · **Task:** Causal Learning · **Model:** Theory / Analysis
- **Outstanding Paper Award** — [High-Pass Matters: Theoretical Insights and Sheaflet-Based Design for Hypergraph Neural Networks](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/)<br>  **Area:** Graphs & Structured Learning · **Task:** Graph & Structured Learning · **Model:** GNN
- **Outstanding Paper Award** — [LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/)<br>  **Area:** Multimodal & Embodied AI · **Task:** Multimodal & Vision-Language · **Model:** LLM / Transformer / VLM
- **Outstanding Paper Award** — [Model Change for Description Logic Concepts](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/)<br>  **Area:** Graphs & Structured Learning · **Task:** Graph & Structured Learning · **Model:** Neuro-Symbolic
- **Outstanding Paper Award** — [ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/)<br>  **Area:** Multimodal & Embodied AI · **Task:** Multimodal & Vision-Language · **Model:** VLM / Transformer

### CVPR · 2026

**IEEE/CVF Conference on Computer Vision and Pattern Recognition** · [Computer Vision](https://cvpr.thecvf.com/)

- **Best Paper** — [Efficiently Reconstructing Dynamic Scenes One D4RT at a Time](https://www.thecvf.com/?page_id=413)<br>  **Area:** Computer Vision · **Task:** 3D Vision & Reconstruction · **Model:** Transformer

### EMNLP · 2025

**Conference on Empirical Methods in Natural Language Processing** · [Natural Language Processing](https://aclanthology.org/venues/emnlp/)

- **Best Paper** — [Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index](https://2025.emnlp.org/program/awards/)<br>  **Area:** NLP & Language · **Task:** Retrieval & Search · **Model:** Classical / Optimization

### ICCV · 2025

**IEEE/CVF International Conference on Computer Vision** · [Computer Vision](https://iccv.thecvf.com/)

- **Marr Prize** — [Generating Physically Stable and Buildable Brick Structures from Text](https://www.thecvf.com/?page_id=413)<br>  **Area:** Computer Vision · **Task:** 3D Vision & Reconstruction · **Model:** Optimization

### ICLR · 2026

**International Conference on Learning Representations** · [Machine Learning](https://iclr.cc/)

- **Outstanding Paper** — [LLMs Get Lost In Multi-Turn Conversation](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)<br>  **Area:** NLP & Language · **Task:** LLM Analysis & Evaluation · **Model:** LLM / Transformer
- **Outstanding Paper** — [Transformers are Inherently Succinct](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)<br>  **Area:** ML Theory & Optimization · **Task:** Optimization & Generalization · **Model:** Transformer / Theory / Analysis
- **Outstanding Paper Honorable Mention** — [The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm](https://openreview.net/forum?id=yRtgZ1K8hO) · [award source](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/) · `secondary`<br>  **Area:** ML Theory & Optimization · **Task:** Optimization & Generalization · **Model:** Optimization / Theory / Analysis

### ICML · 2026

**International Conference on Machine Learning** · [Machine Learning](https://icml.cc/)

- **Outstanding Paper** — [High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/)<br>  **Area:** ML Theory & Optimization · **Task:** Probabilistic Inference & Sampling · **Model:** Diffusion / Probabilistic / Bayesian
- **Outstanding Paper** — [The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/)<br>  **Area:** ML Theory & Optimization · **Task:** LLM Analysis & Evaluation · **Model:** LLM / Transformer / Diffusion

### NAACL · 2025

**Annual Conference of the Nations of the Americas Chapter of the ACL** · [Natural Language Processing](https://naacl.org/)

- **Best Paper** — [The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models](https://2025.naacl.org/blog/best-papers/)<br>  **Area:** NLP & Language · **Task:** Language Modeling & Generation · **Model:** LLM / Transformer

### NeurIPS · 2025

**Conference on Neural Information Processing Systems** · [Machine Learning](https://neurips.cc/)

- **Best Paper** — [1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)<br>  **Area:** Reinforcement Learning & Decision Making · **Task:** Reinforcement Learning & Planning · **Model:** Representation Learning / RL
- **Best Paper** — [Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)<br>  **Area:** NLP & Language · **Task:** LLM Analysis & Evaluation · **Model:** LLM / Transformer
- **Best Paper** — [Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)<br>  **Area:** NLP & Language · **Task:** Model Efficiency & Architecture · **Model:** LLM / Transformer
- **Best Paper** — [Why Diffusion Models Don’t Memorize: The Role of Implicit Dynamical Regularization in Training](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)<br>  **Area:** ML Theory & Optimization · **Task:** Generative Modeling · **Model:** Diffusion / Theory / Analysis

## Data and contributions

To add or correct an award, edit the CSV data rather than this README. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for source requirements, tier definitions, and taxonomy rules.

```bash
python scripts/validate_catalog.py
python scripts/generate_readme.py
python scripts/generate_readme.py --check
```

## References

- [Best Paper Awards in Computer Science (Jeff Huang)](https://jeffhuang.com/best_paper_awards.html)
- [ACL-family best paper awards](https://www.aclweb.org/aclwiki/Best_paper_awards)
- [CVF best paper archive](https://www.thecvf.com/?page_id=413)

## License

The catalog continues the original repository's [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) dedication.
