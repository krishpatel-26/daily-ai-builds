# Implementation verification checklist

Before calling a blocker resolved:
- reproduce the original issue or capture a reliable source;
- agree on expected behavior with the customer;
- document environment and relevant versions without exposing secrets;
- implement the smallest safe change;
- test the happy path and important failure modes;
- verify behavior with the customer or their approved test;
- record evidence of the outcome;
- update the account handoff with remaining limitations.