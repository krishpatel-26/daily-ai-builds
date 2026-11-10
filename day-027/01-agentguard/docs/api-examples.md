# API examples

## Allowed read
```bash
curl -X POST http://127.0.0.1:8000/api/evaluate -H "Content-Type: application/json" -d '{"actor":"bot","role":"support_agent","action":"read","resource_type":"ticket","resource_id":"T-1","payload":{}}'
```

## Approval-gated update
```json
{"actor":"bot","role":"support_agent","action":"update_contact","resource_type":"customer","resource_id":"C-10","payload":{"email":"new@example.com"}}
```
