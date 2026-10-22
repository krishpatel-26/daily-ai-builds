# LiveGlass AI — Day 016

Windows 10/11 desktop MVP for translating detected screen text into English using a transparent, click-through overlay.

Features: Electron dashboard, always-on-top overlay, primary-display capture, local OCR with Tesseract.js, local-first Argos Translate integration, optional HTTPS translation API fallback, keyboard shortcuts, configurable scan interval and opacity.

## Run

Install Node.js 22 LTS or later, extract the project, open PowerShell in this directory, then run:

    npm install
    npm run check
    npm start

For offline German-to-English translation, see docs/WINDOWS_SETUP.md.

## Shortcuts
- Ctrl+Shift+L: start or pause live translation
- Ctrl+Shift+O: show the dashboard
- Ctrl+Shift+K: clear translated overlay boxes

## Limitations
This is an MVP, not a release-tested desktop product. It draws glass boxes over the detected source text; it does not reconstruct the original background. It currently captures the primary display only. DPI, OCR quality, click-through behavior and packaged installation must be checked on Windows hardware.

## Privacy
OCR runs locally. API fallback is disabled by default in the project settings. When enabled, recognized text is sent to the configured translation endpoint; screenshots are not sent by the translation helper. Read docs/PRIVACY.md before using it with sensitive content.