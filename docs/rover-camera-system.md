# Rover / Dynamic Camera System

## Status

**Proposed system direction — 20 August 2026**

This document records the high-level rover/camera concept discussed during the research meeting. It is intentionally kept at the system-design level while the hardware architecture, control strategy, and patent-sensitive details are being finalized.

## 1. Motivation

The existing research pipeline assumes multiple camera views of a subject moving through an experimental setup. A fixed camera can become less useful when the subject changes position or when the viewpoint becomes unsuitable during movement.

The proposed hardware extension is a mobile camera platform that can move smoothly, particularly sideways, to maintain useful observation of the moving subject.

## 2. High-Level Concept

```text
Moving Subject
      ↓
Rover-Based Camera Platform
      ↓
Controlled / Smooth Camera Movement
      ↓
Subject Observation
      ↓
2D Video Frames
      ↓
Knee Landmark Detection
      ↓
Temporal Tracking
      ↓
Multi-View Analysis
```

The rover is therefore a **capture-system extension**. It does not replace the AI landmark-detection pipeline.

## 3. Initial Functional Requirements

The exact specifications are not finalized. The current functional requirements are:

- Support controlled sideways camera movement.
- Provide sufficiently smooth movement for video capture.
- Carry the required camera safely and consistently.
- Maintain useful observation of the moving subject.
- Provide a controllable interface for movement commands.
- Allow later integration with subject-tracking logic.
- Avoid introducing unnecessary motion that degrades landmark detection.

## 4. Development Strategy

The hardware and software should be developed incrementally:

### Phase 1 — Controlled movement

Demonstrate reliable manual or programmatic sideways movement of the camera platform.

### Phase 2 — Camera stabilization / smoothness

Tune movement so that camera motion does not unnecessarily degrade the captured video.

### Phase 3 — Subject-following logic

Use subject-position information to estimate the desired camera movement direction and maintain a useful viewpoint.

### Phase 4 — Perception integration

Connect camera movement with the existing video-processing pipeline and verify that landmark detection remains stable while the camera moves.

### Phase 5 — Multi-view integration

Investigate how the dynamic camera can coexist with the intended four-camera capture arrangement and future multi-view reconstruction.

## 5. Relationship to the AI Pipeline

The current CSE/AI responsibility remains:

```text
Video
 ↓
20 Landmark Detection
 ↓
(x, y) + Confidence
 ↓
Temporal Tracking
```

The rover adds a preceding capture layer:

```text
Subject movement
      ↓
Camera-positioning system
      ↓
Video capture
      ↓
20-landmark AI pipeline
```

This separation is important because the landmark model can be developed and validated independently before the complete rover system is available.

## 6. Validation Targets

The first tests should focus on measurable engineering behaviour rather than claiming a finished autonomous system.

Potential validation measures include:

- Camera position tracking error.
- Smoothness / stability of camera movement.
- Subject retention within the useful camera field of view.
- Video quality during rover movement.
- Landmark detection confidence while the camera is stationary versus moving.
- Landmark tracking consistency during camera movement.

The exact metrics and thresholds will be finalized after the hardware and dataset constraints are known.

## 7. Open Questions

The following are intentionally unresolved:

- Rover mechanical design.
- Motor and actuator selection.
- Camera mounting mechanism.
- Maximum movement range and speed.
- Movement controller / embedded platform.
- Subject-tracking method used for camera control.
- Whether the rover is used as one camera in a four-camera system or as a separate dynamic capture stage.
- Synchronization requirements between moving and fixed cameras.

These should be decided through further supervisor and industrial guidance rather than assumed in the public documentation.

## 8. IP / Patent Note

The research team is preparing a patent application around the broader research approach. Consequently, this public document intentionally avoids confidential mechanical drawings, control parameters, unpublished algorithmic details, and other potentially patent-sensitive implementation information.
