# Security and Privacy Notes

- The local prototype has no authentication; do not expose it publicly with personal data.
- Resume content is stored in local SQLite in plaintext.
- Optional LLM mode sends supplied prompt text to the configured provider. Review provider retention policies before enabling it.
- Never commit API keys, resumes, or personal information.
- Add authentication, encryption at rest, deletion/export controls, rate limiting, and audit logs before multi-user deployment.
- Treat resume text as untrusted input.