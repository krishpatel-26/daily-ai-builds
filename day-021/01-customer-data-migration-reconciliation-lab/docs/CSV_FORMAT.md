# CSV format

The parser supports common comma-separated exports with:
- a single header row
- commas inside double-quoted fields
- escaped double quotes represented by two double quotes
- CRLF, LF and CR line endings
- newline characters inside quoted fields
- UTF-8 BOM stripping

It rejects blank headers, duplicate headers, an unexpected quote inside an unquoted cell, unterminated quoted fields and rows containing extra non-empty cells. Short rows are filled with empty values.

This is a pragmatic implementation for common exports, not a formally certified RFC 4180 parser. Check delimiter, encoding, date and numeric conventions before relying on cross-system comparisons.