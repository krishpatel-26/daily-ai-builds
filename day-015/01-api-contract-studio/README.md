# Day 015 — API Contract Studio

A local-first developer tool for inspecting JSON API payloads against a lightweight schema, reviewing contract changes, and generating reproducible edge-case examples.

## Run
Open `index.html` in a modern browser. No package installation, API key, backend, or build step is needed.

## Features
- Edit a JSON contract and request/response example.
- Validate payloads using a documented subset of JSON Schema-like rules.
- Review path-specific validation findings.
- Compare contract revisions for property, required-field, type, enum, and selected constraint changes.
- Generate positive and negative test payloads.
- Export validation reports and generated test packs as JSON.
- Load a synthetic customer-creation example.

## Supported subset
`type`, `required`, `properties`, `enum`, `minimum`, `maximum`, `minLength`, `maxLength`, basic `format: email`, `items`, and `additionalProperties: false`.

## Limitations
This is not a complete JSON Schema implementation. Schema comparison focuses on root-level properties and selected keywords. Test cases are generated examples, not executed against a live API. Automated browser tests have not yet been run.