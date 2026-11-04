# CareerOS — Autonomous Career Intelligence Platform

**Day 031 / Daily AI Builds · 30 meaningful GitHub commits**

CareerOS turns a career goal into an evidence-backed execution plan. It parses a resume, extracts skills, compares a target role, identifies gaps, creates a learning roadmap, recommends portfolio projects, and tracks applications and progress.

This is a human-in-the-loop career operating system. It does not guarantee employment, fabricate experience, submit applications automatically, or claim that inferred skills are verified.

## Features
- Resume text ingestion (paste text or upload a .txt file in the UI).
- Skill extraction with evidence snippets and confidence labels.
- Role requirement matching and explainable skill-gap analysis.
- Adaptive learning roadmap with milestones and completion tracking.
- Portfolio project recommendations mapped to missing skills.
- Job application pipeline with stage, dates, notes, and follow-up reminders.
- Career dashboard with readiness score and progress metrics.
- Optional LLM provider integration via OpenAI-compatible API; deterministic local mode works without an API key.
- SQLite persistence, input validation, REST API, and tests.

## Run locally
Python 3.10+.

```bash
cd day-031/01-careeros
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000.

## Optional LLM mode
Set `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_MODEL` in your environment. CareerOS uses an OpenAI-compatible chat-completions endpoint for optional narrative refinement. Never commit secrets. The deterministic engine remains available if no provider is configured.

## API overview
- `GET /api/health`
- `GET/POST /api/profile`
- `POST /api/profile/resume`
- `POST /api/analyze`
- `GET/POST /api/roadmap`
- `PATCH /api/roadmap/{item_id}`
- `GET/POST /api/applications`
- `PATCH /api/applications/{application_id}`
- `GET /api/dashboard`

Interactive API docs: http://127.0.0.1:8000/docs

## Architecture
FastAPI API layer → service orchestration → deterministic skill/role intelligence → SQLite repository. A static responsive client consumes the REST API. Optional LLM calls are isolated behind a provider adapter.

## Responsible-use boundaries
CareerOS provides planning support, not hiring decisions. Skill extraction is heuristic and can miss context. Review every inferred skill and every generated recommendation. Do not upload confidential employer documents or personal data without permission. Application tracking is user-controlled; no credentials are collected.

## Roadmap
Add authenticated multi-user workspaces, document parsing for PDF/DOCX, labor-market connectors, semantic skill ontology, calibrated assessment tasks, and user-consented integrations.
