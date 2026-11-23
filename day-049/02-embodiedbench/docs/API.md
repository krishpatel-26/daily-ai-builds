# API contract
`GET /api/report?policy=nearest&fault=true&limit=200` returns the main scenario, snapshots, event logs and a four-condition planner comparison. Policies: nearest or ordered. Fault flag: true or false. Limit: 1–1000 simulated ticks. Unknown policies or invalid horizons return HTTP 400. `GET /` serves the animated replay UI. No write endpoints or physical robot connectors exist.
