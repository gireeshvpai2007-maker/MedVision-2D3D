# Models

This directory contains model implementations for the MedVision-2D3D pipeline.

## Current model target

The first AI component is **2D knee landmark detection** for the four-camera setup.

```text
2D frame
  ↓
Knee / landmark detector
  ↓
20 landmark IDs
  ↓
(x, y, confidence)
```

The exact architecture will be selected only after the actual dataset and annotation format are inspected.

## Structure

```text
models/
└── knee_landmark/
    ├── dataset.py
    ├── model.py
    ├── train.py
    ├── infer.py
    └── utils.py
```

Model-specific experiments should remain reproducible and should record dataset version, split, configuration, training settings and evaluation metrics.
