from pathlib import Path
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .database import init_db
from .seed import seed
from .schemas import EventInput,RecallRequest,RelationshipInput,FactInput
from . import characters,events,memory,relationships,facts,continuity,analytics
ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="MythosGraph",version="1.0.0",description="Persistent character memory and narrative continuity for AI game worlds.")
app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static")
@app.on_event("startup")
def startup():init_db();seed()
@app.get("/",response_class=HTMLResponse)
def home():return (ROOT/"web"/"index.html").read_text()
@app.get("/api/characters")
def get_characters():return characters.list_characters()
@app.get("/api/timeline")
def get_timeline(limit:int=50):return events.timeline(max(1,min(limit,200)))
@app.post("/api/events")
def post_event(e:EventInput):
 try:return events.record_event(e)
 except Exception as exc:raise HTTPException(409,"Could not record event; check duplicate ID and character references.") from exc
@app.post("/api/memory/recall")
def post_recall(r:RecallRequest):
 if not characters.get_character(r.character_id):raise HTTPException(404,"Character not found")
 return {"character":characters.get_character(r.character_id),"memories":memory.recall(r.character_id,r.query,r.limit)}
@app.get("/api/relationships")
def get_relationships():return relationships.all_relationships()
@app.post("/api/relationships")
def post_relationship(r:RelationshipInput):return relationships.update(r.source_id,r.target_id,r.delta,r.reason)
@app.get("/api/facts")
def get_facts():return facts.all_facts()
@app.post("/api/facts")
def post_fact(f:FactInput):return facts.add(f)
@app.get("/api/continuity/check")
def check(subject:str,predicate:str,obj:str):return continuity.check(subject,predicate,obj)
@app.get("/api/context/{cid}")
def get_context(cid:str,query:str):
 if not characters.get_character(cid):raise HTTPException(404,"Character not found")
 return continuity.context(cid,query)
@app.get("/api/analytics")
def get_analytics():return analytics.overview()