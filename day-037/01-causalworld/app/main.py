from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from . import engine,graph,scenarios,analytics
from .schemas import ScenarioRequest,CompareRequest
ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="CausalWorld",version="0.1.0")
app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static")
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text()
@app.get("/api/model")
def model():return {"graph":graph.graph(),"validation":graph.validate_graph(),"variables":scenarios.catalog(),"baseline":engine.simulate()}
@app.get("/api/explain/{variable}")
def explain(variable:str):
 try:return engine.explain(variable)
 except ValueError as e:raise HTTPException(404,str(e))
@app.post("/api/simulate")
def simulate(req:ScenarioRequest):
 try:return scenarios.run(req.name,{x.variable:x.value for x in req.interventions})
 except ValueError as e:raise HTTPException(422,str(e))
@app.post("/api/compare")
def compare(req:CompareRequest):
 try:return {"scenarios":[scenarios.run(x.name,{i.variable:i.value for i in x.interventions}) for x in req.scenarios],"baseline":engine.simulate()}
 except ValueError as e:raise HTTPException(422,str(e))
@app.get("/api/analytics")
def stats():return analytics.summarize(engine.compare({}))