export function createSlidingWindowState() { return new Map(); }
export function slidingWindowDecision(state, key, timestamp, policy, cost = 1) {
  const windowMs = Math.max(1, Number(policy.windowMs)), limit = Math.max(1, Number(policy.limit)), now = Number(timestamp), cutoff = now - windowMs;
  const history = (state.get(key) ?? []).filter((entry) => entry.at > cutoff);
  const used = history.reduce((total, entry) => total + entry.cost, 0), requestCost = Math.max(1, Number(cost) || 1), allowed = used + requestCost <= limit;
  if (allowed) history.push({ at: now, cost: requestCost });
  state.set(key, history);
  const count = history.reduce((total, entry) => total + entry.cost, 0), remaining = Math.max(0, limit - count);
  const resetAtMs = history.length ? Math.min(...history.map((entry) => entry.at)) + windowMs : now + windowMs;
  return { allowed, statusCode: allowed ? 200 : 429, limit, remaining, resetAtMs, retryAfterMs: allowed ? 0 : Math.max(0, resetAtMs - now), used: count, reason: allowed ? "Within rolling time window." : "Rolling-window request budget exhausted." };
}
