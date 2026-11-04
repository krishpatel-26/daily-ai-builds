"""Evidence-oriented skill extraction using a transparent local taxonomy."""
import re

TAXONOMY = {
 "Python":["python"], "SQL":["sql","sqlite","postgresql","mysql"], "Machine Learning":["machine learning","scikit-learn","sklearn"],
 "Deep Learning":["deep learning","pytorch","tensorflow"], "LLM Engineering":["llm","large language model","langchain","llamaindex"],
 "RAG":["rag","retrieval augmented generation","vector database","embeddings"], "Computer Vision":["opencv","yolo","computer vision"],
 "Cloud":["aws","azure","gcp","cloud"], "Docker":["docker","containerization"], "Git":["git","github"],
 "React":["react","vite","typescript"], "FastAPI":["fastapi"], "Data Analysis":["pandas","numpy","data analysis"],
 "ROS 2":["ros2","ros 2","robot operating system"], "C++":["c++","cpp"], "Communication":["stakeholder","presentation","communication"],
 "Testing":["pytest","unit testing","testing","test automation"], "Statistics":["statistics","hypothesis testing","regression"],
 "MLOps":["mlops","model monitoring","model deployment"], "System Design":["system design","distributed systems","microservices"]
}

def extract_skills(text: str):
    source = text.lower()
    found = []
    for skill, aliases in TAXONOMY.items():
        matches = [a for a in aliases if re.search(r"(?<![a-z0-9])" + re.escape(a) + r"(?![a-z0-9])", source)]
        if matches:
            alias = max(matches, key=len)
            pos = source.find(alias)
            snippet = text[max(0,pos-65):min(len(text),pos+len(alias)+90)].replace("\n"," ")
            found.append({"skill":skill,"evidence":snippet.strip(),"confidence":"keyword evidence","verified":False})
    return sorted(found, key=lambda x:x["skill"])

def normalize_skills(values):
    return sorted({str(v).strip() for v in values if str(v).strip()})
