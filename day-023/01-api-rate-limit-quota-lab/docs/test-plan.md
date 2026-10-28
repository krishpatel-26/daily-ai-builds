# Test plan

## Deterministic unit coverage
- Normalize route paths, clients and request identifiers.
- Check fixed-window aligned resets and sliding-window boundary retention.
- Verify token-bucket burst capacity and timed refill.
- Ensure counters are isolated across client/route keys.
- Verify replay preserves original display ordering while evaluating timestamp order.
- Cover HTTP 429 retry-after formatting and HTTP-date parsing.
- Validate policy bounds and rejected algorithm names.
- Confirm reports contain disclaimers and correctly escape Markdown table separators.

## Manual browser checks
1. Load the dashboard with default scenario.
2. Switch each scenario and re-run the comparison.
3. Change limit and window values; try 0, negative and out-of-range values.
4. Filter allowed vs rate-limited requests and search by client or ID.
5. Select a request and inspect all three algorithm outcomes.
6. Export Markdown and JSON reports and confirm output is labelled synthetic.

## Non-goals
No live provider integration, distributed concurrency testing, browser automation, load test, or security certification is implied by this test plan.
