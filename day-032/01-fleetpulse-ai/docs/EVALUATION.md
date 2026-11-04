# Evaluation Plan

## Prototype verification
Unit tests cover feature trend calculations, robust MAD outlier behavior, threshold signals, explainable health output, and exports.

## Before field deployment
Collect labeled operational histories with maintenance timestamps. Split chronologically by asset and plant to prevent leakage. Compare rule baselines with isolation forest, gradient boosting and temporal models. Report precision/recall at actionable alert rates, lead time, false alarms per asset-week, calibration, and maintenance cost impact. Validate across asset types and changing load regimes.