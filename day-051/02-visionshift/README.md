# VisionShift — Active Learning & Model Drift Engineering Lab

**Day 051/365 · Wednesday build 02.** A hands-on ML research system for testing what happens when an industrial visual-inspection classifier encounters a shifted input distribution and a limited labeling budget.

## Real implementation
- Reproducible **synthetic numerical inspection features** (not actual images).
- Binary defect-label simulation with both covariate and modest concept shift.
- Logistic regression fit by batch gradient descent, implemented from scratch.
- Accuracy, F1, precision, recall, Brier score, calibration error, confusion matrices.
- **Population Stability Index (PSI)** on each feature.
- Three label acquisition strategies: random, uncertainty sampling, greedy diversity.
- Eight-seed matched benchmarking and approximate confidence intervals.
- Local responsive evaluation dashboard and unlabeled review queue.

## Run
Python 3.11+, no third-party packages.

```bash
python -m visionshift.server
```

Open http://127.0.0.1:4207. Tests: `python -m unittest discover -s tests -v`.

## Research boundary
This tool uses **fictional numeric features and oracle labels**, not a real image corpus, industrial camera, CNN, YOLO model, or validated defect-detection accuracy. PSI measures distribution change, not model correctness. The active-learning benchmark does not guarantee performance improvement. Integration with real vision systems requires calibrated labels, independent holdouts, bias analysis, monitoring security, and expert review.
