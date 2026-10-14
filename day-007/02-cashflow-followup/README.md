# Cashflow Follow-up Planner

A local-first tool for freelancers and small businesses to track unpaid invoices and decide which follow-up to send next.

## The real-world problem
Small teams often manage invoices across spreadsheets, email, and memory. Due dates slip, late payments are hard to prioritize, and follow-up messages take time to write. This MVP turns a simple invoice list into an actionable work queue.

## MVP features
- Add, edit, and delete invoices
- Track client, invoice number, amount, issue date, due date, and status
- Calculate overdue days and outstanding value
- Prioritize follow-ups by lateness and amount
- Draft polite reminder messages (nothing is sent automatically)
- Search and filter invoices
- Export/import CSV
- Local browser persistence; no account or external service required
- Sample data clearly marked as demo data

## Run
Open `index.html` in a modern browser. No build step or API key required.

## Privacy and limitations
Data stays in the browser's local storage unless the user exports it. This is a lightweight MVP, not accounting software: it does not verify payments, issue invoices, connect to a bank, or send emails. Back up data with CSV export. Use sample data only for demos.

## Project structure
- `index.html` — app shell
- `styles.css` — responsive interface
- `app.js` — user interactions and rendering
- `src/` — domain, storage, CSV, reminder, and metrics helpers
- `tests/` — Node built-in tests for core business rules
- `docs/` — product decisions, QA, privacy, and roadmap
