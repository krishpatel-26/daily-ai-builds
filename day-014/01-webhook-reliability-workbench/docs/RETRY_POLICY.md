# Retry policy

## Suggested production baseline
- Retry network timeouts, connection resets, and selected 5xx responses.
- Treat most 4xx responses as non-retryable until the payload or authorization problem is corrected; 408 and 429 may need special handling.
- Use exponential backoff with jitter and a bounded maximum attempt count.
- Respect Retry-After when the receiver provides it.
- Record every attempt and stop retrying once the event expires or is manually cancelled.
- Route exhausted events to a dead-letter queue with an owner and reason.

## Example schedule
Illustrative delays: 1s, 2s, 4s, 8s plus jitter, capped at a configured maximum. Tune this to the integration's latency and receiver capacity.

## Prototype limitation
The app simulates outcomes; it does not wait, schedule jobs, or execute network retries. The displayed history is not a record of real requests.