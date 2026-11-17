# Threat model

The demo binds to loopback and serves synthetic data. Before network exposure, add authentication, authorization, TLS, request limits, secure headers and audit controls. Do not send sensitive facility or robot identifiers to untrusted hosts.
