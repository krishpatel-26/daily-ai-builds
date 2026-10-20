# Test plan

## Unit tests to add
- Valid event envelope is accepted.
- Missing required field is rejected with a useful message.
- Invalid timestamp and non-object data are rejected.
- Duplicate event IDs are identified.
- Retry count is bounded.
- Retry behavior differs for transient and non-retryable failures.
- Exported logs are valid JSON and preserve event history.

## Integration tests for a future receiver
- Receiver returns 2xx and sender records success.
- Receiver returns 400 and event is not retried blindly.
- Receiver returns 429 with Retry-After.
- Receiver returns 500 then recovers.
- Duplicate delivery causes one downstream side effect.
- Signature mismatch and stale timestamp are rejected.
- Timeout after receiver commit does not duplicate the business action.

## Current status
A manual checklist is included in tests/manual-test-cases.md. Automated tests and real receiver integration have not been implemented.