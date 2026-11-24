# Local API

`GET /api/scenario?strategy=baseline&failed_line=L05` — a network representation plus simulated outcomes. Strategies: baseline, backup, reinforce, combined. Omit `failed_line` for intact topology. Invalid parameters return HTTP 400.

`GET /api/compare` — aggregate metrics for four strategies over 12 single-line outages each.

No write endpoints. No authorization or deployment hardening; localhost only.
