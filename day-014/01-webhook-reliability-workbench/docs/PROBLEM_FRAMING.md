# Problem framing

## Primary user
A forward-deployed engineer, solutions engineer, integration engineer, or customer-facing platform developer diagnosing a webhook integration.

## Job to be done
Answer four questions quickly:
1. What event was sent?
2. Was its payload structurally valid?
3. What happened during delivery attempts?
4. What is the safest next step?

## Common failure patterns
- Required fields are absent or use an unexpected type.
- The receiving endpoint returns a transient 5xx error.
- The receiver rejects a valid JSON body because the business schema differs.
- Retry creates duplicate downstream side effects.
- Event logs lack a clear owner or next action.

## Design principles
- Evidence before assumptions.
- Validation errors should be specific.
- Retries must be bounded and visible.
- Idempotency belongs at the receiver as well as the sender.
- The tool must make it clear when a result is simulated.
- Customer-facing updates should not claim an unverified fix.