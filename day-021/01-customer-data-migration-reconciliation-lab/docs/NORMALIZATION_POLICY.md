# Normalization policy

The UI offers two comparison-only normalization options:
1. Trim surrounding whitespace from compared values and keys.
2. Lowercase a value only when the mapped field name contains “email” and the value resembles an email address.

These options do not mutate the CSV editors or downloaded source files. They can hide differences that matter in some business contexts. Confirm the source system's canonicalization rules before enabling them for real customer data.

The tool intentionally does not coerce dates, numeric formats, time zones, phone numbers, Unicode, null sentinels or locale-specific decimal separators. Add explicit, reviewed transformations for these cases rather than guessing.