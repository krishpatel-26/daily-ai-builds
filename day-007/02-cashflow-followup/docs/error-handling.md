# Error handling

Invalid invoice fields throw clear validation errors before state changes. Duplicate invoice numbers are rejected within the workspace. Storage writes return a failure status rather than claiming persistence. CSV parse errors are shown to the user. Clipboard access has a fallback. Clearing records requires explicit confirmation.

Remaining work: row-specific CSV diagnostics, import size limits, and stronger clipboard fallback coverage.