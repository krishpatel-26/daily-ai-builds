# Event data contract

## Minimum event envelope
- event_id: stable non-empty string used for traceability and deduplication
- event_type: non-empty string identifying the business event
- created_at: timestamp string parseable as a date-time
- data: JSON object containing event-specific fields

## Example
```json
{
  "event_id": "evt_1042",
  "event_type": "order.created",
  "created_at": "2026-10-20T10:45:00Z",
  "data": {"order_id": "ord_219", "total": 86.5, "currency": "USD"}
}
```

## Contract cautions
The prototype checks field presence and basic types, not event-type-specific required fields, unknown properties, numeric ranges, signature validity, version compatibility, or semantic consistency. A production integration should version its event schemas and publish compatibility rules.