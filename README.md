# MedVision-2D3D

> AI-driven 2D-to-3D reconstruction for medical imaging.

## 🔬 Overview

This repository is the research workspace for an interdisciplinary medical-imaging project focused on understanding and developing computational methods for reconstructing useful 3D anatomical information from 2D medical images.

The current research direction is centered on **knee imaging and 2D-to-3D reconstruction**, with emphasis on algorithms, computer vision, optimization, AI/ML, experimentation, and clinical evaluation.

> ⚠️ The exact anatomical target, imaging modality, dataset, and proposed algorithm are intentionally not fixed yet. These will be finalized with the research supervisor.

## 🎯 Current Objectives

- Study existing 2D-to-3D medical imaging methods
- Review classical statistical-shape and optimization-based approaches
- Study AI and deep-learning based reconstruction methods
- Compare datasets, reconstruction strategies, metrics, and limitations
- Identify research gaps that can motivate a new algorithmic contribution
- Maintain reproducible research documentation
- Develop and evaluate the final algorithm after the research problem is finalized

## 🧠 Current Research Pipeline

```text
2D Medical Images
        ↓
Preprocessing / Feature Extraction
        ↓
Reconstruction / Registration Algorithm
        ↓
3D Anatomical Representation
        ↓
Validation Against Ground Truth
        ↓
Clinical / Quantitative Evaluation
```

This is a **working conceptual pipeline** and may change after the supervisor specifies the exact research problem.

## 📚 Literature Progress

The current review work is studying the evolution of knee and lower-limb 2D-to-3D methods:

```text
Statistical Shape Models
        ↓
Geometric Optimization
        ↓
Contour / Landmark-Based Automation
        ↓
AI-Based 2D → 3D Reconstruction
        ↓
Deep-Learning Reconstruction
        ↓
Patient-Level Validation
        ↓
Learned 2D/3D Registration
```

A literature matrix is being maintained in [`docs/literature-review.md`](docs/literature-review.md).

## 📂 Repository Structure

| Directory | Purpose |
|---|---|
| `docs/` | Research problem, literature review, methodology notes, and supervisor meetings |
| `papers/` | Paper list, references, and literature resources |
| `data/` | Dataset organization; raw/processed medical data is not committed without authorization |
| `notebooks/` | Exploratory analysis and research experiments |
| `src/` | Final preprocessing, algorithms, models, and evaluation code |
| `experiments/` | Controlled experiment configurations and results |
| `results/` | Research figures, tables, and visualizations |

## 🛠️ Planned Technologies

- Python
- NumPy
- OpenCV
- SciPy
- scikit-learn
- PyTorch / TensorFlow
- Matplotlib
- Jupyter

The final stack will be selected after the research methodology is finalized.

## 📊 Current Status

### Phase 1 — Literature Foundation ✅

- Supervisor-provided review studied
- Core 2D-to-3D knee reconstruction literature identified
- Classical and AI-based approaches compared conceptually
- Major evaluation concepts identified
- Review draft prepared

### Phase 2 — Research Problem Definition ⏳

**Pending supervisor briefing.**

The following will be finalized after discussion with the supervisor:

- Exact anatomical target
- 2D imaging modality
- Ground-truth 3D source
- Dataset
- Reconstruction vs. registration objective
- Algorithmic contribution expected from the CSE team
- Evaluation protocol

### Phase 3 — Implementation

Not started yet. The algorithm and code structure will be created only after the research problem is finalized.

## 👥 Research

Interdisciplinary research involving **Computer Science and Electronics & Communication Engineering**.

> Note: Research data, unpublished methodology, patient information, and other confidential material are not included in this public repository without appropriate authorization.
