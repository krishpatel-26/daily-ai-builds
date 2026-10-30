import test from "node:test";
import assert from "node:assert/strict";
import { stableBucket, evaluateExposure, assessGuardrails, simulateRollout, flagHealth } from "../src/rollout.js";

test("stable assignment is deterministic", () => {
  assert.equal(stableBucket("customer-42"), stableBucket("customer-42"));
});
test("disabled flag never exposes a feature", () => {
  assert.equal(evaluateExposure("customer-42", 100, false), false);
});
test("percentage boundaries are clamped", () => {
  assert.equal(evaluateExposure("x", 0), false);
  assert.equal(evaluateExposure("x", 100), true);
});
test("guardrail breach requests rollback", () => {
  assert.equal(assessGuardrails({ errorRate: 3, latencyP95: 200 }).decision, "ROLLBACK");
});
test("rollout stops at first failed guardrail", () => {
  const result = simulateRollout({ steps: [1, 5, 25, 50, 100], errorRate: 3, latencyP95: 200 });
  assert.equal(result.status, "ROLLED_BACK");
  assert.equal(result.results.length, 1);
  assert.equal(result.finalExposure, 0);
});
test("healthy rollout reaches final stage", () => {
  const result = simulateRollout({ steps: [1, 5, 25], errorRate: 0.5, latencyP95: 250 });
  assert.equal(result.finalExposure, 25);
});
test("rejects non-ascending rollout steps", () => {
  assert.throws(() => simulateRollout({ steps: [10, 5], errorRate: 0, latencyP95: 100 }), RangeError);
});
test("flag health identifies missing governance", () => {
  assert.equal(flagHealth({ createdAt: "2026-10-01", percentage: 10 }).health, "REVIEW");
});
