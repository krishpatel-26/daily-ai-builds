"""Dashboard aggregation."""
from . import repository
from .services import analyze_profile

def dashboard_data():
    profile=repository.get_profile()
    analysis=analyze_profile(profile)
    apps=repository.list_applications()
    roadmap=repository.list_roadmap()
    done=sum(x["status"]=="done" for x in roadmap)
    return {
      "profile":profile,
      "readiness_score":analysis["analysis"]["readiness_score"],
      "matched_skills":analysis["analysis"]["matched_count"],
      "required_skills":analysis["analysis"]["required_count"],
      "roadmap":{"total":len(roadmap),"done":done,"in_progress":sum(x["status"]=="in_progress" for x in roadmap)},
      "applications":{"total":len(apps),"interviews":sum(x["stage"]=="Interview" for x in apps),"offers":sum(x["stage"]=="Offer" for x in apps)},
      "top_gaps":[x for x in analysis["analysis"]["gaps"] if x["status"]=="gap"][:5]
    }
