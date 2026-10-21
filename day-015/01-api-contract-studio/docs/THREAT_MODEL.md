# Threat model

Assets: schema definitions, payloads, validation findings, and exported reports.

Risks: confidential payloads pasted into a page; partial validation mistaken for full compliance; generated examples mistaken for production data; heuristic diffs misread as compatibility proof.

Mitigations: use synthetic demo data, process locally, disclose supported rules, review contract changes with consumers, and avoid credentials or personal data in public fixtures. No authentication or persistence is included.