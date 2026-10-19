# Regression policy

Before releasing a prompt, model, retrieval, or tool change:

1. Run the same versioned evaluation dataset.
2. Compare overall and category-level results against the baseline.
3. Inspect every new failure and every high-severity review.
4. Check latency, token use, and tool-error rates.
5. Record accepted regressions and the accountable approver.
6. Preserve the evaluated prompt and configuration for reproducibility.

Example release gate: no newly introduced high-severity failure, no schema-validity regression, and no latency increase above an explicitly agreed budget. Thresholds must be defined for the application; this prototype does not enforce production release gates.