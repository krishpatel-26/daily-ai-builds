# Agent Task Router

A lightweight multi-agent pattern that classifies an incoming request and routes it to a specialist.

## Flow

Request → Router → Specialist Agent → Structured Response

The starter uses deterministic routing so it runs without an API key. Replace the specialist functions with LLM calls later.

## Run

```bash
python agent_router.py
```
