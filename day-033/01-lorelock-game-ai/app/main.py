from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from . import world,runtime
from .schemas import ActionProposal,DialogueRequest
from .validation import validate
from .lore import ground
from .mock_agent import propose
ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="LoreLock Game AI",version="1.0.0",description="Hallucination-resistant game agent runtime.")
app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static")
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text()
@app.get("/api/world")
def get_world():return world.snapshot()
@app.post("/api/demo/reset")
def reset():runtime.clear();return world.reset()
@app.post("/api/proposals/validate")
def validate_action(p:ActionProposal):return validate(p)
@app.post("/api/actions/execute")
def execute_action(p:ActionProposal):return runtime.execute(p)
@app.post("/api/dialogue/ground")
def dialogue(p:DialogueRequest):
 if p.actor_id not in world.STATE["actors"]:raise HTTPException(404,"Actor not found")
 return ground(p.question)
@app.get("/api/audit")
def audit():return list(reversed(world.STATE["event_log"]))
@app.post("/api/demo/propose/{kind}")
def demo(kind:str):
 try:p=propose(kind)
 except KeyError:raise HTTPException(404,"Unknown demo case")
 return {"proposal":p.model_dump(),"validation":validate(p)}