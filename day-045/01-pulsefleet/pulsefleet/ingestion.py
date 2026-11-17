import csv
from pathlib import Path
from .validation import parse_record
def load_csv(path):
 records=[]
 with Path(path).open(newline="",encoding="utf-8") as f:
  for line,row in enumerate(csv.DictReader(f),2):
   try: records.append(parse_record(row))
   except ValueError as exc: raise ValueError(f"CSV line {line}: {exc}") from exc
 return records
def group_by_robot(records):
 grouped={}
 for r in records: grouped.setdefault(r.robot_id,[]).append(r)
 for values in grouped.values(): values.sort(key=lambda x:x.timestamp)
 return grouped
