# Manual test checklist

- [ ] Load sample and verify schema and payload populate.
- [ ] Validate valid sample; expect no supported-rule violations.
- [ ] Load invalid sample; expect required-field and constraint findings.
- [ ] Remove required fields and inspect issue paths.
- [ ] Try malformed schema and payload JSON.
- [ ] Format both editors.
- [ ] Compare previous and current schemas.
- [ ] Generate test cases for sample schema.
- [ ] Export and parse report JSON.
- [ ] Export and parse test-pack JSON.
- [ ] Add nested properties and check nested rules.
- [ ] Test enums and numeric bounds.
- [ ] Resize to mobile width and use keyboard navigation.
- [ ] Confirm no API calls occur.
- [ ] Confirm wording does not imply full JSON Schema compliance.