# Local API

`GET /api/report?policy=diversified&seed=50&days=70&disrupted=true`

Policies: lean, diversified, resilient. Seed 0..100000, days 1..365. Returns one trajectory, daily events, KPIs, ten-seed policy comparisons and Pareto alternatives. Invalid values return HTTP 400. There are no mutation endpoints and no persistence.
