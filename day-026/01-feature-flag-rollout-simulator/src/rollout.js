export function stableBucket(identifier) {
  let hash = 2166136261;
  for (const char of String(identifier)) {
    hash ^= char.charCodeAt(0);
    hash = Math.imul(hash, 16777619);
  }
  return (hash >>> 0) % 100;
}

export function evaluateExposure(identifier, percentage, enabled = true) {
  if (!enabled) return false;
  const pct = Math.max(0, Math.min(100, Number(percentage) || 0));
  return stableBucket(identifier) < pct;
}

export function assessGuardrails({ errorRate, latencyP95, maxErrorRate = 2, maxLatencyP95 = 500 }) {
  const errors = Number(errorRate);
  const latency = Number(latencyP95);
  if (![errors, latency, Number(maxErrorRate), Number(maxLatencyP95)].every(Number.isFinite)) {
    throw new TypeError("Guardrail metrics and thresholds must be finite numbers.");
  }
  const breaches = [];
  if (errors > maxErrorRate) breaches.push({ metric: "errorRate", actual: errors, limit: Number(maxErrorRate) });
  if (latency > maxLatencyP95) breaches.push({ metric: "latencyP95", actual: latency, limit: Number(maxLatencyP95) });
  return { safe: breaches.length === 0, decision: breaches.length ? "ROLLBACK" : "CONTINUE", breaches };
}

export function simulateRollout(config) {
  const steps = (config.steps ?? [1, 5, 25, 50, 100]).map(Number);
  if (!steps.length || steps.some((n, i) => !Number.isFinite(n) || n < 0 || n > 100 || (i && n < steps[i - 1]))) {
    throw new RangeError("Rollout steps must be ascending percentages between 0 and 100.");
  }
  const results = [];
  for (const percentage of steps) {
    const guardrail = assessGuardrails({
      errorRate: config.errorRate,
      latencyP95: config.latencyP95,
      maxErrorRate: config.maxErrorRate,
      maxLatencyP95: config.maxLatencyP95
    });
    results.push({ percentage, ...guardrail });
    if (!guardrail.safe) break;
  }
  return {
    status: results.at(-1).decision === "ROLLBACK" ? "ROLLED_BACK" : "READY_TO_PROMOTE",
    results,
    finalExposure: results.at(-1).decision === "ROLLBACK" ? 0 : results.at(-1).percentage
  };
}

export function flagHealth(flag, now = new Date()) {
  const ageDays = Math.floor((now.getTime() - new Date(flag.createdAt).getTime()) / 86400000);
  const issues = [];
  if (!flag.owner?.trim()) issues.push("Missing owner");
  if (!flag.purpose?.trim()) issues.push("Missing purpose");
  if (!flag.reviewDate) issues.push("Missing review date");
  if (flag.percentage === 100 && ageDays > 14) issues.push("Fully rolled out: consider retiring the flag");
  if (ageDays > 90) issues.push("Flag older than 90 days: review lifecycle");
  return { ageDays, issues, health: issues.length ? "REVIEW" : "HEALTHY" };
}
