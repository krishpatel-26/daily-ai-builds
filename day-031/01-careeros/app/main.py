"""CareerOS FastAPI application."""
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .database import initialize
from .schemas import ProfileInput, ResumeInput, AnalyzeInput, RoadmapUpdate, ApplicationInput, ApplicationUpdate
from . import repository
from .services import analyze_profile, generate_and_save_roadmap
from .dashboard import dashboard_data

ROOT=Path(__file__).resolve().parent.parent
app=FastAPI(title="CareerOS API",version="1.0.0",description="Human-in-the-loop career intelligence and execution platform")

@app.on_event("startup")
def startup():
    initialize()

@app.get("/",response_class=HTMLResponse)
def home():
    return (ROOT/"web"/"index.html").read_text(encoding="utf-8")

app.mount("/static",StaticFiles(directory=ROOT/"web"),name="static")

@app.get("/api/health")
def health():
    return {"status":"ok","service":"CareerOS"}

@app.get("/api/profile")
def get_profile():
    return repository.get_profile()

@app.post("/api/profile")
def save_profile(payload:ProfileInput):
    return repository.save_profile(payload.model_dump())

@app.post("/api/profile/resume")
def upload_resume(payload:ResumeInput):
    profile=repository.get_profile()
    profile["resume_text"]=payload.text
    profile["skills"]=sorted(set(profile.get("skills",[])))
    return repository.save_profile(profile)

@app.post("/api/analyze")
def analyze(payload:AnalyzeInput):
    profile=repository.get_profile()
    return analyze_profile(profile,payload.target_role)

@app.get("/api/roadmap")
def get_roadmap():
    return repository.list_roadmap()

@app.post("/api/roadmap")
def create_roadmap(payload:AnalyzeInput):
    return generate_and_save_roadmap(repository.get_profile(),payload.target_role)

@app.patch("/api/roadmap/{item_id}")
def update_roadmap(item_id:int,payload:RoadmapUpdate):
    result=repository.update_roadmap(item_id,payload.status)
    if result is None: raise HTTPException(404,"Roadmap item not found")
    return result

@app.get("/api/applications")
def get_applications():
    return repository.list_applications()

@app.post("/api/applications")
def create_application(payload:ApplicationInput):
    return repository.add_application(payload.model_dump())

@app.patch("/api/applications/{application_id}")
def patch_application(application_id:int,payload:ApplicationUpdate):
    result=repository.update_application(application_id,payload.model_dump())
    if result is None: raise HTTPException(404,"Application not found or no changes supplied")
    return result

@app.get("/api/dashboard")
def dashboard():
    return dashboard_data()
