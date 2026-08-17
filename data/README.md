# Dataset Structure

The MedVision-2D3D project is designed around synchronized multi-view 2D video capture.

## Camera Configuration

The initial experimental setup consists of four camera views:

| Camera | View | Purpose |
|---|---|---|
| `front` | Front | Observe the subject from the front |
| `rear` | Rear | Observe the subject from the rear |
| `left_side` | Left lateral | Observe the left side of the subject |
| `right_side` | Right lateral | Observe the right side of the subject |

The four views are intended to provide complementary 2D observations of the subject's left and right knees during walking.

## Initial Data Pipeline

```text
Four Camera Videos
        │
        ▼
Frame Extraction
        │
        ▼
Knee Landmark Detection
        │
        ▼
2D Landmark Coordinates
        │
        ▼
Temporal Tracking
        │
        ▼
Multi-View Landmark Data