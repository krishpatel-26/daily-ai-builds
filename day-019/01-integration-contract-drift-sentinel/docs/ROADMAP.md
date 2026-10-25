# Roadmap

## Harden this prototype
- Add fixtures representing real provider release notes and reviewed compatibility outcomes.
- Expand schema resolution and context-aware request versus response classification.
- Add format, pattern, numeric range, nullable and composite-schema validation.
- Add source maps and clickable references from diff rows to JSON paths.
- Add deterministic snapshot tests for exports and edge cases.

## Next iteration
- Import OpenAPI files directly and support YAML with a vetted parser.
- Generate runnable contract tests for a selected language/framework.
- Add a consumer-contract fixture registry and baseline drift history.
- Add evidence fields for test owner, build, test run URL and observed outcome.
- Add CI integration to block a pull request only after a team configures and validates the policy.

## Future
- Integrate with approved API registries and CI systems using least-privilege tokens.
- Track false positive/negative rates against labeled real contract changes.
- Do not claim full OpenAPI support or release-gate quality until conformance tests and evaluations justify it.