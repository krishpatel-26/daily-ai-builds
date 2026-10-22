# Privacy and data handling

- Screen images are processed locally for OCR and are not intentionally uploaded.
- OCR language data may be downloaded once and cached on-device.
- Argos Translate runs locally when Python and a matching language model are installed.
- With API fallback enabled, recognized text is sent to the configured endpoint. The screenshot itself is not submitted by the translator.
- Use HTTPS for remote endpoints; HTTP is permitted only for localhost development.
- A custom endpoint may log or retain submitted text. Review its retention terms.
- API keys are persisted using Electron safeStorage when available. On platforms without encryption support, this MVP avoids writing the key to settings.json.
- The overlay requests content protection to avoid OCR feedback; platform support is best-effort, not a security guarantee.

For strict offline mode, turn API fallback off and install the needed Argos pair. Do not scan confidential content with an endpoint you do not trust.