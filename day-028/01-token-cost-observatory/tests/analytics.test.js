const test = require("node:test");
const assert = require("node:assert/strict");
const { estimateCost, normalizeEvent, analyzeUsage } = require("../src/analytics");
test("estimates model cost per million tokens",()=>{assert.equal(estimateCost({model:"gpt-4.1-mini",inputTokens:1000000,outputTokens:0}),0.4);});
test("returns null for models without configured pricing",()=>{assert.equal(estimateCost({model:"custom",inputTokens:100,outputTokens:10}),null);});
test("rejects negative token counts",()=>{assert.throws(()=>normalizeEvent({model:"gpt-4.1-mini",inputTokens:-1,outputTokens:2}),/non-negative/);});
test("aggregates spend, tokens and budget",()=>{const a=analyzeUsage([{model:"gpt-4.1-mini",project:"demo",inputTokens:1000000,outputTokens:0,timestamp:"2026-11-02T10:00:00Z"}],{monthlyBudget:10});assert.equal(a.summary.totalCost,0.4);assert.equal(a.summary.totalTokens,1000000);assert.equal(a.summary.budgetRemaining,9.6);});
test("flags budget threshold and unknown pricing",()=>{const a=analyzeUsage([{model:"gpt-4.1",inputTokens:50000000,outputTokens:0},{model:"mystery",inputTokens:1,outputTokens:1}],{monthlyBudget:50});assert.ok(a.alerts.some(x=>x.level==="warning"));assert.ok(a.alerts.some(x=>x.level==="info"));});