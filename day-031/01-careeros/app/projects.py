"""Portfolio project suggestions mapped to missing skills."""
PROJECTS = [
 {"title":"Production RAG Evaluation Workbench","skills":["RAG","Python","Statistics","Testing"],"level":"Advanced","deliverable":"Benchmark suite with retrieval metrics, regression gates, and reproducible reports."},
 {"title":"Real-Time Vision Quality Inspector","skills":["Computer Vision","Python","Machine Learning"],"level":"Advanced","deliverable":"Annotated dataset, detection pipeline, evaluation report, and operator dashboard."},
 {"title":"ML Model Monitoring Service","skills":["MLOps","Docker","SQL","Testing"],"level":"Advanced","deliverable":"Drift checks, model metrics, alert rules, and deployment runbook."},
 {"title":"Typed API with Role-Based Access","skills":["FastAPI","SQL","System Design","Testing"],"level":"Intermediate","deliverable":"Documented API, migrations, RBAC tests, and audit trail."},
 {"title":"Data Quality Investigation Pipeline","skills":["Data Analysis","Python","Statistics","SQL"],"level":"Intermediate","deliverable":"Data profiling, anomaly detection, validation rules, and findings."},
 {"title":"ROS 2 Autonomous Navigation Demo","skills":["ROS 2","C++","Computer Vision"],"level":"Advanced","deliverable":"Simulation, navigation stack, sensor logs, and benchmark video."},
 {"title":"Frontend Analytics Console","skills":["React","SQL","Communication"],"level":"Intermediate","deliverable":"Accessible dashboard with filters, loading states, and API integration."}
]

def recommend_projects(missing_skills):
    missing = {s.lower() for s in missing_skills}
    ranked = []
    for project in PROJECTS:
        overlap = [s for s in project["skills"] if s.lower() in missing]
        if overlap:
            ranked.append({**project,"skill_coverage":len(overlap),"matched_gaps":overlap})
    return sorted(ranked,key=lambda p:(-p["skill_coverage"],p["title"]))[:5]
