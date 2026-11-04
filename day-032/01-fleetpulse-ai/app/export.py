"""Portable CSV/JSON export helpers."""
import csv,io,json

def telemetry_csv(rows):
 out=io.StringIO()
 fields=["asset_id","timestamp","temperature","vibration","pressure","current","rpm","runtime_hours"]
 writer=csv.DictWriter(out,fieldnames=fields);writer.writeheader()
 for row in rows:writer.writerow({k:row.get(k) for k in fields})
 return out.getvalue()

def health_json(assessment):
 return json.dumps(assessment,indent=2)
