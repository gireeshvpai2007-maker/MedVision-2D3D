# Landmark Tracking

This module will contain algorithms for tracking detected knee landmarks across consecutive video frames.

## Initial Objective

Maintain consistent landmark identities over time.

```text
Frame t
   ↓
Detected landmarks
   ↓
Frame t+1
   ↓
Updated landmark positions
   ↓
Temporal trajectories