from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from . import world,engine,metrics
from .schemas import TurnRequest,PolicyRequest
ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="AgentArena",version="0.1.0",description="Multi-agent policy simulation sandbox")
app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static")
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text()
@app.get("/api/state")
def state():return {"world":world.snapshot(),"metrics":metrics.summary(world.STATE)}
@app.post("/api/turn")
def turn(req:TurnRequest):return {"turns":engine.run(req.steps),"metrics":metrics.summary(world.STATE)}
@app.post("/api/reset")
def reset():return world.reset()
@app.post("/api/policy")
def policy(req:PolicyRequest):
 if req.agent_id not in world.STATE["agents"]:raise HTTPException(404,"Unknown agent")
 world.STATE["agents"][req.agent_id]["policy"]=req.policy;return {"agent_id":req.agent_id,"policy":req.policy}
@app.get("/api/replay")
def replay():return engine.replay()
@app.get("/api/metrics")
def get_metrics():return metrics.summary(world.STATE)