from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from . import world,engine,rumours,analytics
from .schemas import SocialAction,RumourInput,TickInput
ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="SocialSim",version="1.0.0",description="Relationship-driven narrative simulation")
app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static")
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text()
@app.get("/api/state")
def state():return engine.status()
@app.post("/api/reset")
def reset():return world.reset()
@app.post("/api/actions")
def action(a:SocialAction):
 try:return engine.act(a)
 except ValueError as e:raise HTTPException(422,str(e))
@app.post("/api/rumours")
def rumour(r:RumourInput):
 try:return rumours.create(world.STATE,r)
 except ValueError as e:raise HTTPException(422,str(e))
@app.post("/api/tick")
def advance(t:TickInput):return {"ticks":engine.tick(t.steps),"state":engine.status()}
@app.get("/api/analytics")
def stats():return analytics.overview(world.STATE)
@app.get("/api/events")
def events():return world.STATE["events"][-100:]