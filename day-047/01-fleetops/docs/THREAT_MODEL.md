# Threat model
The local read-only HTTP service binds to loopback, with no authentication and no production telemetry. Production requires input limits, access controls, TLS, authorization, audit logs and operational network isolation.
