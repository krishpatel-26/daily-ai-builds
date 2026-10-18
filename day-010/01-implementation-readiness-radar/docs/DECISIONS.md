# Design decisions

## Why a checklist first?
A checklist is easier to inspect and validate than a generated readiness verdict.

## Why weighted scoring?
Not all launch prerequisites carry equal risk. Weights make the assumption explicit, though they require calibration.

## Why critical gates?
A high score should not hide unresolved security, access, integration, or acceptance work.

## Why local-first?
The prototype can be explored without credentials or customer data leaving the browser.

## Why manual exports?
The user controls when an assessment is shared, and the prototype avoids unapproved external commitments.