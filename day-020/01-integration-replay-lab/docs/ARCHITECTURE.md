# Architecture

The application has three layers:
- index.html and styles.css: local-first UI
- src/core.js: scenario validation, deterministic mock runner, assertion evaluation, redaction and export generation; usable from a browser or CommonJS
- scripts/serve.js: dependency-free static server bound to 127.0.0.1

## Replay flow
1. Parse a JSON scenario pack and validate each case.
2. Read the case's declared mockResponse; do not open a network connection.
3. Evaluate the configured status, JSON-path, header, latency-budget and value assertions.
4. Produce per-assertion expected/observed evidence and a run summary.
5. Generate a redacted incident handoff, a standalone Node.js test draft or a JSON scenario pack.

The latencyMs value is simulated metadata. The runner does not sleep or measure actual network time. All customer integrations and environments are external to this tool.