# Manual smoke-test plan

Record Windows version, display resolution, scale factor and Node/Python versions.

## Controls
- [ ] Install dependencies, run npm run check, then npm start.
- [ ] Dashboard opens and Save settings succeeds.
- [ ] Start/pause works from button and Ctrl+Shift+L.
- [ ] Ctrl+Shift+O reveals the dashboard; Ctrl+Shift+K clears boxes.
- [ ] Tray actions still work after hiding the dashboard.
- [ ] Quit exits the app and unregisters shortcuts.

## OCR and overlay
- [ ] Display a high-contrast German webpage and Scan once.
- [ ] Check translation meaning and bounding-box alignment.
- [ ] Check 100%, 125% and 150% scaling.
- [ ] Click and scroll through the overlay.
- [ ] Verify overlay does not detect its own translated text repeatedly.
- [ ] Pause, clear, resume and change the screen during a scan.

## Privacy and failure handling
- [ ] API fallback off with Argos installed works after disconnecting internet.
- [ ] Missing local model and disabled fallback produces a clear error.
- [ ] Non-HTTPS remote endpoint is rejected.
- [ ] Settings persist after restart; key stays masked.

## Packaging
- [ ] Build the NSIS installer.
- [ ] Install and uninstall on a clean test account.