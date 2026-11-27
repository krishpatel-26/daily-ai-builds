# Local API

GET `/api/report?seed=53&rounds=18` returns six experiment histories plus a five-seed fixed benchmark. Query values are bounded to seed 0..999999 and rounds 1..80. Returns JSON. The localhost-only service does not accept datasets, authenticate users or train on external records.
