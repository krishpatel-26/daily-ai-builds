# Acceptance criteria

- [ ] App loads from npm start at http://127.0.0.1:4173.
- [ ] Load sample contracts fills both editors and starts analysis.
- [ ] The sample reports a removed operation as a critical breaking change.
- [ ] Newly required parameter/property and removed property risks are surfaced.
- [ ] Additive changes are separated from breaking changes.
- [ ] Filtering changes shows only the selected classification.
- [ ] Baseline payload passes the supported V1 request schema rules.
- [ ] The same baseline payload fails V2 due to missing region and/or unknown legacy_code.
- [ ] A valid V2 payload passes the supported rules.
- [ ] Invalid JSON produces a clear error without crashing the page.
- [ ] Markdown report, regression plan JSON and analysis JSON export correctly.
- [ ] Core unit tests pass and syntax checks run successfully.
- [ ] Manual browser tests are performed before claiming release readiness.

This list is an acceptance plan; checked items require observed test results.