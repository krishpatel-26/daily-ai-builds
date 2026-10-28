export function createFixedWindowState() { return new Map(); }
export function fixedWindowDecision(state, key, timestamp, policy, cost = 1) {
  const windowMs = Math.max(1, Number(policy.windowMs)), limit = Math.max(1, Number(policy.limit)), now = Number(timestamp);
  const start = Math.floor(now / windowMs) * windowMs;
  let bucket = state.get(key);
  if (!bucket || bucket.start !== start) bucket = { start, count: 0 };
  const requestCost = Math.max(1, Number(cost) || 1), allowed = bucket.count + requestCost <= limit;
  if (allowed) bucket.count += requestCost;
  state.set(key, bucket);
  const resetAtMs = start + windowMs;
  return { allowed, statusCode: allowed ? 200 : 429, limit, remaining: Math.max(0, limit - bucket.count), resetAtMs, retryAfterMs: allowed ? 0 : Math.max(0, resetAtMs - now), used: bucket.count, reason: allowed ? "Within current fixed window." : "Fixed-window request budget exhausted." };
}
