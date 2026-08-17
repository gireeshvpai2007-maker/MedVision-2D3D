# Literature Review — 2D-to-3D Medical Imaging

## Purpose

This document records the literature groundwork for the MedVision-2D3D project. The current focus is 2D-to-3D reconstruction and related 2D/3D registration methods for the knee and lower limb.

> **Status:** Preliminary review. The exact research problem, anatomical target, imaging modality, dataset, and proposed contribution will be finalized after the supervisor briefing.

## Core Literature Matrix

| Paper / Year | Problem | Input | Main Approach | Evaluation | Key Takeaway |
|---|---|---|---|---|---|
| Baka et al. (2011) | 3D distal-femur reconstruction | Stereo X-ray | Statistical Shape Model + 2D/3D fitting | Shape reconstruction accuracy | Anatomical shape priors constrain an otherwise ill-posed 2D-to-3D problem |
| Baka et al. (2014) | Knee kinematics without patient-specific CT/MRI models | Biplane fluoroscopy | Personalizable statistical shape models | Kinematic precision and reconstruction accuracy | Reconstruction should be evaluated according to the downstream clinical task |
| Gajny et al. (2022) | Automated lower-limb reconstruction | Low-dose biplanar radiographs | Statistical Shape Models + contour matching | Shape accuracy and clinical parameters | Automation can reduce manual intervention while retaining useful accuracy |
| AI-based TKA reconstruction (2023) | 2D radiographs to 3D bone models | 2D radiographs | AI-based reconstruction | Anatomical accuracy, reliability, repeatability | AI-based reconstruction can support clinically relevant measurements |
| Factor et al. (2024) | Patient-level TKA validation | Preoperative radiographs | AI 2D-to-3D reconstruction | Mesh RMSE, landmarks, simulated cuts | Real-patient validation is essential for assessing generalization |
| Roth et al. (2024) | 3D lower-limb reconstruction for osteotomy planning | Biplanar radiographs / DRRs | Deep-learning pipeline | Dice, geometric error, clinical planning parameters | Complex reconstruction can be divided into landmark, separation and reconstruction tasks |
| Recent 2D/3D registration work (2026) | Aligning 3D knee models with fluoroscopic images | Fluoroscopy + 3D model | Learned perceptual similarity + differentiable registration | Registration / pose error | Learned image similarity can improve optimization-based registration |

## Major Method Families

### 1. Statistical Shape Models

Statistical Shape Models represent anatomical variation learned from a population of 3D shapes. Instead of searching over arbitrary 3D geometries, reconstruction is constrained to plausible anatomical shapes.

### 2. Projection and Optimization

A candidate 3D anatomical model can be projected into the imaging geometry to create a simulated 2D image. The candidate is then adjusted to reduce disagreement between the simulated and observed image.

### 3. Contour and Landmark Matching

Image contours and anatomical landmarks provide geometric constraints. These approaches can reduce manual work and provide interpretable intermediate information.

### 4. AI / Deep Learning

Deep-learning methods learn relationships between 2D image information and 3D anatomical representations. Some pipelines divide the problem into smaller tasks such as landmark localization, image separation, segmentation, and reconstruction.

### 5. 2D/3D Registration

Registration is related to, but distinct from, reconstruction. In registration, a 3D model already exists and the goal is to estimate its position and orientation relative to a 2D image.

## Important Evaluation Concepts

- **Ground truth:** A trusted reference, often derived from CT segmentation in the studies reviewed.
- **RMSE / geometric error:** Measures distance between reconstructed and reference geometry.
- **Dice coefficient:** Measures overlap between predicted and reference regions.
- **Landmark error:** Measures distance between predicted and reference anatomical landmarks.
- **Reliability / repeatability:** Determines whether measurements remain consistent across observers or repeated evaluations.
- **Clinical parameters:** Reconstruction should ultimately be evaluated according to the measurements or planning tasks it is intended to support.

## Research Questions to Investigate

1. How well do existing methods generalize across patient anatomies and pathological cases?
2. How much does performance depend on the number and geometry of available 2D views?
3. How should reconstruction accuracy be balanced against clinically relevant measurements?
4. Can the pipeline be made more automated while remaining interpretable and reproducible?
5. What ground-truth data and evaluation protocol are appropriate for the intended clinical task?
6. Can classical geometric constraints and learned models be combined effectively?

## Next Step

After the supervisor briefing, this document will be revised to match the exact project scope. The final review will then focus on the selected anatomy, imaging modality, dataset, algorithmic contribution, baseline methods, and evaluation metrics.
