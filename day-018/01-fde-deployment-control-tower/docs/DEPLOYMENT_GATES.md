# Deployment readiness gates

## 1. Discovery
Identify customer stakeholders, integration scope and measurable acceptance criteria before engineering effort starts.

## 2. Connectivity
Confirm environment, host, region, DNS/network path and a bounded smoke test from the actual runtime location.

## 3. Authentication
Record the authentication pattern and secret owner, verify minimum roles/scopes and plan expiry/rotation without copying a credential into notes.

## 4. API contract
Validate schema version, required fields, mapping, null/duplicate behavior and negative validation paths with synthetic fixtures.

## 5. Observability
Require request/correlation IDs, timestamps, bounded deadlines/retries, dashboards and an escalation owner.

## 6. Security and data handling
Verify TLS, webhook signature and replay protection, least privilege, personal-data minimization and retention.

## 7. UAT
Prove the happy path, important failures/recovery paths and customer acceptance against agreed criteria.

## 8. Go-live and rollback
Assign launch authority, agree the change window, test or rehearse rollback, and set post-launch monitoring and exit criteria.

A check marked Pass without evidence remains an evidence gap. A failed required check blocks the GO-TO-REVIEW recommendation.