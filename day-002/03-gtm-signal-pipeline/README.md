# GTM Signal Pipeline

Event-driven lead scoring service that converts company, role, and product-intent signals into a prioritized sales queue.

Run: pip install -r requirements.txt && uvicorn app.main:app --reload

POST /v1/signals and GET /v1/leads/{lead_id}. Tests: pytest -q