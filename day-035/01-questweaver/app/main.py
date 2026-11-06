from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from . import world,engine
from .schemas import QuestRequest,QuestProposal
ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="QuestWeaver",version="1.0.0",description="World-aware quest generation and validation.")
app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static")
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text()
@app.get("/api/world")
def get_world():return world.snapshot()
@app.post("/api/world/reset")
def reset():return world.reset()
@app.post("/api/quests/generate")
def generate(req:QuestRequest):return engine.propose(req.tone,req.max_results)
@app.post("/api/quests/validate")
def validate(q:QuestProposal):return engine.validate_proposal(q.model_dump())
@app.post("/api/quests/accept")
def accept(q:QuestProposal):
 r=engine.accept(q.model_dump())
 if not r["accepted"]:raise HTTPException(422,r)
 return r
@app.post("/api/quests/complete/{quest_id}")
def complete(quest_id:str):
 from .lifecycle import complete as finish
 r=finish(quest_id)
 if not r["ok"]:raise HTTPException(404,r)
 return r