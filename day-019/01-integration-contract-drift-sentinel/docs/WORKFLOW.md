# FDE workflow

1. Obtain the baseline contract currently used by the integration.
2. Obtain the exact candidate contract and provider release notes.
3. Remove internal URLs, secrets and customer-specific examples if they do not need to be shared.
4. Load both revisions and analyze changes.
5. Review breaking and semantic findings; verify each finding in the provider documentation.
6. Validate representative customer request fixtures against both versions.
7. Generate regression tests for each compatibility risk.
8. Execute the tests in a non-production environment; the Sentinel does not run them.
9. Agree on migration steps, versioning, rollout window, owner and rollback condition.
10. Publish the review as part of the deployment record and reassess when the contract changes.

Do not turn a warning off merely to get a green status. Record a compatibility decision and its evidence.