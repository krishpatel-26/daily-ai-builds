import { retryAfterSeconds } from "./retry-after.js";

// These generic headers illustrate a possible mapping; use the actual provider contract in production.
export function toDemoRateLimitHeaders(decision, nowMs=0){
 const headers={
  "X-RateLimit-Limit":String(decision.limit),
  "X-RateLimit-Remaining":String(decision.remaining),
  "X-RateLimit-Reset":String(Math.ceil((Number(decision.resetAtMs)+Number(nowMs))/1000))
 };
 if(!decision.allowed)headers["Retry-After"]=String(retryAfterSeconds(decision.retryAfterMs));
 return headers;
}
