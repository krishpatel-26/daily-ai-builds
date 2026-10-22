# Translation providers

## Argos Translate
The Python helper reads JSON from stdin with texts, source and target fields. It returns an ok flag and translation array, or a reason. Language models must be installed in the Python environment used by the app.

## API fallback
The endpoint should accept a LibreTranslate-compatible JSON request and return translatedText. Remote endpoints must use HTTPS. Some hosts require keys, have rate limits, or are not free; terms, quotas and reliability vary.

## Known limitation
The current fallback joins lines with newline separators and splits the response back into segments. Providers may normalize line breaks, causing imperfect alignment. Segment-level translation is a future improvement.