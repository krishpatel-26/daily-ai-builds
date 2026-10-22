# Acceptance criteria

- [ ] App starts on a Windows 10/11 x64 machine with dependencies installed.
- [ ] Dashboard loads without renderer or IPC errors.
- [ ] Settings persist across restarts and API key is masked in the dashboard.
- [ ] Keyboard shortcuts start/pause, reveal controls and clear the overlay.
- [ ] Scan once surfaces completion or a useful failure message.
- [ ] High-contrast German text is detected and translated plausibly.
- [ ] Installed Argos language pair works without translation API requests.
- [ ] API fallback works with a compatible HTTPS endpoint when enabled.
- [ ] Overlay coordinates remain close at 100%, 125% and 150% DPI.
- [ ] Mouse clicks reach the app behind the overlay.
- [ ] Clear overlay removes all boxes.
- [ ] API fallback disabled means recognized text is not sent remotely.
- [ ] npm run check passes.

Syntax checks do not establish Windows runtime acceptance.