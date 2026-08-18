# 2D-to-3D Reconstruction

This module will contain the geometric pipeline that converts corresponding 2D knee landmarks from multiple calibrated camera views into 3D landmark coordinates.

## Planned components

```text
Camera calibration
      ↓
Multi-view correspondence
      ↓
2D landmark confidence handling
      ↓
Triangulation / reconstruction
      ↓
3D trajectory refinement
      ↓
3D validation
```

## Current status

This module is a research scaffold. No reconstruction algorithm has been selected or treated as final yet.

The method will be selected after the actual four-camera dataset, camera geometry, synchronisation procedure, landmark visibility and available ground truth are confirmed.

## Expected inputs

- Camera calibration parameters
- Synchronized 2D landmark coordinates
- Landmark confidence values
- Camera/view identifiers
- Frame or timestamp information

## Expected output

```text
landmark_id → (X, Y, Z) + reconstruction confidence/error
```

## Research requirements

Any implemented reconstruction method should document:

- camera model and calibration assumptions
- coordinate-system convention
- correspondence strategy
- handling of missing/occluded landmarks
- triangulation or optimisation method
- uncertainty/error estimation
- validation protocol
