# Awesome AI Best Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![Catalog Check](https://github.com/shunk031/awesome-ai-best-papers/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/shunk031/awesome-ai-best-papers/actions/workflows/catalog-check.yml)

![Award records](https://img.shields.io/badge/award%20records-569-informational)
![Venues](https://img.shields.io/badge/venues-9-informational)
![Coverage](https://img.shields.io/badge/coverage-2016%E2%80%932026-informational)

<!-- This file is generated from data/*.csv by scripts/generate_readme.py. Do not edit it directly. -->

A curated, source-backed catalog of paper awards from major AI, machine learning, computer vision, and natural language processing conferences.

The repository is **data-driven**: [`data/papers.csv`](data/papers.csv) is the canonical award catalog, [`data/paper_taxonomy.csv`](data/paper_taxonomy.csv) stores research annotations, [`data/venues.csv`](data/venues.csv) defines venue metadata, and this README is regenerated deterministically.

Each paper is annotated with a maintainer-curated **research area**, **task**, and coarse **model / method family** (for example `LLM`, `VLM`, `Transformer`, `Diffusion`, `CNN`, `GNN`, `RL`, or `Theory / Analysis`). These tags are intended for navigation and trend inspection rather than as a formal taxonomy.

> **Freshness:** a conference year is added only after awards are announced. Conferences without a current-year award announcement intentionally stop at the latest completed edition.

## Scope

The catalog tracks research-paper awards such as **Best Paper**, **Outstanding Paper**, **Marr Prize**, honorable mentions / runners-up, student-paper awards, and venue-specific research-paper categories. Award candidates, nominations, demos, workshops, dissertations, lifetime awards, retrospective test-of-time awards, and separately reviewed **position-paper tracks** are excluded by default.

The v2 catalog prioritizes official conference sources. The complete 2016–2018 content of the original repository has been normalized into the structured catalog; the [pre-revamp snapshot](https://github.com/shunk031/awesome-ai-best-papers/blob/1d33f4f2c39c53b6cec85816c6b3383334b8e913/README.md) remains available for provenance and comparison.

## Research landscape

The tables below summarize the **132 award records from 2024–2026 currently in this catalog**. They describe this curated award set, not publication volume or the field as a whole.

### Research areas

| Label | Award records |
| --- | ---: |
| NLP & Language | 34 |
| Computer Vision | 30 |
| ML Theory & Optimization | 17 |
| Responsible AI & Privacy | 15 |
| Multimodal & Embodied AI | 10 |
| Scientific ML & Applications | 8 |
| General ML & Representation Learning | 8 |
| Reinforcement Learning & Decision Making | 5 |
| Graphs & Structured Learning | 4 |
| Speech & Audio | 1 |

### Model / method families

| Label | Award records |
| --- | ---: |
| Transformer | 57 |
| LLM | 41 |
| Theory / Analysis | 28 |
| Neural Model | 20 |
| Diffusion | 14 |
| Optimization | 12 |
| Probabilistic / Bayesian | 9 |
| VLM | 9 |
| RL | 8 |
| Representation Learning | 7 |
| Autoregressive | 6 |
| Neuro-Symbolic | 3 |
| GNN | 3 |
| CNN | 2 |
| Classical / Optimization | 2 |
| VAE | 1 |
| Meta-Learning | 1 |

### Frequently awarded tasks

| Label | Award records |
| --- | ---: |
| Safety, Fairness & Privacy | 14 |
| 3D Vision & Reconstruction | 14 |
| LLM Analysis & Evaluation | 13 |
| Optimization & Generalization | 11 |
| Image & Video Generation | 8 |
| Model Efficiency & Architecture | 7 |
| Generative Modeling | 7 |
| Multimodal & Vision-Language | 6 |
| Reinforcement Learning & Planning | 6 |
| Probabilistic Inference & Sampling | 6 |
| Language Modeling & Generation | 5 |
| Visual Recognition & Representation | 5 |

### Reading the recent slice

- **Language-model work is the clearest cluster:** `NLP & Language` accounts for 34 recent award records, while `LLM` and `Transformer` appear in 41 and 57 records respectively.
- **Evaluation, safety, and theory are prominent:** `LLM Analysis & Evaluation` has 13 records, `Safety, Fairness & Privacy` has 14, and `Optimization & Generalization` has 11.
- **Generative and multimodal work remains broad rather than single-model:** `Diffusion` appears in 14 records, alongside `VLM` in 9, with recurring awards in image/video generation, 3D reconstruction, and multimodal vision-language tasks.
- **RL and structured reasoning remain active:** `Reinforcement Learning & Planning` has 6 recent records, while graph / structured and neuro-symbolic work continues to appear across AAAI and ICLR.

These are descriptive signals from the curated award set; they should not be interpreted as publication-volume or citation trends.

## Coverage

| Venue | Area | Years in catalog | Records | Official awards |
| --- | --- | ---: | ---: | --- |
| [ACL](https://aclweb.org/) | Natural Language Processing | 2016–2026 | 137 | [source](https://www.aclweb.org/aclwiki/Best_paper_awards) |
| [AAAI](https://aaai.org/conference/aaai/) | Artificial Intelligence | 2016–2026 | 76 | [source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/) |
| [CVPR](https://cvpr.thecvf.com/) | Computer Vision | 2016–2026 | 59 | [source](https://www.thecvf.com/?page_id=413) |
| [EMNLP](https://aclanthology.org/venues/emnlp/) | Natural Language Processing | 2016–2025 | 65 | [source](https://www.aclweb.org/aclwiki/Best_paper_awards) |
| [ICCV](https://iccv.thecvf.com/) | Computer Vision | 2017, 2019, 2021, 2023, 2025 | 23 | [source](https://www.thecvf.com/?page_id=413) |
| [ICLR](https://iclr.cc/) | Machine Learning | 2016–2019, 2021–2026 | 62 | [source](https://blog.iclr.cc/) |
| [ICML](https://icml.cc/) | Machine Learning | 2016–2026 | 67 | [source](https://blog.icml.cc/) |
| [NAACL](https://naacl.org/) | Natural Language Processing | 2018–2019, 2021–2022, 2024–2025 | 35 | [source](https://naacl.org/policies/best-paper.html) |
| [NeurIPS](https://neurips.cc/) | Machine Learning | 2016–2025 | 45 | [source](https://blog.neurips.cc/) |

> **Coverage note:** year ranges list conference years with in-scope awards in the catalog. Gaps are explicit and can reflect a non-conference year or a confirmed no-award year; **ICLR 2020 is intentionally absent because no paper award was given that year.**

## Latest awards

This section shows the latest completed award year for each venue. The full historical catalog is in [`data/papers.csv`](data/papers.csv).

### ACL · 2026

**Annual Meeting of the Association for Computational Linguistics** · [Natural Language Processing](https://aclweb.org/)

- **Best Paper** — [Characterizing the Expressivity of Local Attention in Transformers](https://aclanthology.org/2026.acl-long.1739/) · [award source](https://2026.aclweb.org/program/best_papers/)<br>  **Area:** ML Theory & Optimization · **Task:** Model Efficiency & Architecture · **Model:** Transformer / Theory / Analysis
- **Best Paper** — [Memory Efficiency and Resource-Rational Encoding in Sentence Processing](https://aclanthology.org/2026.acl-long.1550/) · [award source](https://2026.aclweb.org/program/best_papers/)<br>  **Area:** NLP & Language · **Task:** Language Understanding & Linguistics · **Model:** Theory / Analysis
- **Best Paper** — [The Imperfective Paradox in Large Language Models](https://aclanthology.org/2026.acl-long.689/) · [award source](https://2026.aclweb.org/program/best_papers/)<br>  **Area:** NLP & Language · **Task:** LLM Analysis & Evaluation · **Model:** LLM / Transformer

### AAAI · 2026

**AAAI Conference on Artificial Intelligence** · [Artificial Intelligence](https://aaai.org/conference/aaai/)

- **Outstanding Paper Award** — [Causal Structure Learning for Dynamical Systems with Theoretical Score Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/40999) · [award source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/)<br>  **Area:** Scientific ML & Applications · **Task:** Causal Learning · **Model:** Theory / Analysis
- **Outstanding Paper Award** — [High-Pass Matters: Theoretical Insights and Sheaflet-Based Design for Hypergraph Neural Networks](https://ojs.aaai.org/index.php/AAAI/article/view/39469) · [award source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/)<br>  **Area:** Graphs & Structured Learning · **Task:** Graph & Structured Learning · **Model:** GNN
- **Outstanding Paper Award** — [LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation](https://ojs.aaai.org/index.php/AAAI/article/view/37427) · [award source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/)<br>  **Area:** Multimodal & Embodied AI · **Task:** Multimodal & Vision-Language · **Model:** LLM / Transformer / VLM
- **Outstanding Paper Award** — [Model Change for Description Logic Concepts](https://ojs.aaai.org/index.php/AAAI/article/view/39008) · [award source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/)<br>  **Area:** Graphs & Structured Learning · **Task:** Graph & Structured Learning · **Model:** Neuro-Symbolic
- **Outstanding Paper Award** — [ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver](https://ojs.aaai.org/index.php/AAAI/article/view/38921) · [award source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/)<br>  **Area:** Multimodal & Embodied AI · **Task:** Multimodal & Vision-Language · **Model:** VLM / Transformer
- **Best Paper Award – AI Alignment Track** — [On the Alignment of Large Language Models with Global Human Opinion](https://ojs.aaai.org/index.php/AAAI/article/view/41102) · [award source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/) · `special`<br>  **Area:** Responsible AI & Privacy · **Task:** Safety, Fairness & Privacy · **Model:** LLM / Transformer
- **Best Paper Award – AI for Social Impact Track** — [Fractured Glass, Failing Cameras: Simulating Physics-Based Adversarial Samples for Autonomous Driving Systems](https://ojs.aaai.org/index.php/AAAI/article/view/37792) · [award source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/) · `special`<br>  **Area:** Computer Vision · **Task:** Robustness & Domain Adaptation · **Model:** CNN / Transformer
- **Best Paper Award – AI for Social Impact Track** — [Generalizable Slum Detection from Satellite Imagery with Mixture-of-Experts](https://ojs.aaai.org/index.php/AAAI/article/view/41227) · [award source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/) · `special`<br>  **Area:** Scientific ML & Applications · **Task:** Scientific Discovery & Simulation · **Model:** Neural Model
- **Best Paper Award – AI for Social Impact Track** — [PlantTraitNet: An Uncertainty-Aware Multimodal Framework for Global-Scale Plant Trait Inference from Citizen Science Data](https://ojs.aaai.org/index.php/AAAI/article/view/41272) · [award source](https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/) · `special`<br>  **Area:** Scientific ML & Applications · **Task:** Scientific Discovery & Simulation · **Model:** VLM / Transformer

### CVPR · 2026

**IEEE/CVF Conference on Computer Vision and Pattern Recognition** · [Computer Vision](https://cvpr.thecvf.com/)

- **Best Paper** — [Efficiently Reconstructing Dynamic Scenes One D4RT at a Time](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Efficiently_Reconstructing_Dynamic_Scenes_One_D4RT_at_a_Time_CVPR_2026_paper.html) · [award source](https://www.thecvf.com/?page_id=413)<br>  **Area:** Computer Vision · **Task:** 3D Vision & Reconstruction · **Model:** Transformer
- **Best Paper Honorable Mention** — [NitroGen: An Open Foundation Model for Generalist Gaming Agents](https://openaccess.thecvf.com/content/CVPR2026/html/Magne_NitroGen_An_Open_Foundation_Model_for_Generalist_Gaming_Agents_CVPR_2026_paper.html) · [award source](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) · `secondary`<br>  **Area:** Multimodal & Embodied AI · **Task:** Reinforcement Learning & Planning · **Model:** Transformer / RL
- **Best Paper Honorable Mention** — [SAM 3D: 3Dfy Anything in Images](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_SAM_3D_3Dfy_Anything_in_Images_CVPR_2026_paper.html) · [award source](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) · `secondary`<br>  **Area:** Computer Vision · **Task:** 3D Vision & Reconstruction · **Model:** Transformer / Neural Model
- **Best Student Paper** — [Native and Compact Structured Latents for 3D Generation](https://openaccess.thecvf.com/content/CVPR2026/html/Xiang_Native_and_Compact_Structured_Latents_for_3D_Generation_CVPR_2026_paper.html) · [award source](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) · `secondary`<br>  **Area:** Computer Vision · **Task:** Generative Modeling · **Model:** Neural Model
- **Best Student Paper Honorable Mention** — [ChordEdit: One-Step Low-Energy Transport for Image Editing](https://openaccess.thecvf.com/content/CVPR2026/html/Lu_ChordEdit_One-Step_Low-Energy_Transport_for_Image_Editing_CVPR_2026_paper.html) · [award source](https://cvpr.thecvf.com/Conferences/2026/News/Best_Papers) · `secondary`<br>  **Area:** Computer Vision · **Task:** Image & Video Generation · **Model:** Optimization

### EMNLP · 2025

**Conference on Empirical Methods in Natural Language Processing** · [Natural Language Processing](https://aclanthology.org/venues/emnlp/)

- **Best Paper** — [Infini-gram mini: Exact n-gram Search at the Internet Scale with FM-Index](https://aclanthology.org/2025.emnlp-main.1268/) · [award source](https://2025.emnlp.org/program/awards/)<br>  **Area:** NLP & Language · **Task:** Retrieval & Search · **Model:** Classical / Optimization

### ICCV · 2025

**IEEE/CVF International Conference on Computer Vision** · [Computer Vision](https://iccv.thecvf.com/)

- **Marr Prize** — [Generating Physically Stable and Buildable Brick Structures from Text](https://openaccess.thecvf.com/content/ICCV2025/html/Pun_Generating_Physically_Stable_and_Buildable_Brick_Structures_from_Text_ICCV_2025_paper.html) · [award source](https://www.thecvf.com/?page_id=413)<br>  **Area:** Computer Vision · **Task:** 3D Vision & Reconstruction · **Model:** Optimization
- **Best Student Paper** — [FlowEdit: Inversion-Free Text-Based Editing Using Pre-Trained Flow Models](https://openaccess.thecvf.com/content/ICCV2025/html/Kulikov_FlowEdit_Inversion-Free_Text-Based_Editing_Using_Pre-Trained_Flow_Models_ICCV_2025_paper.html) · [award source](https://www.thecvf.com/?page_id=413) · `secondary`<br>  **Area:** Computer Vision · **Task:** Image & Video Generation · **Model:** Neural Model
- **Marr Prize Paper Honorable Mention** — [RayZer: A Self-supervised Large View Synthesis Model](https://openaccess.thecvf.com/content/ICCV2025/html/Jiang_RayZer_A_Self-supervised_Large_View_Synthesis_Model_ICCV_2025_paper.html) · [award source](https://www.thecvf.com/?page_id=413) · `secondary`<br>  **Area:** Computer Vision · **Task:** 3D Vision & Reconstruction · **Model:** Neural Model
- **Marr Prize Paper Honorable Mention** — [Spatially-Varying Autofocus](https://openaccess.thecvf.com/content/ICCV2025/html/Qin_Spatially-Varying_Autofocus_ICCV_2025_paper.html) · [award source](https://www.thecvf.com/?page_id=413) · `secondary`<br>  **Area:** Computer Vision · **Task:** 3D Vision & Reconstruction · **Model:** Classical / Optimization

### ICLR · 2026

**International Conference on Learning Representations** · [Machine Learning](https://iclr.cc/)

- **Outstanding Paper** — [LLMs Get Lost In Multi-Turn Conversation](https://openreview.net/forum?id=VKGTGGcwl6) · [award source](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)<br>  **Area:** NLP & Language · **Task:** LLM Analysis & Evaluation · **Model:** LLM / Transformer
- **Outstanding Paper** — [Transformers are Inherently Succinct](https://openreview.net/forum?id=Yxz92UuPLQ) · [award source](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/)<br>  **Area:** ML Theory & Optimization · **Task:** Optimization & Generalization · **Model:** Transformer / Theory / Analysis
- **Outstanding Paper Honorable Mention** — [The Polar Express: Optimal Matrix Sign Methods and their Application to the Muon Algorithm](https://openreview.net/forum?id=yRtgZ1K8hO) · [award source](https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/) · `secondary`<br>  **Area:** ML Theory & Optimization · **Task:** Optimization & Generalization · **Model:** Optimization / Theory / Analysis

### ICML · 2026

**International Conference on Machine Learning** · [Machine Learning](https://icml.cc/)

- **Outstanding Paper** — [High-Accuracy Sampling for Diffusion Models and Log-Concave Distributions](https://proceedings.mlr.press/v306/chen26p.html) · [award source](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/)<br>  **Area:** ML Theory & Optimization · **Task:** Probabilistic Inference & Sampling · **Model:** Diffusion / Probabilistic / Bayesian
- **Outstanding Paper** — [The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models](https://proceedings.mlr.press/v306/ni26e.html) · [award source](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/)<br>  **Area:** ML Theory & Optimization · **Task:** LLM Analysis & Evaluation · **Model:** LLM / Transformer / Diffusion
- **Outstanding Paper Honorable Mention** — [A Random Matrix Theory Perspective on the Consistency of Diffusion Models](https://proceedings.mlr.press/v306/wang26kf.html) · [award source](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/) · `secondary`<br>  **Area:** ML Theory & Optimization · **Task:** Generative Modeling · **Model:** Diffusion / Theory / Analysis
- **Outstanding Paper Honorable Mention** — [How much can language models memorize?](https://proceedings.mlr.press/v306/morris26a.html) · [award source](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/) · `secondary`<br>  **Area:** NLP & Language · **Task:** LLM Analysis & Evaluation · **Model:** LLM / Transformer / Theory / Analysis
- **Outstanding Paper Honorable Mention** — [Motion Attribution for Video Generation](https://proceedings.mlr.press/v306/wu26aq.html) · [award source](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/) · `secondary`<br>  **Area:** Computer Vision · **Task:** Image & Video Generation · **Model:** Diffusion / Neural Model
- **Outstanding Paper Honorable Mention** — [The Obfuscation Atlas: Mapping Where Honesty Emerges in RLVR with Deception Probes](https://proceedings.mlr.press/v306/taufeeque26a.html) · [award source](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/) · `secondary`<br>  **Area:** Responsible AI & Privacy · **Task:** Safety, Fairness & Privacy · **Model:** LLM / RL / Theory / Analysis
- **Outstanding Paper Honorable Mention** — [To Grok Grokking: Provable Grokking in Ridge Regression](https://proceedings.mlr.press/v306/xu26bd.html) · [award source](https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/) · `secondary`<br>  **Area:** ML Theory & Optimization · **Task:** Optimization & Generalization · **Model:** Optimization / Theory / Analysis

### NAACL · 2025

**Annual Conference of the Nations of the Americas Chapter of the ACL** · [Natural Language Processing](https://naacl.org/)

- **Best Paper** — [The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models](https://aclanthology.org/2025.naacl-long.303/) · [award source](https://2025.naacl.org/blog/best-papers/)<br>  **Area:** NLP & Language · **Task:** LLM Analysis & Evaluation · **Model:** LLM / Transformer

### NeurIPS · 2025

**Conference on Neural Information Processing Systems** · [Machine Learning](https://neurips.cc/)

- **Best Paper** — [1000 Layer Networks for Self-Supervised RL: Scaling Depth Can Enable New Goal-Reaching Capabilities](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e74ee34cc0f2d0780f34ee77d8fba25b-Abstract-Conference.html) · [award source](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)<br>  **Area:** Reinforcement Learning & Decision Making · **Task:** Reinforcement Learning & Planning · **Model:** Representation Learning / RL
- **Best Paper** — [Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond)](https://proceedings.neurips.cc/paper_files/paper/2025/hash/754d5a526a5ee5a47220664a0eb92751-Abstract-Datasets_and_Benchmarks_Track.html) · [award source](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)<br>  **Area:** NLP & Language · **Task:** LLM Analysis & Evaluation · **Model:** LLM / Transformer
- **Best Paper** — [Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free](https://proceedings.neurips.cc/paper_files/paper/2025/hash/904e89bb4e632e75fb47f093b620b257-Abstract-Conference.html) · [award source](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)<br>  **Area:** NLP & Language · **Task:** Model Efficiency & Architecture · **Model:** LLM / Transformer
- **Best Paper** — [Why Diffusion Models Don’t Memorize: The Role of Implicit Dynamical Regularization in Training](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ceb7f3cc876a6dcb15130a645b5a4507-Abstract-Conference.html) · [award source](https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/)<br>  **Area:** ML Theory & Optimization · **Task:** Generative Modeling · **Model:** Diffusion / Theory / Analysis

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
