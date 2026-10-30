const $ = id => document.getElementById(id);
const selected = [1, 5, 25, 50, 100];
document.querySelectorAll("[data-pct]").forEach(btn => {
  btn.classList.add("active");
  btn.addEventListener("click", () => {
    document.querySelectorAll("[data-pct]").forEach(b => b.classList.toggle("active", Number(b.dataset.pct) <= Number(btn.dataset.pct)));
    selected.splice(0, selected.length, ...[1,5,25,50,100].filter(n => n <= Number(btn.dataset.pct)));
    $("cohortPct").textContent = btn.dataset.pct + "%";
    $("cohortBar").style.width = btn.dataset.pct + "%";
  });
});
function render(result) {
  $("exposure").textContent = result.finalExposure + "%";
  $("barFill").style.width = result.finalExposure + "%";
  $("status").textContent = result.status.replaceAll("_", " ");
  $("status").className = "status " + (result.status === "ROLLED_BACK" ? "bad" : "good");
  $("stageList").innerHTML = result.results.map(r => `<div class="stage ${r.safe ? "" : "fail"}"><span>${r.percentage}% exposure</span><b>${r.safe ? "✓ GUARDRAILS PASS" : "✕ ROLLBACK TRIGGERED"}</b></div>`).join("");
  $("decision").textContent = result.status === "ROLLED_BACK"
    ? "Guardrail breach detected. Exposure returns to 0%. Investigate the candidate before another rollout attempt."
    : "All simulated guardrails passed. The candidate reached the final configured stage. Review real telemetry before promoting.";
}
$("simulate").addEventListener("click", async () => {
  const input = { flagName: $("flagName").value, steps: [...selected], errorRate: Number($("errorRate").value), latencyP95: Number($("latency").value), maxErrorRate: Number($("maxError").value), maxLatencyP95: Number($("maxLatency").value) };
  try {
    const response = await fetch("/api/simulate", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(input) });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Simulation failed");
    $("metricError").textContent = input.errorRate + "%";
    $("metricLatency").textContent = input.latencyP95 + " ms";
    render(result);
  } catch (error) {
    $("decision").textContent = error.message + " — start the local server with npm start.";
  }
});
$("kill").addEventListener("click", () => {
  render({ status: "ROLLED_BACK", finalExposure: 0, results: [{ percentage: 0, safe: false }] });
  $("decision").textContent = "KILL SWITCH ACTIVATED — simulated feature exposure set to 0%. This changes only the local demo state.";
});
