# Contributing to MedVision-2D3D

MedVision-2D3D is a research repository for AI-based multi-view knee landmark detection and 2D-to-3D reconstruction.

## Research Workflow

```text
Issue → Branch → Commit → Pull Request → Review → Merge
```

## Before You Start

1. Check existing Issues before beginning a task.
2. Create or use an issue describing the work.
3. Work on a feature branch; do not develop directly on `main`.

Example:

```bash
git checkout main
git pull origin main
git checkout -b feature/knee-landmark-model
```

## Branch Naming

Use clear, task-based names:

- `feature/knee-landmark-model`
- `feature/video-preprocessing`
- `feature/temporal-tracking`
- `feature/3d-reconstruction`
- `feature/literature-review`
- `feature/evaluation`

## Commits

Keep commits focused and descriptive.

```bash
git add .
git commit -m "Add baseline knee landmark detector"
git push -u origin feature/knee-landmark-model
```

## Pull Requests

Every substantial contribution should be submitted through a Pull Request to `main`.

A good Pull Request should explain:

- what changed
- which Issue it addresses
- how the change was tested or evaluated
- any assumptions or limitations

Do not merge experimental code just because it runs. Research decisions should be reproducible and documented.

## Repository Rules

- Do not commit patient-identifiable information or restricted clinical data.
- Do not commit raw clinical videos/images unless explicitly authorised.
- Do not commit credentials, API keys, or private configuration.
- Keep notebooks for exploration and move reusable logic into `src/`.
- Document important experiment settings and evaluation results.
- Do not change the canonical landmark definitions without recording the reason and obtaining the required research approval.

## Code Areas

```text
src/
├── preprocessing/     Data and frame preparation
├── models/            AI/ML models
├── tracking/          Temporal landmark tracking
├── reconstruction/    Calibration, correspondence and 2D→3D geometry
├── evaluation/        Metrics and validation
└── visualization/     Research plots and visual outputs
```

## Research Principle

The repository is organised around the research pipeline, not around individual team members. Contributors should own task branches and Issues while keeping the final codebase modular and reproducible.
