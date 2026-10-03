# LLM Gateway with Routing, Budgets and Guardrails

Provider-agnostic AI gateway separating policy, routing, provider execution and usage accounting. Includes deterministic local providers so it runs without an API key.

Run: pip install -r requirements.txt && uvicorn app.main:app --reload
Tests: pytest -q