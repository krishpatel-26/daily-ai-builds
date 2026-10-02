# Mini RAG API

A minimal retrieval-augmented generation backend.

## Flow

Documents → chunking → keyword retrieval → context → answer

This version is dependency-light and deterministic. The retrieval layer can later be replaced with embeddings/vector search and the answer layer with an LLM.

## Run

```bash
pip install fastapi uvicorn
uvicorn app:app --reload
```

POST text to `/documents`, then query `/ask?q=...`.
