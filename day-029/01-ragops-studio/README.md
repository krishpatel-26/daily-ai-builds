# RAGOps Studio — Day 029/365

A local RAG evaluation workbench for retrieval ranking, benchmark diagnostics, heuristic groundedness, and regression gates.

## Features
- Seeded knowledge base and benchmark dataset
- Configurable overlapping chunking and BM25 retrieval
- Precision@5, Recall@5, MRR, nDCG@5
- Lexical groundedness diagnostic
- Configurable quality regression thresholds
- Per-question diagnostics and saved in-memory run history
- REST API for evaluation and run comparison

## Run
Requires Node.js 20+. No third-party dependencies.

```bash
npm test
npm run check
npm start
```

Open http://127.0.0.1:4180.

## API
- GET /api/health, /api/documents, /api/cases, /api/runs
- POST /api/cases
- POST /api/evaluate (topK, chunkSize, overlap, optional caseIds)
- GET /api/runs/:id
- GET /api/compare?a=RUN_ID&b=RUN_ID

## Methodology and limitations
BM25 is deterministic lexical retrieval, not embedding search. Groundedness uses lexical overlap and does not prove semantic entailment. The demo answer is based on benchmark answer text; this is not live LLM generation. Data is in memory and resets on restart. The benchmark is small and synthetic. No vector database, hosted model, reranker, authentication, or durable storage is connected.

## Production roadmap
Add dense retrieval and hybrid fusion, live model generation, human/model judging, versioned datasets, persistent multi-tenant storage, RBAC, audit logs, and CI deployment gates. See SECURITY.md.

**Daily AI Builds:** measure, investigate, improve.