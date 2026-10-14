# Manual QA checklist

## Invoice CRUD
- [ ] Add a valid invoice.
- [ ] Reject empty client/invoice number.
- [ ] Reject zero or negative amount.
- [ ] Reject due date earlier than issue date.
- [ ] Edit an existing invoice without duplicating it.
- [ ] Reject duplicate invoice number.
- [ ] Mark paid and reopen.

## Queue
- [ ] Outstanding total excludes paid invoices.
- [ ] Overdue labels update based on local date.
- [ ] Search matches client and invoice number.
- [ ] Filters and sorting can be combined.
- [ ] Empty state appears when there are no matches.

## Reminder and data portability
- [ ] Reminder includes client, number, amount, and due status.
- [ ] Paid invoices cannot generate reminders.
- [ ] Copy button reports clipboard failures gracefully.
- [ ] Export CSV and import it into an empty workspace.
- [ ] Malformed CSV reports an understandable error.
- [ ] Reload restores locally stored records.
- [ ] Clear action requires confirmation.

Core unit tests use Node's built-in test runner: `node --test tests/*.test.js`. Tests have not been executed in this repository session.
