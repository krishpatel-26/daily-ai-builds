# Integration error taxonomy

| Class | Typical signals | First validation |
|---|---|---|
| Identity | 401, expired token | token expiry, audience, issuer |
| Authorization | 403, insufficient scope | role/scope mapping |
| Throttling | 429, Retry-After | quota, backoff and concurrency |
| Upstream | 500/502/503/504 | request IDs, upstream health |
| Network | DNS errors, refused connection | name resolution, VPN, firewall |
| Timeout | deadline exceeded | latency distribution, connect/read timeout |
| Contract | 400/422, missing field | API version and request schema |
| Browser | CORS/preflight | calling origin and preflight headers |
| TLS | cert or handshake error | certificate chain and trust store |
| Webhook trust | invalid signature | raw-body verification and timestamp |

This catalog is not exhaustive. Provider-specific codes and response bodies may require additional rules.