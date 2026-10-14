# Data model

An invoice record contains:
- `id`: stable local identifier
- `client`: required display name
- `number`: required invoice reference, unique in the current workspace
- `amount`: positive numeric amount, interpreted as INR in the UI
- `issueDate`: ISO date (YYYY-MM-DD)
- `dueDate`: ISO date, not earlier than issue date
- `status`: `unpaid` or `paid`
- `createdAt`: ISO timestamp

Dates are stored as date-only strings to avoid time-zone shifts in due-date math. This MVP has no currency conversion, tax calculation, payment reconciliation, or multi-user conflict resolution.
