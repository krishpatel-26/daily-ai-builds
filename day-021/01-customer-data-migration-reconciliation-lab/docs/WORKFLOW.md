# FDE migration workflow

1. Confirm the migration's success criteria and authoritative source snapshot time.
2. Export a complete, sanitized source snapshot and destination snapshot from the same agreed window.
3. Identify a stable unique key in each export.
4. Define the source-to-target field mapping and transformations approved by the data owner.
5. Run the reconciliation and review missing/extra records, duplicate/blank keys and field mismatches.
6. Compare with the migration job's accepted/rejected counts and logs.
7. Investigate each difference using the source/target system as ground truth.
8. Fix or disposition the issue in the migration process; do not edit source data just to obtain a green report.
9. Re-export both sides after remediation and rerun the same scoped checks.
10. Have the data owner review exceptions, totals, field scope and acceptance criteria before sign-off.
11. Record a reviewer, decision notes and report artifact in the team's approved system.

The report supports sign-off; it cannot certify completeness for unmapped fields or unrepresented business rules.