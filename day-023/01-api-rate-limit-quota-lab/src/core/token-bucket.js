export function createTokenBucketState() { return new Map(); }
export function tokenBucketDecision(state, key, timestamp, policy, cost = 1) {
  const now = Number(timestamp), capacity = Math.max(1, Number(policy.limit)), windowMs = Math.max(1, Number(policy.windowMs));
  const refillPerMs = capacity / windowMs, requestCost = Math.max(1, Number(cost) || 1);
  const previous = state.get(key) ?? { tokens: capacity, updatedAt: now };
  const elapsed = Math.max(0, now - previous.updatedAt), tokens = Math.min(capacity, previous.tokens + elapsed * refillPerMs);
  const allowed = tokens >= requestCost, nextTokens = allowed ? tokens - requestCost : tokens;
  state.set(key, { tokens: nextTokens, updatedAt: now });
  const retryAfterMs = allowed ? 0 : Math.ceil((requestCost - tokens) / refillPerMs);
  return { allowed, statusCode: allowed ? 200 : 429, limit: capacity, remaining: Math.floor(nextTokens), resetAtMs: now + Math.ceil((capacity - nextTokens) / refillPerMs), retryAfterMs, used: capacity - nextTokens, reason: allowed ? "Token bucket has sufficient capacity." : "Insufficient tokens; wait for refill." };
}
