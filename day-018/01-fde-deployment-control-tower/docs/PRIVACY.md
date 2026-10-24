# Privacy and data handling

- Workspace records are stored in this browser's localStorage.
- The app has no API backend, analytics or customer-system connectors.
- JSON and Markdown exports are generated locally when a user clicks an export button.
- Common bearer token, API key, password, JWT-like and email patterns are masked in export/display paths, but pattern-based redaction is not guaranteed.
- Raw notes remain in the form controls and localStorage until cleared by the user. Treat this device and browser profile as sensitive.
- A shared computer, browser sync, extensions or an exported file can expose locally stored content. Use synthetic evidence wherever possible.
- Never paste credentials, access tokens, private customer data or full production payloads. If real credentials were exposed, follow the customer's incident and rotation process.

This prototype has no encrypted workspace vault or role-based access control. Do not treat localStorage as secure storage.