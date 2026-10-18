# Architecture

The prototype is a static HTML/CSS/JavaScript application.

- index.html defines the page structure.
- styles.css provides responsive dark-mode layout.
- app.js owns checklist data, scoring, rendering, plan generation, and exports.
- docs explain the product assumptions and validation gaps.
- templates provide reusable handoff artifacts.
- tests/manual-test-cases.md records the current QA checklist.

There is no backend, authentication, network request, database, or external message delivery. Browser exports are generated locally.