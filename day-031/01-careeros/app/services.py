"""Career intelligence orchestration."""
from .skills import extract_skills, normalize_skills
from .gap_analysis import analyze_gaps
from .projects import recommend_projects
from .roadmap import build_roadmap
from . import repository

def analyze_profile(profile, target_role=None):
    role = target_role or profile.get("target_role") or "AI Engineer"
    evidence = extract_skills(profile.get("resume_text",""))
    detected = [x["skill"] for x in evidence]
    skills = normalize_skills(profile.get("skills",[]) + detected)
    gaps = analyze_gaps(skills,role)
    missing = [x["skill"] for x in gaps["gaps"] if x["status"]=="gap"]
    projects = recommend_projects(missing)
    roadmap = build_roadmap(missing)
    return {"target_role":role,"skills":skills,"skill_evidence":evidence,"analysis":gaps,
            "recommended_projects":projects,"roadmap_preview":roadmap,
            "disclaimer":"Skills are inferred from supplied text or manually entered. Review evidence; this score is a planning heuristic, not a hiring probability."}

def generate_and_save_roadmap(profile, target_role=None):
    result=analyze_profile(profile,target_role)
    saved=repository.replace_roadmap(result["roadmap_preview"])
    return {"items":saved,"count":len(saved),"target_role":result["target_role"]}
