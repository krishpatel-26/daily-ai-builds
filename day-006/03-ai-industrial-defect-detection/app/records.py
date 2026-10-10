from datetime import datetime, timezone
from io import StringIO
import csv
from typing import Any
from app.policy import Detection, InspectionDecision

def build_record(filename: str, detections: list[Detection],
                 decision: InspectionDecision) -> dict[str, Any]:
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "filename": filename,
        "status": decision.status,
        "detection_count": len(detections),
        "flagged_labels": ", ".join(decision.flagged_labels),
        "reason": decision.reason,
        "detections": "; ".join(f"{d.label}:{d.confidence:.3f}" for d in detections),
    }

def records_to_csv(records: list[dict[str, Any]]) -> str:
    if not records:
        return ""
    buffer = StringIO()
    writer = csv.DictWriter(buffer, fieldnames=list(records[0].keys()))
    writer.writeheader()
    writer.writerows(records)
    return buffer.getvalue()
