# Input formats

## Log input
Paste newline-delimited application logs. Include UTC timestamp, request ID, endpoint label, status code and error message where available. The analyzer scans text for recognizable patterns; structure is not mandatory.

## Config input
Provide a JSON object. Common optional properties include:
- environment, env or stage
- base_url, api_url or endpoint
- auth_type, authentication or auth
- timeout_ms or timeout
- retry_attempts or max_retries
- webhook_signature_validation or verify_webhook_signature
- verify_tls, ssl_verify or reject_unauthorized
- api_version or version

Unknown fields are ignored by preventive checks. The analyzer does not verify a real endpoint or interpret arbitrary nested schemas. Never paste unredacted customer credentials or personal data.