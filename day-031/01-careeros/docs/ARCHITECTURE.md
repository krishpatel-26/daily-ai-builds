# Architecture

Browser (vanilla JS) → FastAPI REST API → Pydantic validation → Career intelligence orchestration → skill extraction / role-gap analysis / project and roadmap recommendation → repository abstraction → SQLite.

The optional OpenAI-compatible provider is isolated from deterministic scoring. It must not silently alter readiness scores.

The current local prototype is single-user and unauthenticated. Do not expose it publicly with personal data.