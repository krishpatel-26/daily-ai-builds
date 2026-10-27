const playbooks = {
  timeout: { severity: "medium", category: "Transient transport", action: "Confirm destination health, then retry with backoff and idempotency protection." },
  rate_limit: { severity: "medium", category: "Rate limiting", action: "Respect Retry-After, lower concurrency, and avoid synchronized retry bursts." },
  auth: { severity: "high", category: "Authentication", action: "Validate credential scope, secret rotation and destination authentication before retrying." },
  validation: { severity: "high", category: "Payload contract", action: "Compare payload schema with receiver contract; correct the event before replay." },
  forbidden: { severity: "high", category: "Authorization", action: "Check destination permissions and workspace access; do not retry unchanged." },
  not_found: { severity: "medium", category: "Endpoint routing", action: "Verify the receiver URL and route version before replay." },
  server_error: { severity: "medium", category: "Destination 5xx", action: "Inspect receiver health and correlate provider logs; retry within bounded policy." },
  unknown: { severity: "medium", category: "Unclassified", action: "Inspect response body, provider request ID and destination logs before deciding." },
  none: { severity: "low", category: "Delivered", action: "No action required; retain evidence for audit." }
};
export function classifyFailure(event) {
  const key = String(event?.failureType ?? (event?.status === "delivered" ? "none" : "unknown")).toLowerCase();
  const base = playbooks[key] ?? playbooks.unknown;
  return { ...base, failureType: key, shouldRetry: ["timeout", "rate_limit", "server_error", "unknown"].includes(key) && event?.status !== "delivered" };
}
