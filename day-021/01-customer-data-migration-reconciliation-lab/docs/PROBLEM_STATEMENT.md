# Problem statement

A migration job can finish successfully while records are silently dropped, duplicated or transformed incorrectly. Teams often verify job status and a small handful of samples, but lack a repeatable record-level comparison between the source export and destination export.

Migration Reconciliation Lab compares two CSV snapshots using an explicit identity key and field map. It surfaces missing and extra records, ambiguous keys and field mismatches, then generates a reviewer-facing report.

## Target users
- Forward Deployed Engineers onboarding customer datasets
- Data integration and implementation engineers
- Solutions engineers validating import jobs
- Customer platform teams preparing migration sign-off

## Non-goals
The prototype is not an ETL engine, database connector, migration executor or automatic repair service. It never changes source or target data and cannot validate business rules that have not been mapped into the comparison.