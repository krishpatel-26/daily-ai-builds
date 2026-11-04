# Data Dictionary

| Field | Meaning | Unit |
|---|---|---|
| temperature | Bearing or process temperature | °C |
| vibration | Overall vibration magnitude | mm/s assumed; sensor-dependent |
| pressure | Process pressure | site-specific |
| current | Motor current | A |
| rpm | Rotational speed | rpm |
| runtime_hours | Accumulated operating time | hours |
| health_index | Rule-based condition indicator | 0–100 |
| anomaly_score | Combined heuristic anomaly signal | 0–100 |

Units and sensor locations must be explicitly mapped and calibrated in any deployment.