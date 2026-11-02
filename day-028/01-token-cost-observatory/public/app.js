const $ = id => document.getElementById(id);
const money = n => "$" + Number(n).toFixed(4);
async function api(url, options) { const r = await fetch(url,options); const data = await r.json(); if (!r.ok) throw new Error(data.error || "Request failed"); return data; }
function metric(label,value,note){return `<article class="metric"><small>${label}</small><strong>${value}</strong><em>${note}</em></article>`;}
function rows(items,key){return items.length ? items.map(x=>`<div class="rowline"><div><b>${x[key]}</b><small>${x.requests} requests · ${x.unpriced ? x.unpriced+" unpriced" : "priced usage"}</small></div><b>${money(x.cost)}</b></div>`).join("") : "<p>No usage yet.</p>";}
async function refresh(){
 const d=await api("/api/analytics"),s=d.summary;
 $("metrics").innerHTML=metric("TOTAL ESTIMATED SPEND",money(s.totalCost),"Across priced events")+metric("TOTAL TOKENS",s.totalTokens.toLocaleString(),s.inputTokens.toLocaleString()+" input · "+s.outputTokens.toLocaleString()+" output")+metric("API REQUESTS",s.requests.toLocaleString(),s.unpricedRequests+" unpriced model events")+metric("AVERAGE COST / REQUEST",money(s.averageCostPerRequest),"Priced requests only");
 const max=Math.max(0.000001,...d.byDay.map(x=>x.cost));
 $("dailyChart").innerHTML=d.byDay.map(x=>`<div class="barwrap"><b>${money(x.cost)}</b><div class="bar" style="height:${Math.max(3,x.cost/max*100)}%"></div><small>${x.date.slice(5)}</small></div>`).join("") || "No data";
 const pct=Math.min(100,Math.max(0,s.budgetUsedPct));
 $("budgetHealth").innerHTML=`<div class="health">${pct.toFixed(1)}%</div><small>${money(s.totalCost)} spent of ${money(s.monthlyBudget)}</small><div class="track" style="margin:16px 0"><span style="width:${pct}%"></span></div><div class="rowline"><span>Remaining budget</span><b class="ok">${money(s.budgetRemaining)}</b></div>`;
 $("models").innerHTML=rows(d.byModel,"model"); $("projects").innerHTML=rows(d.byProject,"project");
 $("alerts").innerHTML=d.alerts.length?d.alerts.map(a=>`<div class="alert ${a.level}"><b>${a.level.toUpperCase()}</b> · ${a.message}</div>`).join(""):'<div class="alert"><b class="ok">ALL CLEAR</b> · No budget or data quality alerts.</div>';
 $("budget").value=s.monthlyBudget;
}
$("saveBudget").onclick=async()=>{try{await api("/api/budget",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({monthlyBudget:Number($("budget").value)})});await refresh();}catch(e){alert(e.message)}};
$("addEvent").onclick=async()=>{try{const event=JSON.parse($("eventInput").value);const result=await api("/api/events",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(event)});$("ingestStatus").textContent="Added "+result.added+" event(s).";await refresh();}catch(e){$("ingestStatus").textContent=e.message;}};
refresh().catch(e=>$("alerts").textContent=e.message);