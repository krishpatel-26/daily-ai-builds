export function validateInput(input) {
  const values = ["targetAvailability", "totalRequests", "failedRequests", "windowDays"];
  for (const key of values) if (!Number.isFinite(Number(input[key]))) throw new TypeError(key + " must be a finite number");
  const target = Number(input.targetAvailability), total = Number(input.totalRequests), failed = Number(input.failedRequests), days = Number(input.windowDays);
  if (target <= 0 || target >= 100) throw new RangeError("Availability target must be between 0 and 100 (exclusive)");
  if (total <= 0 || failed < 0 || failed > total || days <= 0) throw new RangeError("Request counts and window are outside valid bounds");
  return { target, total, failed, days };
}
export function calculateSlo(input) {
  const {target,total,failed,days}=validateInput(input);
  const allowedFailureRate=1-target/100, observedFailureRate=failed/total, budgetRequests=total*allowedFailureRate;
  const consumedPct=budgetRequests===0?(failed?100:0):(failed/budgetRequests)*100;
  const remainingPct=Math.max(0,100-consumedPct);
  const burnRate=allowedFailureRate===0?0:observedFailureRate/allowedFailureRate;
  const monthlyBudgetDays=30*(1-target/100), projectedBudgetDays=burnRate>0?monthlyBudgetDays/burnRate:Infinity;
  const status=consumedPct>=100?"BUDGET_EXHAUSTED":burnRate>=2?"HIGH_BURN":consumedPct>=50?"BUDGET_WARNING":"HEALTHY";
  const recommendation=status==="BUDGET_EXHAUSTED"?"Pause non-essential releases and prioritize reliability work.":status==="HIGH_BURN"?"Investigate the regression and consider slowing or pausing risky releases.":status==="BUDGET_WARNING"?"Review error-budget consumption and tighten release safeguards.":"Continue delivery while monitoring the SLO.";
  return {targetAvailability:target,observedAvailability:(1-observedFailureRate)*100,totalRequests:total,failedRequests:failed,windowDays:days,allowedFailureRatePct:allowedFailureRate*100,observedFailureRatePct:observedFailureRate*100,consumedPct,remainingPct,burnRate,projectedBudgetDays:Number.isFinite(projectedBudgetDays)?projectedBudgetDays:null,status,recommendation};
}
export function classifyBurnRate(burnRate){if(!Number.isFinite(burnRate)||burnRate<0)throw new RangeError("Burn rate must be a non-negative finite number");return burnRate>=14.4?"CRITICAL":burnRate>=6?"SEVERE":burnRate>=2?"ELEVATED":burnRate>1?"ABOVE PACE":"WITHIN PACE";}
