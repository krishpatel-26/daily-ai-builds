# Privacy and data handling

- Analysis runs in the local browser tab. The included server only serves static project files and receives no diagnostic evidence in a backend.
- No customer endpoint is called and no telemetry is emitted by this prototype.
- Common bearer tokens, API-key assignments, passwords, JWT-like strings and email addresses are masked in displayed evidence and reports.
- Redaction uses patterns and is not a guarantee. Unknown token formats, encoded secrets, multiline values or credentials embedded in unusual formats may remain.
- The original input remains in the browser text boxes until the user clears it or closes the page. It is not automatically overwritten after analysis.
- Exports contain the current redacted report; review exported material before sending it to a customer or teammate.
- Do not commit real logs, personal data, access tokens, session IDs or tenant-identifying metadata to a public repository.

For real customer investigations, follow the organization's data classification, incident response and secret-rotation policy. If a real credential was exposed in a shared place, treat that as an incident even if the tool redacts it after pasting.