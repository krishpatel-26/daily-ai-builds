# Manual test plan

1. Run npm start and open http://localhost:4173.
2. Click Load sample case; verify readiness summary and prioritized findings appear.
3. Confirm AUTH-401 is critical; RATE-429 and TIMEOUT are present.
4. Confirm ENV-HTTP and ENV-WEBHOOK are found from sample config.
5. Inspect redaction preview and verify demo bearer/API key strings are masked.
6. Select Critical, High, Medium and Info filters and confirm only matching items show.
7. Click Format JSON with valid JSON, then enter invalid JSON and analyze; the app should explain the syntax error.
8. Export JSON and Markdown. Open both files and confirm no demo credential is shown in the evidence.
9. Click Clear inputs; verify findings are removed and exports are disabled.
10. Resize to mobile width and ensure controls remain operable.
11. Try text containing a JWT-like secret and an email; review whether the current masking patterns catch it.
12. Try a sanitized log with no matching errors; confirm the readiness copy does not promise production safety.