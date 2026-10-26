# Privacy and data handling

- CSV parsing and reconciliation run inside the current browser page.
- The Node server serves static assets only and listens on 127.0.0.1.
- The app has no backend, telemetry, network connector or localStorage persistence.
- The original CSV text remains in the editor until replaced or the page closes.
- Exported reports may contain customer field values and identifiers; inspect them before sharing.
- File input is limited to 20 MB per file in the UI.
- Pattern-based anonymization is not implemented for the full report; therefore, treat export values as sensitive.

Use synthetic or pre-sanitized exports. Never paste credentials or sensitive personal data into a public demo. Local-only processing does not mean the files are encrypted or protected from browser extensions or other users of the same machine.