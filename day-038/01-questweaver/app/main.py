from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .schemas import PlanRequest,ValidateRequest
from . import planner,graph,templates,validator,explain
ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="QuestWeaver",version="0.1.0",description="Adaptive quest generation and planning")
app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static")
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text()
@app.get("/api/catalog")
def catalog():return graph.catalog()
@app.post("/api/plan")
def make_plan(req:PlanRequest):return planner.plan(req.state,req.completed_quests,req.limit)
@app.get("/api/quest/{quest_id}")
def quest(quest_id:str):
 t=next((x for x in templates.TEMPLATES if x["id"]==quest_id),None)
 if not t:raise HTTPException(404,"Quest not found")
 return {"quest":t,"graph":graph.quest_graph(t),"order":graph.topological_order(graph.quest_graph(t))}
@app.post("/api/validate")
def validate(req:ValidateRequest):
 t=next((x for x in templates.TEMPLATES if x["id"]==req.quest_id),None)
 if not t:raise HTTPException(404,"Quest not found")
 return validator.validate_progress(t,req.completed_objectives)
@app.get("/api/health")
def health():return {"status":"ok","templates":len(templates.TEMPLATES)}