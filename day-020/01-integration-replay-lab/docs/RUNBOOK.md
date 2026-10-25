# Local runbook

## Start
Use Node.js 18 or newer. From this directory:

    npm start

Open http://127.0.0.1:4173.

## Check code and tests
    npm run check
    npm test

## Common issues
- Port in use: set PORT=4174 before starting the server.
- Invalid JSON: the error banner gives the parse location.
- No results: validate the scenario pack, then run all replays.
- Export disabled: run the scenarios to create the result snapshot.
- Generated tests fail syntax: inspect the export and report the issue; exports must be reviewed and are not guaranteed for every unusual key or schema.

No external credentials or API keys are required.