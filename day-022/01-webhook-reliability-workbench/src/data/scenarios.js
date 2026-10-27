export const scenarios = [
  { id: "provider-timeout", title: "Provider timeout", failure: "timeout", description: "Destination did not respond before the deadline." },
  { id: "rate-limit", title: "Rate limited", failure: "rate_limit", description: "Destination asks the sender to slow down." },
  { id: "auth-expired", title: "Authentication rejected", failure: "auth", description: "Credentials or signing configuration may be invalid." },
  { id: "bad-payload", title: "Payload rejected", failure: "validation", description: "Destination rejected the body or schema." },
  { id: "success", title: "Delivered", failure: "none", description: "Destination returned a successful response." }
];
export function getScenario(id) { return scenarios.find((scenario) => scenario.id === id) ?? null; }
