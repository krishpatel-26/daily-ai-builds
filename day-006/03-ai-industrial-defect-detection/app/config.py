import os
from dataclasses import dataclass

def _labels(value: str) -> frozenset[str]:
    return frozenset(x.strip().lower() for x in value.split(",") if x.strip())

@dataclass(frozen=True)
class Settings:
    model_path: str
    confidence: float
    defect_labels: frozenset[str]

def load_settings() -> Settings:
    try:
        confidence = float(os.getenv("DEFECT_CONFIDENCE", "0.35"))
    except ValueError:
        confidence = 0.35
    return Settings(
        model_path=os.getenv("DEFECT_MODEL_PATH", "models/defect_detector.pt"),
        confidence=min(max(confidence, 0.0), 1.0),
        defect_labels=_labels(os.getenv("DEFECT_LABELS", "scratch,crack,dent,contamination")),
    )
