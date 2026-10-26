# Test strategy

Core tests cover:
- quoted CSV fields, commas, escaped quotes and multiline cell parsing
- errors for duplicate headers and unterminated quote sequences
- key-based record matching
- missing/extra records, duplicate keys, blank keys and field mismatches
- trimming and email case-folding behavior
- mapped source/target fields with different names
- invalid key and empty mapping validation
- report generation and zero-difference outcome

Server tests cover static asset delivery, security headers, not-found behavior and encoded path traversal.

These tests validate the local prototype's logic. They do not test real database exports, API connectivity, business-specific transformations or browser-level usability.