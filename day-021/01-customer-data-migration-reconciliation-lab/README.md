# Customer Data Migration Reconciliation Lab — Day 021

A local-first FDE workbench for validating customer data migrations by comparing source and target CSV exports. Match records by a chosen key, detect duplicates, missing/extra records and field-level mismatches, preview safe normalizations, and generate a migration sign-off report.

## Run
Requirements: Node.js 18+. No npm runtime dependencies.

    npm start

Open http://127.0.0.1:4173. Run automated tests with npm test and syntax checks with npm run check.

## Demo workflow
1. Click Load sample migration.
2. Review source and target CSV, keys and field mappings.
3. Click Reconcile data.
4. Inspect missing records, extra records, duplicates and field mismatches.
5. Enable normalization previews (trim whitespace and case-fold email values) to check whether formatting differences explain mismatches.
6. Export a Markdown migration report or JSON findings package.

## Privacy and scope
CSV parsing and reconciliation run entirely in the browser. The local server only serves static files and no customer endpoint is called. The app does not upload, persist or transmit source data. Exported reports can contain field values; review them before sharing.

Use synthetic or sanitized data. This prototype does not encrypt files, implement role-based access, infer complex entity relationships or replace a customer-approved migration validation plan.

A zero-difference result means only that the selected data, key, field mapping and configured normalization rules matched; it is not proof of overall business correctness.