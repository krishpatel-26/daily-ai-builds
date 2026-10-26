# Architecture

The tool is a dependency-free browser application with a small Node.js static server.

- src/core.js parses CSV, applies configured comparison normalization, indexes records by key, detects duplicate/blank identities, matches records and compares mapped fields.
- app.js manages file uploads, editable CSV text, key selectors, mapping controls, rendering and exports.
- scripts/serve.js serves static files on loopback.
- fixtures contain synthetic examples only.

The core is exportable for CommonJS tests and exposes a browser global. The app makes no network requests and does not store data in localStorage. Source CSV remains in browser memory while the page is open. Exports are generated locally by the browser.