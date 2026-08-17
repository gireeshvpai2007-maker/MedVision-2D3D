# MedVision-2D3D

> **AI-driven multi-view knee landmark detection and 2D-to-3D reconstruction research**

MedVision-2D3D is an interdisciplinary research project focused on developing a computer-vision pipeline for extracting meaningful 3D information from multiple 2D observations of the knee.

The **current implementation stage** focuses on detecting and tracking standardized knee landmarks from 2D video captured using a four-camera setup. The resulting multi-view landmark data is intended to provide the foundation for later 3D reconstruction, biomechanical analysis, and expert-guided clinical interpretation.

> ⚠️ **Research status:** The project is under active development. The exact anatomical terminology, dataset characteristics, model architecture, evaluation protocol, and later clinical objectives will be finalized as the dataset and expert guidance become available.

---

## 🔬 Current Research Objective

The initial CSE/AI task is to identify and track predefined knee landmarks from four camera views:

- **Front**
- **Rear**
- **Left side**
- **Right side**

The current landmark reference contains **20 numbered landmarks**. For the initial implementation, the landmarks are represented by their numerical IDs rather than assumed anatomical names. Anatomical terminology will be assigned after confirmation from the research supervisor / orthopedic expert.

### Initial model output

For each visible landmark in a frame:

```text
Landmark ID → (x, y) + confidence
```

The system will then track these landmark coordinates across consecutive video frames.

---

## 🎯 Research Pipeline

```text
                 FOUR CAMERA 2D VIDEO
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       Front           Rear        Left / Right
          │              │              │
          └──────────────┼──────────────┘
                         ↓
                  Frame Extraction
                         ↓
                Knee Landmark Detection
                         ↓
                 2D Coordinates (x, y)
                         ↓
                   Confidence Scores
                         ↓
                  Temporal Tracking
                         ↓
               Multi-View Correspondence
                         ↓
                  Future 3D Reconstruction
                         ↓
               Biomechanical Analysis
                         ↓
             Expert-Guided Interpretation
```

### Current scope

The present stage is **landmark detection and tracking**. It is not currently intended to directly diagnose ACL injury or classify specific knee conditions.

Clinical interpretation and condition-specific analysis are planned only for later stages after sufficient data and expert-labelled information are available.

---

## 📌 Landmark Standard

The project currently uses the numbered landmark scheme from the approved reference image:

```text
1, 2, 3, ... 20
```

The canonical schema is maintained in:

`config/landmarks.yaml`

Each landmark is represented using image-pixel coordinates with:

- `x` — horizontal coordinate
- `y` — vertical coordinate
- `confidence` — model/annotation confidence where applicable

The coordinate convention currently uses the **top-left image origin**, with `x` increasing to the right and `y` increasing downward.

---

## 📷 Four-Camera Data Design

The intended data organization is:

```text
data/
├── raw/
│   ├── front/
│   ├── rear/
│   ├── left_side/
│   └── right_side/
│
├── processed/
│
└── annotations/
```

The four views provide complementary 2D observations of the subject while walking through the experimental setup.

Patient/clinical video and other restricted research data should **not** be committed to this public repository.

---

## 🧠 Development Stages

### Stage 1 — Dataset Understanding 🔄

- Inspect the available dataset
- Verify the four camera views
- Understand image/video characteristics
- Inspect annotation format
- Verify the numbered landmark definitions
- Determine left/right knee representation

### Stage 2 — 2D Landmark Detection ⏳

- Prepare the training data
- Establish a baseline keypoint-detection approach
- Detect the 20 standardized landmarks
- Produce `(x, y)` coordinates and confidence values
- Evaluate localization accuracy

### Stage 3 — Temporal Tracking ⏳

- Track landmarks across consecutive frames
- Analyze landmark trajectories
- Evaluate tracking consistency

### Stage 4 — Multi-View Analysis ⏳

- Associate corresponding landmarks across camera views
- Establish multi-view consistency
- Prepare data for 3D reconstruction

### Stage 5 — 3D Reconstruction ⏳

