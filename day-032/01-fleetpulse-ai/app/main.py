"""FleetPulse AI REST API and static dashboard."""
from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse,Response
from fastapi.staticfiles import StaticFiles
from .database import initialize
from .schemas import AssetCreate,TelemetryInput,WorkOrderInput,WorkOrderClose
from . import repository
from .health import assess
from .fleet import fleet_summary
from .demo import seed_demo
from .export import telemetry_csv,health_json

ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="FleetPulse AI",version="1.0.0",description="Explainable industrial asset health and predictive maintenance prototype")
@app.on_event("startup")
def startup():initialize()
app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static")
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text(encoding="utf-8")
@app.get("/api/health")
def health():return {"status":"ok","service":"FleetPulse AI"}
@app.get("/api/assets")
def assets():return repository.list_assets()
@app.post("/api/assets")
def create_asset(payload:AssetCreate):
 if payload.pressure_min>=payload.pressure_max:raise HTTPException(422,"pressure_min must be lower than pressure_max")
 try:return repository.add_asset(payload.model_dump())
 except Exception as exc:raise HTTPException(409,"Asset ID already exists or data violates constraints.") from exc
def get_asset_or_404(asset_id):
 asset=repository.get_asset(asset_id)
 if not asset:raise HTTPException(404,"Asset not found")
 return asset
@app.get("/api/assets/{asset_id}")
def asset_detail(asset_id:str):
 a=get_asset_or_404(asset_id);rows=repository.telemetry_for(asset_id)
 return {"asset":a,"health":assess(a,rows),"telemetry":rows}
@app.post("/api/assets/{asset_id}/telemetry")
def ingest(asset_id:str,payload:TelemetryInput):
 get_asset_or_404(asset_id)
 if payload.timestamp is None:
  from datetime import datetime,timezone
  data=payload.model_dump();data["timestamp"]=datetime.now(timezone.utc).isoformat()
 else:data=payload.model_dump()
 return repository.add_telemetry(asset_id,data)
@app.get("/api/assets/{asset_id}/telemetry")
def get_telemetry(asset_id:str,limit:int=300):
 get_asset_or_404(asset_id)
 if not 1<=limit<=5000:raise HTTPException(422,"limit must be between 1 and 5000")
 return repository.telemetry_for(asset_id,limit)
@app.get("/api/assets/{asset_id}/health")
def asset_health(asset_id:str):
 a=get_asset_or_404(asset_id);return assess(a,repository.telemetry_for(asset_id))
@app.get("/api/fleet/summary")
def summary():return fleet_summary()
@app.get("/api/alerts")
def alerts():
 result=fleet_summary()
 return [x for x in result["assets"] if x["priority"] in ("high","critical")]
@app.get("/api/work-orders")
def work_orders(status:str|None=None):return repository.list_work_orders(status)
@app.post("/api/work-orders")
def create_work_order(payload:WorkOrderInput):
 get_asset_or_404(payload.asset_id);return repository.create_work_order(payload.model_dump())
@app.patch("/api/work-orders/{work_order_id}/close")
def close_work_order(work_order_id:int,payload:WorkOrderClose):
 result=repository.close_work_order(work_order_id,payload.resolution_notes)
 if not result:raise HTTPException(404,"Open work order not found")
 return result
@app.post("/api/demo/seed")
def demo():return seed_demo()
@app.get("/api/export/telemetry.csv")
def export_csv(asset_id:str|None=None):
 rows=repository.telemetry_for(asset_id,5000) if asset_id else repository.all_telemetry()
 return Response(telemetry_csv(rows),media_type="text/csv",headers={"Content-Disposition":"attachment; filename=fleetpulse-telemetry.csv"})
@app.get("/api/export/health/{asset_id}.json")
def export_health(asset_id:str):
 a=get_asset_or_404(asset_id);data=assess(a,repository.telemetry_for(asset_id))
 return Response(health_json(data),media_type="application/json",headers={"Content-Disposition":f"attachment; filename={asset_id}-health.json"})
