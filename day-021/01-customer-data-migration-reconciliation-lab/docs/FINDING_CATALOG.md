# Finding catalog

- Missing: a non-empty unique source key is absent from the target index. Verify batch status, rejects, pagination and retry/idempotency behavior.
- Extra: a target key does not occur in the source index. Determine whether it predates the migration or was introduced accidentally.
- Duplicate: a selected key repeats or is blank. Fix the identity rule or disposition duplicates before sign-off.
- Mismatch: matched records have different values for a configured field pair. Confirm mapping, intended transformation, null/default behavior and source/target snapshot timing.

Every finding records the key, source/target values and a recommended investigation step. Values may contain sensitive data. Use synthetic or sanitized files and review exports manually.