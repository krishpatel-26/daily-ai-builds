# HTTP 429 quota incident runbook

## 1. Gather evidence
Record request ID, route, authenticated client/credential scope, timestamp, limit, remaining quota and provider request/trace IDs. Preserve relevant response headers without exposing secrets.

## 2. Confirm the scope
Determine whether the quota applies per token, account, project, endpoint, IP, or a shared service tier. Check whether parallel instances share an atomic counter.

## 3. Respond safely
- If the provider sends a valid Retry-After, honor it.
- Otherwise use bounded exponential backoff with jitter; avoid tight loops.
- Use a retry budget and circuit-break noisy clients when appropriate.
- Do not assume a 429 means the original operation had no side effect; verify the provider contract.
- Separate quota pressure from 5xx outages and authentication failures.

## 4. Escalate and hand off
Include a representative timeline, policy configuration, retry amplification risk, affected customers, mitigation, owner and next update. Redact tokens and personal data.

## Demo limitation
This workbench replays synthetic events locally. Its algorithm output and headers are simulated; they do not replace actual provider headers, documentation or service telemetry.
