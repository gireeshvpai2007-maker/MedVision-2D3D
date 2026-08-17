# Research Problem

## Project

2D-to-3D Reconstruction in Medical Imaging

## Current Research Stage

The initial stage of the project focuses on detecting and tracking standardized knee landmarks from 2D video captured using a four-camera setup.

The landmark definitions are currently represented using the numbered points provided in the project reference image. Anatomical names will be assigned after confirmation from the research supervisor / orthopedic expert.

## Research Question

How can standardized knee landmarks be reliably detected and tracked from synchronized 2D video captured from multiple camera views to provide the foundation for subsequent 3D reconstruction and biomechanical analysis?

## Application Domain

Medical Imaging / Gait and Knee Movement Analysis

## Input

Four-camera 2D video of a subject walking through the experimental setup:

- Front camera
- Rear camera
- Left-side camera
- Right-side camera

The system is intended to observe the left and right knees from multiple views.

## Initial Expected Output

For each relevant frame and camera view, the system should identify the predefined numbered knee landmarks and provide:

- Landmark ID
- X coordinate
- Y coordinate
- Confidence score

The landmarks should also be tracked across consecutive frames.

## Initial Processing Pipeline

```text
Four-Camera 2D Video
        ↓
Frame Extraction
        ↓
Knee Landmark Detection
        ↓
2D Landmark Coordinates
        ↓
Temporal Tracking
        ↓
Multi-View Landmark Data
        ↓
Future 3D Reconstruction