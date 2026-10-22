# Threat model

Screen contents can include authentication codes, private messages, customer data, internal documents and secrets. Translation keys also require protection.

Risks and mitigations:
- Accidental disclosure: API fallback is disabled by default; local translation is preferred.
- Credential exposure: use Electron safeStorage when available and never commit settings or environment files.
- Renderer compromise: keep context isolation on, Node integration off and the IPC surface narrow.
- Endpoint interception: require HTTPS except for localhost.
- OCR feedback: request overlay content protection; treat it as best effort.
- Over-capture: scan at a bounded interval and skip overlapping scans.

This MVP is not an enterprise DLP system and is not suitable as a certified accessibility or compliance product without further review.