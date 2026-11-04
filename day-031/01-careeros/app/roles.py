"""Role requirement catalogue with transparent skill weights."""
ROLE_CATALOG = {
 "AI Engineer": {"Python":5,"Machine Learning":5,"Deep Learning":4,"LLM Engineering":5,"RAG":4,"SQL":3,"Git":2,"Docker":3,"Testing":3,"Statistics":3,"MLOps":3,"System Design":2},
 "Data Scientist": {"Python":5,"SQL":4,"Machine Learning":5,"Statistics":5,"Data Analysis":5,"Deep Learning":2,"Git":2,"Communication":3},
 "ML Engineer": {"Python":5,"Machine Learning":5,"Deep Learning":4,"MLOps":5,"Docker":4,"Cloud":3,"SQL":3,"Testing":4,"System Design":3},
 "Robotics Software Engineer": {"Python":4,"C++":5,"ROS 2":5,"Computer Vision":4,"Machine Learning":3,"Git":3,"Docker":2,"System Design":3},
 "Backend Engineer": {"Python":4,"SQL":5,"FastAPI":4,"Docker":4,"Cloud":3,"Git":3,"Testing":5,"System Design":5,"Communication":2},
 "Full Stack Developer": {"React":5,"Python":3,"FastAPI":3,"SQL":4,"Git":3,"Docker":2,"Testing":3,"Communication":2}
}

def requirements_for(role):
    if role in ROLE_CATALOG:
        return ROLE_CATALOG[role]
    return ROLE_CATALOG["AI Engineer"]
