# Architecture

The app consists of a static HTML/CSS dashboard, a dependency-free JavaScript core and a small Node static server.

## Flow
1. Accept a baseline and candidate OpenAPI-style JSON document.
2. Parse and structurally compare operations, parameters, request/response schemas and component schemas.
3. Classify changes as breaking, additive or review, with severity, confidence note, evidence and next action.
4. Derive risk classification and regression-test ideas from the changes.
5. Validate a caller-provided JSON payload against a basic request-schema subset.
6. Export a Markdown review, test-plan JSON or complete analysis snapshot.

The core in src/core.js works both in the browser and CommonJS tests. The UI renders dynamic values through textContent or an explicit HTML escape helper. No API server, database or analytics is present.