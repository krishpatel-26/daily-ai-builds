"""Explainable role-fit and skill-gap calculations."""
from .roles import requirements_for

def analyze_gaps(skills, role):
    present = {s.lower() for s in skills}
    requirements = requirements_for(role)
    rows = []
    for skill, weight in requirements.items():
        matched = skill.lower() in present
        rows.append({"skill":skill,"weight":weight,"status":"present" if matched else "gap",
                     "priority": "high" if weight >= 4 and not matched else ("medium" if not matched else "covered")})
    total = sum(requirements.values()) or 1
    earned = sum(weight for skill, weight in requirements.items() if skill.lower() in present)
    return {"role":role,"readiness_score":round(earned/total*100),"matched_count":sum(x["status"]=="present" for x in rows),
            "required_count":len(rows),"gaps":sorted(rows,key=lambda x:(x["status"]=="present",-x["weight"],x["skill"]))}
