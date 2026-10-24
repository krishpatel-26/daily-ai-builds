# Evidence model

A useful evidence note lets another engineer repeat or challenge the observation.

For technical checks, include as appropriate:
- timestamp and timezone
- environment and build/API version
- request/correlation ID
- expected outcome and observed outcome
- sanitized command/fixture name or test reference
- who ran the check and where it ran
- link or ticket reference without credentials

## Evidence states
- To do: not tested or no result yet
- Pass: observed expected behavior; evidence should be attached
- Fail: expected behavior was not observed; record a reproduction and stop condition
- N/A: documented rationale exists elsewhere; avoid using N/A to hide an incomplete test

The prototype stores free-text evidence locally. It doesn't verify artifacts or independently confirm the evidence is genuine. Review exports before sharing.