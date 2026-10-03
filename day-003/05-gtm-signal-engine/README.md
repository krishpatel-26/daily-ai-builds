# GTM Signal Engine

A production-style GTM engineering service that converts account activity into explainable sales signals. It combines weighted intent events, account fit, freshness decay and deduplication, then exposes ranked signals through FastAPI.

## Example
A target account viewed pricing twice, opened an integration page and matches the ICP. The engine turns those events into a ranked signal with reasons and a recommended next action.

## Run
pip install -r requirements.txt
uvicorn app.main:app --reload

Tests: pytest -q
No external APIs or credentials are required.