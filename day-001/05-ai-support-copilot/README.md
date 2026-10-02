# AI Support Copilot

A production-style support-ticket copilot combining routing, retrieval, structured response generation, and an API boundary.

## Architecture

POST /tickets -> validation -> intent router -> knowledge retrieval -> response planner -> JSON result

The default implementation is deterministic so it runs without paid model APIs. Components are separated so an LLM provider, vector database, or queue can be plugged in later.

## Features

- Typed request/response schemas
- Specialist routing
- Knowledge-base retrieval
- Confidence scoring
- Suggested response and escalation decision
- Health endpoint
- Unit tests
- Environment-based configuration
- Structured logging

## Run

python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --reload

Open /docs for interactive API documentation.

This project intentionally does not commit credentials or external API keys.
