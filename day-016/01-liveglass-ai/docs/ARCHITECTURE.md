# Architecture

The Electron main process controls screen capture, settings, OCR lifecycle, keyboard shortcuts, system tray, and translation orchestration. Dashboard and overlay renderer processes run with Node integration disabled and context isolation enabled. A preload bridge exposes a small IPC API.

## Scan flow
1. Capture the primary display via Electron desktopCapturer.
2. Run local Tesseract.js OCR against the returned PNG.
3. Filter short and low-confidence lines.
4. Try local Argos Translate, then optionally use a configured API endpoint.
5. Scale OCR coordinates to the display bounds and render English text boxes.
6. Repeat on a timer while live mode is active.

## Trade-offs
Scans run serially; busy scans are skipped. Glass boxes cover source text but do not reconstruct background pixels. Multi-monitor and per-window capture are future improvements.