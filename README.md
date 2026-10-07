# MedVision-2D3D

> **AI-driven multi-view knee landmark detection and 2D-to-3D reconstruction research**

MedVision-2D3D is an interdisciplinary research project focused on developing a computer-vision pipeline for extracting meaningful 3D information from multiple 2D observations of the knee.

The **current implementation stage** focuses on detecting and tracking standardized knee landmarks from 2D video captured using a four-camera setup. The resulting multi-view landmark data is intended to provide the foundation for later 3D reconstruction, biomechanical analysis, and expert-guided clinical interpretation.

A new systems-engineering direction discussed on **20 August 2026** is a rover-based camera platform designed to support smooth sideways camera movement and maintain useful observation while the subject moves. This is currently a proposed extension and is not yet represented as a completed hardware system.

> ⚠️ **Research status:** The project is under active development. The exact anatomical terminology, dataset characteristics, model architecture, evaluation protocol, rover design, control strategy, and later clinical objectives will be finalized as the dataset and expert/industrial guidance become available.

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

### New hardware extension

The 20 August 2026 meeting introduced a proposed rover/camera layer around the capture system:

```text
Moving Subject
      ↓
Dynamic Rover-Based Camera Platform
      ↓
Smooth Camera Movement / Subject Following
      ↓
Multi-View Video Capture
      ↓
20-Point Knee Landmark Detection
      ↓
Temporal Tracking
      ↓
Future Multi-View 3D Analysis
```

The rover is currently a **proposed hardware extension**. The immediate AI priority remains reliable landmark detection and temporal tracking.

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

## 🤖 Rover / Dynamic Camera Direction

The rover concept is intended to solve a practical capture problem: a moving subject can leave the useful field of view of a fixed camera or produce less useful viewpoints during movement.

### Current concept

- A camera is mounted on a mobile rover/platform.
- The platform is intended to provide controlled sideways movement.
- The camera should move smoothly while maintaining observation of the subject.
- Subject-following and camera-positioning logic can be developed and validated separately from the landmark model.
- The rover will eventually feed the same perception pipeline rather than becoming a separate analysis system.

### Development strategy

The rover should be developed incrementally:

```text
Manual / controlled rover movement
              ↓
Camera-following control logic
              ↓
Subject tracking integration
              ↓
Smooth movement validation
              ↓
Integration with multi-camera capture
```

The physical rover design, motors, control electronics, navigation method, and final tracking algorithm are still under development and should not be treated as finalized specifications.

More detailed planning is documented in:

`docs/rover-camera-system.md`

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

### Stage 3 — Video-Based Temporal Tracking ⏳

- Track landmarks across consecutive frames
- Analyze landmark trajectories
- Evaluate tracking consistency

### Stage 4 — Rover / Dynamic Camera Prototype 🆕

- Define the camera platform movement requirements
- Prototype controlled sideways movement
- Develop subject-following / camera-positioning logic
- Validate smooth camera motion
- Integrate the camera layer with the perception pipeline

### Stage 5 — Multi-View Analysis ⏳

- Associate corresponding landmarks across camera views
- Establish multi-view consistency
- Prepare data for 3D reconstruction

### Stage 6 — 3D Reconstruction ⏳

- Investigate reconstruction methods
- Estimate 3D landmark positions
- Validate reconstruction against appropriate ground truth when available

### Stage 7 — Biomechanical / Clinical Analysis ⏳

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
│   ├── rover-camera-system.md      # New rover/dynamic-camera direction
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
│   │   └── knee_landmark/          # Knee landmark detector
│   ├── tracking/                   # Temporal landmark tracking
│   ├── evaluation/                 # Evaluation utilities
│   └── visualization/              # Landmark/tracking visualization
│
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
Rover / Dynamic Camera Integration
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
- Future rover control / embedded components as the hardware design is finalized

The repository intentionally avoids committing model-specific dependencies until the actual dataset and task constraints have been examined.

---

## 📚 Research Documentation

The main research documentation is maintained in:

- `docs/research-problem.md` — current research question, scope, input/output and future direction
- `docs/literature-review.md` — literature review and research matrix
- `docs/supervisor-meetings.md` — formal supervisor discussions and task clarification
- `docs/rover-camera-system.md` — proposed rover and dynamic-camera direction

Detailed meeting notes should record decisions and implementation direction while avoiding restricted or patent-sensitive information.

---

## 🔐 Data, IP and Research Ethics

This repository is intended for research documentation and reproducible code development.

The following should not be publicly committed without explicit authorization:

- Patient-identifiable information
- Clinical videos/images
- Restricted datasets
- Unpublished sensitive research material
- Patent-sensitive implementation details
- Credentials or private configuration

Kanthi Mam is currently preparing a patent application based on the team's research approach. Until the research team confirms what can be disclosed publicly, patent-sensitive implementation details should remain outside this public repository.

Raw clinical data should remain in the approved storage environment.

---

## 🚧 Current Status

**Research phase:** Initial AI/computer-vision task definition and system-design expansion.

**Current AI focus:** Four-camera 2D knee landmark detection and temporal tracking using the standardized 20-point reference.

**New systems direction:** Prototype a rover-mounted camera platform for controlled sideways movement and smoother subject tracking.

**Next AI milestone:** Receive and inspect the actual dataset and annotation resources before selecting and training the baseline model.

**Next systems milestone:** Define and prototype the rover/camera movement requirements without committing to an unverified hardware architecture.

The model architecture, final evaluation metrics, rover control method, and later 2D-to-3D/clinical methodology will be determined from the available data, literature, and supervisor/orthopedic/industrial expert guidance.

---

## 👥 Research Collaboration

MedVision-2D3D is an interdisciplinary research effort involving **Computer Science and Electronics & Communication Engineering**, with future clinical interpretation informed by orthopedic expertise and project development receiving industrial guidance.

> This repository documents the research process while protecting restricted clinical, unpublished, and patent-sensitive research material.
