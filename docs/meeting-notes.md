# Meeting Notes

This file contains working notes and discussions related to the MedVision-2D3D research project.

---

## 2026-08-17 — Knee Landmark Detection Approach

### Discussion

The initial CSE task was clarified as developing an AI/computer-vision pipeline to identify and track different parts of the knee from 2D video.

The initial focus is **not diagnosis**. The first objective is reliable identification of standardized knee landmarks.

### Camera Setup

The experimental setup is expected to use four cameras:

- Front camera
- Rear camera
- Left-side camera
- Right-side camera

The cameras capture the subject while walking through the experimental setup.

### Landmark Definition

The current reference image contains numbered landmarks representing different parts of the knee.

For the initial implementation, the landmarks will be represented only using their numerical identifiers:

```text
1, 2, 3, ... 20