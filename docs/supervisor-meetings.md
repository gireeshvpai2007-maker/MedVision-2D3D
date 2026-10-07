# Supervisor Meetings

## 2026-08-15 — Initial Research Discussion

### Status

The supervisor will provide the complete research problem, resources, and project details on Monday.

### Current understanding

- Research direction: medical-imaging-based 2D-to-3D reconstruction / related 2D/3D methods.
- Current literature focus: knee and lower-limb reconstruction.
- CSE contribution is expected to involve algorithm development.
- Literature review and related papers are being studied before implementation.

### Pending clarification

- Exact anatomical structure
- Exact imaging modality
- Dataset and data-access conditions
- Ground-truth 3D representation
- Reconstruction vs. registration objective
- Required algorithmic contribution
- Baseline methods
- Evaluation metrics
- Publication / target venue requirements

### Action before next meeting

- Continue reading the core papers.
- Maintain the literature matrix.
- Do not commit patient data or unpublished research material.
- Do not begin the final algorithm implementation until the research problem is confirmed.

## 2026-08-17 — Task and Approach Clarification

### Assigned Initial Task

The initial CSE/AI component focuses on developing a model to identify and track standardized knee landmarks from 2D video.

### Experimental Setup

The intended setup consists of four camera views:

- Front
- Rear
- Left side
- Right side

The cameras observe the subject while walking through the experimental setup.

### Landmark Representation

The knee landmarks will initially be represented using the numbered points provided in the reference image.

The anatomical names of the numbered landmarks are not yet finalized and will be confirmed with the supervisor / orthopedic expert.

The same landmark numbering should be maintained consistently across the four camera views wherever the landmark is visible.

### Initial Model Objective

For each frame of the 2D video, the model should identify the predefined knee landmarks and determine their 2D image coordinates.

The expected output for each detected landmark is:

- Landmark ID
- X coordinate
- Y coordinate
- Confidence score

The landmarks should then be tracked across consecutive frames.

### Initial Pipeline

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
```

### Future Direction

After establishing reliable 2D landmark detection and tracking, the project is expected to progress toward:

- Multi-view landmark correspondence
- 3D reconstruction
- Biomechanical analysis
- Identification of abnormal movement patterns
- Clinical interpretation using expert-labelled data

The later stages are expected to use data and clinical knowledge provided by orthopedic experts.

### Current Scope Boundary

The current task is limited to knee landmark detection and tracking.

The model is not currently being developed to directly diagnose ACL injury or classify specific knee conditions.

### Immediate Next Steps

- Finalize the numbered landmark schema.
- Obtain and inspect the project dataset.
- Determine the annotation format and available landmark labels.
- Inspect the four camera views and video characteristics.
- Establish the baseline landmark detection approach.
- Evaluate the initial landmark detection before progressing to tracking and multi-view reconstruction.

## 2026-08-20 — Research Meeting: Dynamic Camera/Rover Direction

### Meeting Outcome

The research team discussed extending the experimental setup with a rover-based camera platform. The purpose is to support smoother camera movement and maintain useful camera observation while a subject moves through the capture area.

### Proposed Hardware Direction

- Develop a rover/platform capable of controlled sideways camera movement.
- Use the camera platform to follow the subject's motion and maintain an appropriate viewpoint.
- Treat the rover as a hardware extension of the existing computer-vision pipeline rather than replacing the landmark-detection objective.
- Begin with a controllable proof of concept before attempting a fully autonomous tracking system.

### Updated High-Level System Direction

```text
Moving Subject
      ↓
Dynamic Camera Platform
      ↓
Multi-View Video Capture
      ↓
20-Point Knee Landmark Detection
      ↓
Temporal Tracking
      ↓
Multi-View Analysis
      ↓
Future 3D Reconstruction
```

### Patent / Research Documentation Note

Kanthi Mam is preparing a patent application based on the research approach document submitted by the team. The approach documentation therefore needs to describe the process, stages, inputs, outputs, and transitions more clearly and in greater depth for the research/patent workflow.

Detailed unpublished implementation specifics, sensitive algorithmic details, restricted data, and patent-sensitive material should remain outside this public repository until the research team authorizes their release.

### Industrial Guidance

The team is receiving industrial guidance from Abhishek Rhisheekesan on the project direction and development process.

### Current Development Priority

The immediate CSE priority remains the 20-landmark knee detection and tracking pipeline. The rover/camera movement concept will be treated as a parallel hardware and systems-engineering direction that can be integrated progressively.
