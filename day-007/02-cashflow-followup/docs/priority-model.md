# Priority model

The queue is sorted with a deterministic, explainable score:

- Every overdue day adds 100 points.
- Amount contributes up to 999 points (amount / 100, capped).
- An invoice due within seven days gets a 50-point boost.
- Paid invoices sort below unpaid invoices.

This is a heuristic for queue ordering, not a prediction of payment likelihood or credit risk. It should be validated with users and made configurable if it does not match real collection workflows. No model is trained and no external AI service is called.
