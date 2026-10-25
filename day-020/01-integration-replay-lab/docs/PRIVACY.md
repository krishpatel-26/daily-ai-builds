# Privacy and data handling

- Scenario parsing and replay happen in the current browser page.
- The included Node.js server only serves static project files on loopback. The app makes no outbound API requests.
- Export actions mask common bearer tokens, key/secret assignments, provider-style API-key prefixes and email addresses.
- Redaction is heuristic and can miss secret formats; it is not a guarantee.
- The editor retains the user's original text until it is replaced or the page is closed. It is not encrypted or persisted by the app.
- Exports may include contract details, route names and payload structure. Review them before sharing.
- Use synthetic values by default. Never commit actual credentials, production payloads or identifiable customer information to public repositories.

If a live credential is accidentally shared, follow the credential owner's rotation and incident procedures; do not assume redaction after pasting reverses an exposure.