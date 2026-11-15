from fastapi import FastAPI,HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.store import store
from app.engine import analyze
from app.metrics import fleet_summary
from app.schemas import SensorPoint,WorkOrder,ScheduleRequest
from app.scheduling import prioritize
app=FastAPI(title="FactoryTwin",version="1.0.0",description="Industrial condition monitoring research prototype")
@app.get("/api/health")
def health():return {"status":"ok","service":"FactoryTwin"}
@app.get("/api/fleet")
def fleet():
 x=analyze(store.rows);return {"summary":fleet_summary(x),"machines":x}
@app.get("/api/machines/{machine_id}")
def machine(machine_id:str):
 x=store.history(machine_id)
 if not x:raise HTTPException(404,"Machine not found")
 return analyze(x)[0]
@app.post("/api/telemetry")
def telemetry(row:SensorPoint):store.ingest(row);return {"accepted":True,"machine_id":row.machine_id}
@app.post("/api/work-orders")
def work_order(order:WorkOrder):
 store.orders.append(order.model_dump());return store.orders[-1]
@app.post("/api/schedule")
def schedule(req:ScheduleRequest):
 risk={x["machine_id"]:x["risk_score"] for x in analyze(store.rows)};items=[{**o,"risk_score":risk.get(o["machine_id"],0)} for o in store.orders];return prioritize(items,req.available_hours)
@app.get("/")
def home():return FileResponse("web/index.html")
app.mount("/static",StaticFiles(directory="web"),name="static")