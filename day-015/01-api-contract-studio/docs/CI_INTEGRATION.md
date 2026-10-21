# CI integration

The current app does not run in CI. A future pipeline could validate schema syntax, run a standards-compliant validator over fixtures, compare contract snapshots, flag removed or newly required fields, and publish a machine-readable report.

Start in report-only mode. Agree on compatibility policy before making schema diffs a merge-blocking gate.