# Roadmap

## Hardening
- Add report anonymization profiles and export preview.
- Support alternate delimiters, explicit encoding selection and very large files using streaming/Web Workers.
- Define policy for exact duplicates and composite keys.
- Add field-level counts, mismatch percentages and configurable severity thresholds.
- Add deterministic snapshot tests for the full report.

## Next iteration
- Add composite key support and configurable null/date/numeric normalization rules.
- Compare nested JSON exports and parent-child relationships.
- Generate CSV exception files containing only selected keys and mismatch columns.
- Preserve reconciliation configurations as portable, versioned templates.

## Future
- Optional read-only connectors to approved data stores with least privilege.
- Audit, approval and retention controls for team workspaces.
- Evaluate false positive/negative rates on labeled migration fixtures.
- Do not implement automatic repair or writes without a separate reviewed safety design.