# Day 025 — API Security Posture Checker

A local-first static review tool for OpenAPI JSON. It highlights possible missing authentication declarations, operation-level security overrides, plain HTTP server URLs, and credential-like response fields.

## Run
Requires Node.js 20+.

```bash
npm test
npm run check
npm start
```

Open http://127.0.0.1:4175 and load the sample OpenAPI document.

## API
- `GET /api/health`
- `POST /api/scan` with JSON body `{ "spec": { ...OpenAPI JSON... } }`

## Limitations
Static heuristic checks only; no target traffic is sent. Findings may be false positives and cannot prove security or compliance. Review results and use authorized dynamic tests. Server binds to loopback and limits request bodies to 2 MB.

MIT License.
