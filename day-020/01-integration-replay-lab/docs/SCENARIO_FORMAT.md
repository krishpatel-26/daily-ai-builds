# Scenario pack format

A pack is a JSON object with a name and a non-empty scenarios array.

Each scenario uses:
- id: stable unique identifier
- title: concise, observable outcome
- method: supported HTTP method
- path: local/illustrative route beginning with slash
- request: optional headers and JSON body used as context
- mockResponse: status, headers, body and simulated latency
- assertions: conditions to evaluate against that mock response

Minimal example:

    {
      "id": "read-customer",
      "title": "Customer response contains an ID",
      "method": "GET",
      "path": "/v1/customers/demo",
      "mockResponse": {
        "status": 200,
        "headers": {"content-type": "application/json"},
        "body": {"customer": {"id": "demo"}},
        "latencyMs": 30
      },
      "assertions": {
        "status": 200,
        "requiredJsonPaths": ["customer.id"],
        "maxLatencyMs": 100
      }
    }

JSON paths are simple dot-separated paths, with dollar sign representing the root. Escaped keys, array indexes and JSONPath operators are not supported by the MVP.