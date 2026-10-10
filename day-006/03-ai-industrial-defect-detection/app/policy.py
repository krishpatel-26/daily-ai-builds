from dataclasses import dataclass
from typing import Iterable

@dataclass(frozen=True)
class Detection:
    label: str
    confidence: float
    x1: float = 0.0
    y1: float = 0.0
    x2: float = 0.0
    y2: float = 0.0

@dataclass(frozen=True)
class InspectionDecision:
    status: str
    flagged_labels: tuple[str, ...]
    reason: str

def decide_inspection(
    detections: Iterable[Detection],
    defect_labels: set[str] | frozenset[str],
    confidence_threshold: float,
) -> InspectionDecision:
    labels = {label.strip().lower() for label in defect_labels}
    flagged = sorted({
        d.label.strip().lower() for d in detections
        if d.label.strip().lower() in labels and d.confidence >= confidence_threshold
    })
    if flagged:
        return InspectionDecision("REVIEW", tuple(flagged),
                                  "Configured defect label detected above threshold.")
    return InspectionDecision("PASS", (), "No configured defect label detected above threshold.")
