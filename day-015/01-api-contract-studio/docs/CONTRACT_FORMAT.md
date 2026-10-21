# Contract format

Example:
```json
{
  "title": "Create Customer",
  "type": "object",
  "required": ["email"],
  "properties": {
    "email": {"type": "string", "minLength": 5, "maxLength": 120},
    "seats": {"type": "integer", "minimum": 1, "maximum": 500},
    "plan": {"type": "string", "enum": ["starter", "growth"]}
  }
}
```

Supported keywords are a subset. Unsupported keywords are ignored rather than fully enforced, so users must not assume complete JSON Schema compliance.