- Investigate reconstruction methods
- Estimate 3D landmark positions
- Validate reconstruction against appropriate ground truth when available

### Stage 6 — Biomechanical / Clinical Analysis ⏳

- Extract movement-related features
- Investigate normal and abnormal movement patterns
- Incorporate orthopedic expert knowledge and labelled data
- Explore condition-specific interpretation in later research stages

---

## 📂 Repository Structure

```text
MedVision-2D3D/
│
├── config/
│   └── landmarks.yaml              # Canonical 20-landmark schema
│
├── data/
│   ├── raw/                        # Local/restricted camera data
│   │   ├── front/
│   │   ├── rear/
│   │   ├── left_side/
│   │   └── right_side/
│   ├── processed/                  # Processed local datasets
│   └── annotations/                # Annotation documentation/data format
│
├── docs/
│   ├── literature-review.md        # Literature review and research matrix
│   ├── research-problem.md         # Current research problem and scope
│   └── supervisor-meetings.md      # Formal supervisor meeting record
│
├── experiments/
│   └── landmark-detection/         # Controlled landmark-detection experiments
│
├── notebooks/                      # Exploratory research notebooks
│
├── results/
│   ├── figures/                    # Research figures
│   ├── tables/                     # Result tables
│   └── visualizations/             # Prediction/tracking visualizations
│
├── src/
│   ├── preprocessing/              # Data and frame preprocessing
│   ├── models/                     # AI/ML models
│   │   └── knee_landmark/           # Knee landmark detector
│   ├── tracking/                   # Temporal landmark tracking
│   ├── evaluation/                 # Evaluation utilities
│   └── visualization/              # Landmark/tracking visualization
│
├── meeting_notes.md                # Detailed working notes
├── requirements.txt                # Current Python environment
├── .gitignore
└── README.md
```

---

## 📓 Research Workflow

The repository follows a reproducible research workflow:

```text
Literature Review
      ↓
Research Problem Definition
      ↓
Dataset Inspection
      ↓
Annotation Standardization
      ↓
Baseline Model
      ↓
Experiments
      ↓
Evaluation
      ↓
Tracking
      ↓
Multi-View Analysis
      ↓
3D Reconstruction
```

Research decisions, experiments, assumptions, and results should be documented rather than kept only in code or notebooks.

---

## 🛠️ Planned / Current Technology Stack

The project currently uses Python-based research tooling, with the final ML stack to be selected after dataset inspection and baseline-method analysis.

- Python
- NumPy
- Pandas
- OpenCV
- PyYAML
- Matplotlib
- Jupyter
- Future ML framework/model dependencies as required

The repository intentionally avoids committing model-specific dependencies until the actual dataset and task constraints have been examined.

---

## 📚 Research Documentation

The main research documentation is maintained in:

- `docs/research-problem.md` — current research question, scope, input/output and future direction
- `docs/literature-review.md` — literature review and research matrix
- `docs/supervisor-meetings.md` — formal supervisor discussions and task clarification
- `meeting_notes.md` — detailed working notes and implementation direction

---

## 🔐 Data and Research Ethics

This repository is intended for research documentation and reproducible code development.

The following should not be publicly committed without explicit authorization:

- Patient-identifiable information
- Clinical videos/images
- Restricted datasets
- Unpublished sensitive research material
- Credentials or private configuration

Raw clinical data should remain in the approved storage environment.

---

## 🚧 Current Status

**Research phase:** Initial AI/computer-vision task definition and repository setup.

**Current focus:** Four-camera 2D knee landmark detection and temporal tracking.

**Next milestone:** Receive and inspect the actual dataset and annotation resources before selecting and training the baseline model.

The model architecture, final evaluation metrics, and later 2D-to-3D/clinical methodology will be determined from the available data, literature, and supervisor/orthopedic expert guidance.

---

## 👥 Research Collaboration

MedVision-2D3D is an interdisciplinary research effort involving **Computer Science and Electronics & Communication Engineering**, with future clinical interpretation informed by orthopedic expertise.

> This repository documents the research process while protecting restricted clinical and unpublished research material.
