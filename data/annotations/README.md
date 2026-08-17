# Knee Landmark Annotations

This directory stores annotations for the standardized knee landmark detection task.

## Landmark Standard

The project currently uses the numbered landmark scheme from the approved reference image:

- Landmark 1
- Landmark 2
- ...
- Landmark 20

Anatomical names are intentionally not assigned yet and will be added after confirmation from the project supervisor / orthopedic expert.

## Coordinate Format

Each visible landmark is represented using image pixel coordinates:

- `x` — horizontal pixel coordinate
- `y` — vertical pixel coordinate
- `confidence` — annotation/model confidence where applicable

## Camera Views

The four camera views are:

- `front`
- `rear`
- `left_side`
- `right_side`

The same landmark ID must refer to the same standardized point across all applicable camera views.

## Example

```json
{
  "frame_id": 152,
  "camera": "front",
  "side": "left",
  "landmarks": {
    "1": {
      "x": 421,
      "y": 238,
      "confidence": 1.0
    },
    "2": {
      "x": 436,
      "y": 271,
      "confidence": 1.0
    }
  }
}