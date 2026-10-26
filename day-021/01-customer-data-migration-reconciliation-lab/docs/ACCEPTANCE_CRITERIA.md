# Acceptance criteria

- [ ] CSV parser accepts quoted commas, doubled quotes and multiline fields.
- [ ] Duplicate/blank headers and unterminated quoted fields produce clear errors.
- [ ] UI loads source and target CSV files locally, with a 20 MB limit per file.
- [ ] Source and target record keys can be selected independently.
- [ ] Source fields can map to differently named target fields.
- [ ] Reconciliation finds missing, extra, duplicate and blank-key records.
- [ ] Reconciliation identifies differences for mapped fields only.
- [ ] Optional trim and email case normalization affect comparison values but not editor text.
- [ ] Filters switch between finding categories.
- [ ] Markdown and JSON findings reports export successfully.
- [ ] npm run check and npm test pass.
- [ ] Browser manual checks are performed before a wider release.

This file is an acceptance checklist, not a claim that every browser case has already been tested.