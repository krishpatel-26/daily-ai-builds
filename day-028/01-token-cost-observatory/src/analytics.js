const DEFAULT_PRICING = {
  "gpt-4.1-mini": { input: 0.40, output: 1.60 },
  "gpt-4.1": { input: 2.00, output: 8.00 },
  "claude-3-5-sonnet": { input: 3.00, output: 15.00 },
  "gemini-2.5-flash": { input: 0.30, output: 2.50 }
};

function estimateCost(event, pricing = DEFAULT_PRICING) {
  const rates = pricing[event.model];
  if (!rates) return null;
  const input = Number(event.inputTokens);
  const output = Number(event.outputTokens);
  if (!Number.isFinite(input) || !Number.isFinite(output) || input < 0 || output < 0) {
    throw new Error("Token counts must be non-negative numbers");
  }
  return (input * rates.input + output * rates.output) / 1_000_000;
}

function normalizeEvent(event, pricing = DEFAULT_PRICING) {
  if (!event || typeof event !== "object") throw new Error("Usage event must be an object");
  const model = String(event.model || "").trim();
  const project = String(event.project || "unassigned").trim();
  if (!model) throw new Error("model is required");
  const cost = estimateCost({ ...event, model }, pricing);
  return {
    id: String(event.id || ""),
    timestamp: event.timestamp || new Date().toISOString(),
    project,
    provider: String(event.provider || "unknown"),
    model,
    inputTokens: Number(event.inputTokens),
    outputTokens: Number(event.outputTokens),
    cost,
    priced: cost !== null
  };
}

function analyzeUsage(events, { monthlyBudget = 100, pricing = DEFAULT_PRICING } = {}) {
  const normalized = events.map(e => normalizeEvent(e, pricing));
  const priced = normalized.filter(e => e.priced);
  const totalCost = priced.reduce((sum, e) => sum + e.cost, 0);
  const inputTokens = normalized.reduce((sum, e) => sum + e.inputTokens, 0);
  const outputTokens = normalized.reduce((sum, e) => sum + e.outputTokens, 0);
  const byModel = {};
  const byProject = {};
  const byDay = {};
  for (const e of normalized) {
    const model = byModel[e.model] ||= { model: e.model, requests: 0, inputTokens: 0, outputTokens: 0, cost: 0, unpriced: 0 };
    model.requests++; model.inputTokens += e.inputTokens; model.outputTokens += e.outputTokens;
    if (e.priced) model.cost += e.cost; else model.unpriced++;
    const project = byProject[e.project] ||= { project: e.project, requests: 0, cost: 0, unpriced: 0 };
    project.requests++; if (e.priced) project.cost += e.cost; else project.unpriced++;
    const day = e.timestamp.slice(0, 10);
    const daily = byDay[day] ||= { date: day, requests: 0, cost: 0 };
    daily.requests++; if (e.priced) daily.cost += e.cost;
  }
  const budgetUsedPct = monthlyBudget > 0 ? totalCost / monthlyBudget * 100 : 0;
  const latest = [...priced].sort((a,b) => b.timestamp.localeCompare(a.timestamp)).slice(0, 1)[0];
  const previousCosts = Object.values(byDay).sort((a,b) => a.date.localeCompare(b.date)).slice(0, -1).map(d => d.cost);
  const baseline = previousCosts.length ? previousCosts.reduce((a,b) => a+b, 0) / previousCosts.length : 0;
  const latestDayCost = latest ? (byDay[latest.timestamp.slice(0,10)]?.cost || 0) : 0;
  const anomaly = baseline > 0 && latestDayCost > baseline * 2;
  return {
    summary: { requests: normalized.length, inputTokens, outputTokens, totalTokens: inputTokens + outputTokens,
      totalCost, monthlyBudget, budgetRemaining: monthlyBudget - totalCost, budgetUsedPct,
      unpricedRequests: normalized.length - priced.length, averageCostPerRequest: priced.length ? totalCost / priced.length : 0 },
    byModel: Object.values(byModel).sort((a,b) => b.cost-a.cost),
    byProject: Object.values(byProject).sort((a,b) => b.cost-a.cost),
    byDay: Object.values(byDay).sort((a,b) => a.date.localeCompare(b.date)),
    alerts: [
      ...(budgetUsedPct >= 100 ? [{ level: "critical", message: "Monthly budget exceeded" }] : budgetUsedPct >= 80 ? [{ level: "warning", message: "At least 80% of the monthly budget has been used" }] : []),
      ...(anomaly ? [{ level: "warning", message: "Latest day's spend is more than 2× the previous daily average" }] : []),
      ...(normalized.some(e => !e.priced) ? [{ level: "info", message: "Some model usage has no configured price and is excluded from cost totals" }] : [])
    ]
  };
}

module.exports = { DEFAULT_PRICING, estimateCost, normalizeEvent, analyzeUsage };