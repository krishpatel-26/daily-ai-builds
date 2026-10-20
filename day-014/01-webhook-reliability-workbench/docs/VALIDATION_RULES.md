# Payload validation rules

The current validator checks:
- Valid JSON syntax
- Presence of event_id, event_type, created_at, and data
- Non-empty strings for event_id and event_type
- A parseable date-time string for created_at
- data must be a non-null JSON object, not an array

It deliberately does not validate a separate schema for each event_type.

## Production enhancements
- JSON Schema or equivalent versioned contracts
- Required and optional data properties per event type
- Payload size limits
- Unknown-field policy and backward compatibility
- Signature and timestamp verification
- Content type and character encoding checks
- Clear distinction between structural validity and business-rule validity