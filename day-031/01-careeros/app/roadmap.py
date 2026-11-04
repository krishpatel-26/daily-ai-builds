"""Convert prioritized skill gaps into an actionable learning roadmap."""
ROADMAP_LIBRARY = {
 "Python":("Python engineering foundations","Build tested modules, type hints, packaging, and error handling.","2 weeks"),
 "Machine Learning":("Applied machine learning","Train baseline models, validate splits, tune models, and document error analysis.","3 weeks"),
 "Deep Learning":("Deep learning practice","Implement a small neural network and compare training curves and evaluation metrics.","3 weeks"),
 "LLM Engineering":("LLM application engineering","Build structured-output workflows, tool calls, evaluation, and failure handling.","2 weeks"),
 "RAG":("Retrieval-augmented generation","Build ingestion, chunking, retrieval evaluation, citations, and regression tests.","2 weeks"),
 "SQL":("SQL and data modelling","Design normalized schemas, indexes, joins, transactions, and query tests.","2 weeks"),
 "Docker":("Containerized delivery","Package an API with Docker, health checks, configuration, and reproducible startup.","1 week"),
 "Testing":("Testing discipline","Write unit, integration, and boundary tests with coverage of failure paths.","1 week"),
 "Statistics":("Statistics for AI evaluation","Practice confidence intervals, hypothesis tests, sampling, and effect sizes.","2 weeks"),
 "MLOps":("Model operations","Track experiments, package models, monitor drift, and design rollback procedures.","3 weeks"),
 "System Design":("System design fundamentals","Document APIs, data flows, bottlenecks, failure modes, and scaling trade-offs.","2 weeks"),
 "React":("React application engineering","Build reusable components, controlled forms, API states, and accessible interactions.","2 weeks"),
 "FastAPI":("FastAPI service development","Build validated endpoints, dependency injection, persistence, and OpenAPI docs.","1 week"),
 "ROS 2":("ROS 2 systems","Build nodes, topics, services, launch files, and simulation-based tests.","3 weeks"),
 "C++":("Modern C++","Practice RAII, STL, concurrency basics, and tested components.","3 weeks"),
 "Computer Vision":("Computer vision pipeline","Build image preprocessing, inference, metrics, and failure-case analysis.","3 weeks"),
 "Cloud":("Cloud deployment basics","Deploy a containerized service with secrets, logs, health checks, and cost limits.","2 weeks"),
 "Git":("Professional Git workflow","Practice branches, reviewable commits, rebasing, and release tags.","1 week"),
 "Communication":("Technical communication","Write a design note, demo script, and concise project decision log.","1 week"),
 "Data Analysis":("Data analysis workflow","Use pandas, exploratory analysis, data validation, and clear visual summaries.","2 weeks")
}

def build_roadmap(gaps):
    items=[]
    for skill in gaps:
        title,description,duration=ROADMAP_LIBRARY.get(skill,(f"Develop {skill}",f"Complete a practical exercise and publish evidence demonstrating {skill}.","2 weeks"))
        items.append({"title":title,"category":"Skill development","description":description,"skill":skill,"duration":duration})
    return items
