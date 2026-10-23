# Acceptance criteria

- [ ] App loads from the local server at port 4173.
- [ ] Load sample fills logs/config and starts an analysis.
- [ ] A 401 sample produces AUTH-401 with critical severity.
- [ ] A 429 sample produces RATE-429 and suggests honoring Retry-After.
- [ ] HTTP base URL, disabled webhook signature verification and disabled TLS checks appear as findings.
- [ ] Secret-like text is masked in the findings and redaction preview.
- [ ] Invalid config JSON blocks analysis and shows an actionable message.
- [ ] Severity filters change the visible finding list.
- [ ] JSON and Markdown exports download and contain redacted evidence.
- [ ] Clear inputs resets the UI and disables exports.
- [ ] Layout remains usable on narrow screens.
- [ ] npm run check and npm test pass.

These criteria are not evidence of a validated customer deployment.