# Day 024 — API Contract Drift Detector

A local-first prototype that compares two JSON API specifications, flags removed elements and type changes, summarizes risk, and exports a Markdown report.

## Run
Requires Node.js 20+.

```bash
npm test
npm run check
npm start
```

Open http://127.0.0.1:4174. Use the sample contracts preloaded in the dashboard.

## API
- `GET /api/health`
- `POST /api/compare` with JSON `{ "baseline": { ... }, "candidate": { ... } }`

## Features
- Structural JSON contract comparison
- JSON-pointer-style paths and severity labels
- Release review gate, evidence paths, Markdown report
- No third-party dependencies or API keys

## Limitations
This is a structural JSON diff prototype, not a full OpenAPI semantic validator. It does not resolve references, model request/response direction, or prove consumer compatibility. Review findings and run contract/integration tests. Server binds to loopback and rejects request bodies over 2 MB.

MIT License.
