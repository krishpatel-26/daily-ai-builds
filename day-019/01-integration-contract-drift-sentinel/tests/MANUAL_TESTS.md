# Manual acceptance and demo validation

Run from the project root:

    npm run check
    npm test
    npm start

Then open http://127.0.0.1:4173 in a current desktop browser.

## Required browser checks
1. Click Load sample contracts. Confirm both version editors populate and the analysis shows BREAKING CHANGES.
2. Confirm the removed GET operation appears as a critical breaking item.
3. Confirm the new region requirement, newly required X-Region parameter, Idempotency-Key header and closed-schema behavior appear in findings.
4. Filter Breaking, Additive and Review; verify each filter changes the list.
5. Leave the baseline sample payload selected against Proposed V2. Validate it and verify the missing region and unknown legacy_code are reported.
6. Change the payload target to Current V1. Verify the same payload passes the supported subset.
7. Replace the payload with the included V2-valid fixture. Verify it passes the supported subset.
8. Paste invalid JSON into either contract editor and press Analyze. Verify a readable error appears, with no uncaught page exception.
9. Export the Markdown review, regression-test plan JSON and full analysis JSON. Open each export and verify current counts and test ideas are included.
10. Try a contract with no changes and confirm the tool reports no changes by supported rules.
11. Resize the viewport below 620 px and verify controls remain accessible.
12. Check the browser Network panel: analysis should not call external customer endpoints or send contract text to a backend.

## Security and accuracy reminder
Use synthetic examples. This app performs a documented subset comparison, not complete OpenAPI/JSON Schema validation. A passing sample payload does not guarantee a live request will pass. The generated test plan has not been executed against an API unless the engineer separately runs it and records the results.