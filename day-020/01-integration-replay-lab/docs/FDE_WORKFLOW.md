# FDE reproduction workflow

1. Confirm the affected operation, environment, approximate UTC timestamp and correlation/request ID.
2. Request the smallest sanitized request and response evidence that distinguishes the symptom.
3. Remove authorization headers, cookies, emails and customer-specific fields before saving.
4. Convert the observed request into a scenario, record the expected outcome and encode the observed behavior in mockResponse.
5. Add assertions for status, required response fields, headers and important value invariants.
6. Run the scenario locally and identify the first failing assertion.
7. Compare the repro with API documentation, contract version and a controlled non-production test.
8. Make the smallest change that addresses the verified cause.
9. Export the test draft; review its quality and run it against a proper test harness.
10. Record owner, regression result, residual risk and customer communication in the team's system.

The scenario captures a reproducible hypothesis. Confirm against actual test evidence before claiming root cause or closure.