# Contributing

Please keep translation local by default and never commit screenshots, API credentials, tokens or private screen content.

## Local checks
    npm install
    npm run check
    python -m py_compile scripts/local_translate.py scripts/install_language.py

Preserve renderer isolation: Node integration off, context isolation on and use the named preload API. Update the manual test plan whenever capture, OCR, translation or overlay behavior changes.

Pull requests should state the Windows version tested, reproduction steps, expected versus actual behavior and any privacy impact. Explicitly note tests that were not run.