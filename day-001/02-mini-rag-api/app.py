from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI(title="Mini RAG API")
documents: list[str] = []

class Document(BaseModel):
    text: str

def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-zA-Z0-9]+", text.lower()))

def retrieve(query: str, k: int = 3) -> list[str]:
    q = tokenize(query)
    scored = [(len(q & tokenize(doc)), doc) for doc in documents]
    return [doc for score, doc in sorted(scored, reverse=True)[:k] if score > 0]

@app.post("/documents")
def add_document(doc: Document):
    documents.append(doc.text)
    return {"stored": True, "total_documents": len(documents)}

@app.get("/ask")
def ask(q: str):
    context = retrieve(q)
    return {
        "query": q,
        "retrieved_context": context,
        "answer": (
            "No matching context was found."
            if not context
            else "Grounded answer should be generated from the retrieved context."
        ),
    }
