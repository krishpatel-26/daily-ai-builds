# Local API

GET `/api/report?seed=53&step=20` returns scenario metadata, synthetic close approaches, illustrative candidate impulses, and ten-seed benchmark. Valid seeds 0..999999; time steps 1..120 seconds. The service is read-only and binds to localhost at port 4211. No controls or live telemetry interfaces are provided.
