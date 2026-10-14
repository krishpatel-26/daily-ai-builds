# Security review checklist

- [x] Render user-provided strings as escaped text in table cells.
- [x] Avoid transmitting invoice records to external services.
- [x] Require explicit confirmation before clearing all records.
- [x] Keep reminder sending manual.
- [ ] Add automated browser-level XSS tests.
- [ ] Review CSV formula injection for spreadsheets (prefix dangerous exported cells before shipping to business users).
- [ ] Add a stronger import size limit and malformed-row feedback.
- [ ] Consider Content Security Policy before production hosting.
- [ ] Conduct a dependency and browser compatibility review.
