# Reproducibility checklist

To reproduce a real LLM evaluation, preserve:
- Exact dataset version and case IDs
- Full prompt template and hash
- Provider, model identifier, and model version when available
- Temperature, max tokens, and other generation parameters
- Retrieval settings and source snapshot
- Tool schemas and mock/external mode
- Evaluator versions and thresholds
- Start/end time, latency, token counts, and errors

LLM output can be nondeterministic even with a fixed prompt. Repeat trials when variance matters and distinguish the raw response from the evaluator's verdict.