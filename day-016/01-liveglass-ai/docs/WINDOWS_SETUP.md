# Windows setup

## Start the app
1. Install Node.js 22 LTS or newer.
2. Extract the project and open PowerShell in its folder.
3. Run npm install, then npm run check, then npm start.

The first scan may need to download OCR language data.

## German to English offline translation
Install Python 3.12 and ensure the Python launcher is available. Then run:

    py -3.12 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip argostranslate
    python scripts\install_language.py --from-lang de --to-lang en

Restart the app, choose German, and scan once. Install other Argos language pairs only where a package is available.

## Keyboard shortcuts
- Ctrl+Shift+L starts or pauses live translation.
- Ctrl+Shift+O shows the controls dashboard.
- Ctrl+Shift+K clears displayed translations.

## Windows installer
Run npm run dist:win. Test the generated installer on a clean Windows account before distributing it.