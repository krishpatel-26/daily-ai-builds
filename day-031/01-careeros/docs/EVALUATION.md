# Evaluation Plan

## Current checks
- Unit tests for skill extraction, normalization, role scoring, project mapping, and roadmap generation.
- API smoke checks through FastAPI OpenAPI docs.
- Manual review of extracted evidence snippets.
- Boundary checks for empty profiles and unsupported roles.

## Risks
Keyword matching can miss synonyms or infer context incorrectly. Role weights are heuristics, not validated labor-market data. Readiness is weighted coverage, not employment probability.

## Next experiments
1. Build a consented and redacted labeled resume-to-skill dataset.
2. Measure precision and recall per skill.
3. Compare keyword extraction with embedding and LLM extraction.
4. Evaluate recommendations with career coaches and candidates.
5. Measure learning and application outcomes without implying causation.