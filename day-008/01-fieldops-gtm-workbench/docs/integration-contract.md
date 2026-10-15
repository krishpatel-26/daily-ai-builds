# Future integration contract

No integrations are implemented in this prototype. Before adding a CRM, ticketing system, or support platform connector, define:
- the minimum fields required and their source of truth;
- read/write permissions and least-privilege scopes;
- duplicate handling and idempotency;
- audit trail and deletion behavior;
- failure and retry semantics;
- consent and customer-data retention requirements.

Do not sync field notes into external systems without explicit authorization.