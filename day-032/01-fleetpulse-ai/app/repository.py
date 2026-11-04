"""Persistence functions."""
from .database import connect

def add_asset(a):
 with connect() as db:
  db.execute("""INSERT INTO assets(asset_id,name,asset_type,location,criticality,temperature_limit,vibration_limit,pressure_min,pressure_max)
  VALUES(?,?,?,?,?,?,?,?,?)""",tuple(a[k] for k in ("asset_id","name","asset_type","location","criticality","temperature_limit","vibration_limit","pressure_min","pressure_max")))
 return get_asset(a["asset_id"])
def get_asset(asset_id):
 with connect() as db:
  r=db.execute("SELECT * FROM assets WHERE asset_id=?",(asset_id,)).fetchone()
 return dict(r) if r else None
def list_assets():
 with connect() as db:return [dict(r) for r in db.execute("SELECT * FROM assets ORDER BY asset_id")]
def add_telemetry(asset_id,t):
 with connect() as db:
  cur=db.execute("""INSERT INTO telemetry(asset_id,timestamp,temperature,vibration,pressure,current,rpm,runtime_hours)
  VALUES(?,?,?,?,?,?,?,?)""",(asset_id,t["timestamp"],t["temperature"],t["vibration"],t["pressure"],t["current"],t["rpm"],t["runtime_hours"]))
  return dict(db.execute("SELECT * FROM telemetry WHERE id=?",(cur.lastrowid,)).fetchone())
def telemetry_for(asset_id,limit=300):
 with connect() as db:
  rows=db.execute("SELECT * FROM telemetry WHERE asset_id=? ORDER BY timestamp DESC,id DESC LIMIT ?",(asset_id,limit)).fetchall()
 return [dict(r) for r in reversed(rows)]
def all_telemetry(limit=10000):
 with connect() as db:return [dict(r) for r in db.execute("SELECT * FROM telemetry ORDER BY timestamp,id LIMIT ?",(limit,))]
def create_work_order(item):
 keys=("asset_id","title","priority","assigned_to","due_date","notes")
 with connect() as db:
  cur=db.execute("INSERT INTO work_orders(asset_id,title,priority,assigned_to,due_date,notes) VALUES(?,?,?,?,?,?)",tuple(item[k] for k in keys))
  return dict(db.execute("SELECT * FROM work_orders WHERE id=?",(cur.lastrowid,)).fetchone())
def list_work_orders(status=None):
 with connect() as db:
  if status:return [dict(r) for r in db.execute("SELECT * FROM work_orders WHERE status=? ORDER BY created_at DESC",(status,))]
  return [dict(r) for r in db.execute("SELECT * FROM work_orders ORDER BY created_at DESC")]
def close_work_order(order_id,notes):
 with connect() as db:
  cur=db.execute("UPDATE work_orders SET status='closed',resolution_notes=?,closed_at=CURRENT_TIMESTAMP WHERE id=? AND status='open'",(notes,order_id))
  if not cur.rowcount:return None
  return dict(db.execute("SELECT * FROM work_orders WHERE id=?",(order_id,)).fetchone())
