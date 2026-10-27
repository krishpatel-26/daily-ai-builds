export function retryDelayMs(attempt, options = {}) {
  const baseMs = Math.max(0, Number(options.baseMs ?? 1000)); const maxMs = Math.max(baseMs, Number(options.maxMs ?? 60000));
  const maxAttempts = Math.max(1, Math.floor(Number(options.maxAttempts ?? 6))); const n = Math.max(1, Math.floor(Number(attempt) || 1));
  if (n >= maxAttempts) return null;
  return Math.min(maxMs, baseMs * (2 ** (n - 1)));
}
export function buildRetrySchedule(startTime, options = {}) {
  const start = new Date(startTime); if (Number.isNaN(start.getTime())) throw new TypeError("startTime must be a valid date.");
  const attempts = Math.max(1, Math.floor(Number(options.maxAttempts ?? 6))); const schedule = []; let next = start.getTime();
  for (let attempt = 1; attempt < attempts; attempt += 1) {
    const delay = retryDelayMs(attempt, options); if (delay === null) break;
    next += delay; schedule.push({ attempt: attempt + 1, delayMs: delay, at: new Date(next).toISOString() });
  }
  return schedule;
}
export function retryDecision(event, options = {}) {
  if (event?.status === "delivered") return { retry: false, reason: "Already delivered." };
  if (event?.status === "dead-letter") return { retry: false, reason: "Dead-lettered events require explicit review." };
  const maxAttempts = Math.max(1, Math.floor(Number(options.maxAttempts ?? 6)));
  if (Number(event?.attempt ?? 0) >= maxAttempts) return { retry: false, reason: "Attempt limit reached." };
  const failure = String(event?.failureType ?? "").toLowerCase();
  if (["auth", "validation", "forbidden", "not_found"].includes(failure)) return { retry: false, reason: "Likely permanent failure: fix configuration or payload first." };
  return { retry: true, reason: "Retry may be appropriate after checking side effects and rate limits." };
}
