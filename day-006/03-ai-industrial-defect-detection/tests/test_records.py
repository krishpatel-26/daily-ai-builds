import csv
from io import StringIO
from app.policy import Detection, decide_inspection
from app.records import build_record, records_to_csv

def test_record_contains_decision_and_filename():
    detections = [Detection("scratch", .8)]
    record = build_record("part.png", detections, decide_inspection(detections, {"scratch"}, .5))
    assert record["filename"] == "part.png"
    assert record["status"] == "REVIEW"
    assert record["detection_count"] == 1

def test_csv_export():
    output = records_to_csv([{"filename": "part.png", "status": "PASS"}])
    parsed = list(csv.DictReader(StringIO(output)))
    assert parsed[0]["filename"] == "part.png"
    assert parsed[0]["status"] == "PASS"

def test_empty_csv():
    assert records_to_csv([]) == ""
