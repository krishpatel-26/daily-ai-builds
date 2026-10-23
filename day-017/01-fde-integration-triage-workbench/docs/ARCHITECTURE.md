# Architecture

The application is a dependency-free browser UI. A small Node.js static server is included for local development. Inputs remain in the current browser session; there is no API, database or telemetry in this prototype.

Flow:
1. Accept pasted logs and config JSON.
2. Apply conservative text redaction before rendering evidence or generating exports.
3. Run rule-based regex checks against log lines.
4. Run preventive configuration checks against the parsed JSON object.
5. Deduplicate by rule ID and sort findings by severity.
6. Calculate a simple penalty-based readiness score.
7. Render evidence, next actions and filters; export JSON or Markdown.

The readiness score is illustrative and should not be interpreted as a probability of deployment success. Rule definitions in config/rules.json document the initial catalog; app.js is the executable implementation.