import { scenarios, getScenario } from "./data/scenarios.js";
import { simulateAll } from "./core/simulate.js";
import { summarizeResults, compareAlgorithms } from "./core/metrics.js";
import { defaultPolicy } from "./core/policies.js";
import { validatePolicy } from "./core/validate-config.js";
import { formatRetryAfter } from "./core/retry-after.js";
import { buildQuotaReport, reportToMarkdown } from "./core/report.js";
import { formatMs, percent, safeFileName } from "./core/format.js";
const $=(id)=>document.getElementById(id);
let activeScenario=scenarios[0],policy={...defaultPolicy},results=simulateAll(activeScenario.traffic,policy),selectedIndex=0,activeAlgorithm="slidingWindow";
function escapeHtml(value){return String(value??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"})[c]);}
function labelAlgorithm(key){return ({fixedWindow:"Fixed window",slidingWindow:"Sliding window",tokenBucket:"Token bucket"})[key]??key;}
function decisionMarkup(item){return item.allowed?'<span class="decision allow">Allowed</span>':'<span class="decision limited">HTTP 429</span>';}
function renderMetrics(){
 const summary=summarizeResults(results[activeAlgorithm]),comparison=compareAlgorithms(results);
 const cards=[["Requests in replay",summary.total,"Synthetic requests", "blue"],["Allowed",summary.allowed,percent(summary.allowed,summary.total)+" accepted","green"],["Rate limited",summary.limited,percent(summary.limited,summary.total)+" returned 429","red"],["Retry wait",formatMs(summary.totalRetryAfterMs),"Sum of estimated waits","amber"]];
 $("metricGrid").innerHTML=cards.map(c=>'<article class="metric-card"><div class="metric-label">'+c[0]+'</div><div class="metric-value '+c[3]+'">'+c[1]+'</div><div class="metric-foot">'+c[2]+'</div></article>').join("");
 $("algoGrid").innerHTML=Object.entries(results).map(([key,items])=>{
  const s=summarizeResults(items),share=summary.total?Math.round(s.allowed/summary.total*100):0;
  return '<article class="algo-card"><div class="algo-title"><h2>'+labelAlgorithm(key)+'</h2><span class="algo-chip">'+(key==="fixedWindow"?"COUNTER":key==="slidingWindow"?"ROLLING LOG":"REFILLING TOKENS")+'</span></div><div class="algo-stat-row"><span class="algo-big">'+s.limited+' <small class="red">429s</small></span><span class="algo-stat-label">'+s.allowed+' allowed</span></div><div class="progress"><span style="width:'+share+'%"></span></div><div class="algo-footer"><span>'+share+'% accepted</span><span>Retry wait '+formatMs(s.totalRetryAfterMs)+'</span></div></article>';
 }).join("");
}
function renderLedger(){
 const query=$("searchInput").value.toLowerCase().trim(),filter=$("decisionFilter").value;
 const rows=activeScenario.traffic.map((request,index)=>({request,index})).filter(({request,index})=>{
  const chosen=results[activeAlgorithm][index];
  const statusOk=filter==="all"||(filter==="allowed"&&chosen.allowed)||(filter==="limited"&&!chosen.allowed);
  const text=[request.id,request.clientId,request.route,request.label].join(" ").toLowerCase();
  return statusOk&&(!query||text.includes(query));
 });
 $("ledgerBody").innerHTML=rows.map(({request,index})=>{
  const fixed=results.fixedWindow[index],sliding=results.slidingWindow[index],bucket=results.tokenBucket[index];
  return '<tr class="request-row'+(index===selectedIndex?" selected":"")+'" data-index="'+index+'" tabindex="0" aria-selected="'+(index===selectedIndex)+'"><td><div class="req-id">'+escapeHtml(request.id)+'</div><div class="sub">'+escapeHtml(request.label??"Request")+' · '+request.atMs+' ms</div></td><td><b>'+escapeHtml(request.clientId)+'</b><div class="sub">'+escapeHtml(request.route)+'</div></td><td>'+decisionMarkup(fixed)+'<div class="sub">'+fixed.remaining+' remaining</div></td><td>'+decisionMarkup(sliding)+'<div class="sub">'+sliding.remaining+' remaining</div></td><td>'+decisionMarkup(bucket)+'<div class="sub">'+bucket.remaining+' remaining</div></td></tr>';
 }).join("");
 $("ledgerCaption").textContent=rows.length+" of "+activeScenario.traffic.length+" requests · "+labelAlgorithm(activeAlgorithm)+" selected for filtering";
 $("emptyState").classList.toggle("hidden",rows.length>0);
}
function renderDetail(){
 const request=activeScenario.traffic[selectedIndex];if(!request){$("detailPanel").innerHTML='<div class="panel-head"><h2>Decision evidence</h2></div><div class="detail-empty">No request selected.</div>';return;}
 const result=results[activeAlgorithm][selectedIndex],retryText=result.allowed?"No retry needed":"Retry after approximately "+formatRetryAfter(result.retryAfterMs);
 const comparison=Object.entries(results).map(([key,items])=>labelAlgorithm(key)+": "+(items[selectedIndex].allowed?"allowed":"429")).join(" · ");
 $("detailPanel").innerHTML='<div class="panel-head"><div><h2>Decision evidence</h2><p>'+labelAlgorithm(activeAlgorithm)+' · request '+escapeHtml(request.id)+'</p></div></div><div class="detail-body"><div class="detail-event-head"><div><b>'+escapeHtml(request.label??request.route)+'</b><div class="sub">'+escapeHtml(request.clientId)+' · '+escapeHtml(request.route)+'</div></div><span class="detail-state">'+(result.allowed?"HTTP 200":"HTTP 429")+'</span></div><div class="facts"><div class="fact"><span>Configured limit</span><b>'+result.limit+' requests</b></div><div class="fact"><span>Remaining quota</span><b>'+result.remaining+'</b></div><div class="fact"><span>Estimated reset</span><b>'+formatMs(result.resetAtMs-request.atMs)+'</b></div><div class="fact"><span>Retry-After</span><b>'+formatRetryAfter(result.retryAfterMs)+'</b></div></div><div class="reason-box"><b>Decision</b><br>'+escapeHtml(result.reason)+'<br><br><b>Retry posture</b><br>'+escapeHtml(retryText)+'<br><br><b>Algorithm comparison</b><br>'+escapeHtml(comparison)+'</div><div class="export-list"><button class="mini-btn" id="exportRequest">Export request JSON</button><button class="mini-btn" id="chooseFixed">Inspect fixed window</button><button class="mini-btn" id="chooseSliding">Inspect sliding window</button><button class="mini-btn" id="chooseBucket">Inspect token bucket</button></div></div>';
 $("exportRequest").addEventListener("click",()=>downloadText("quota-request-"+request.id+".json",JSON.stringify({request,policy,results:Object.fromEntries(Object.entries(results).map(([k,v])=>[k,v[selectedIndex]]))},null,2),"application/json"));
 $("chooseFixed").addEventListener("click",()=>setAlgorithm("fixedWindow"));$("chooseSliding").addEventListener("click",()=>setAlgorithm("slidingWindow"));$("chooseBucket").addEventListener("click",()=>setAlgorithm("tokenBucket"));
}
function render(){renderMetrics();renderLedger();renderDetail();}
function setAlgorithm(key){activeAlgorithm=key;render();}
function runSimulation(){
 const nextPolicy={limit:Number($("limitInput").value),windowMs:Number($("windowInput").value)*1000};
 const errors=validatePolicy(nextPolicy);
 if(errors.length){alert("Invalid policy:\n"+errors.join("\n"));return;}
 policy=nextPolicy;activeScenario=getScenario($("scenarioSelect").value)??scenarios[0];results=simulateAll(activeScenario.traffic,policy);selectedIndex=0;render();
}
function downloadText(name,text,type){const blob=new Blob([text],{type});const url=URL.createObjectURL(blob);const a=document.createElement("a");a.href=url;a.download=safeFileName(name);a.click();setTimeout(()=>URL.revokeObjectURL(url),250);}
function exportReport(){
 const report=buildQuotaReport({scenario:activeScenario,policy,results,generatedAt:new Date().toISOString()});
 downloadText("quota-incident-handoff.md",reportToMarkdown(report),"text/markdown;charset=utf-8");
}
function exportJson(){
 const report=buildQuotaReport({scenario:activeScenario,policy,results,generatedAt:new Date().toISOString()});
 downloadText("quota-evidence.json",JSON.stringify(report,null,2),"application/json");
}
function openGuide(title,html){$("dialogTitle").textContent=title;$("dialogBody").innerHTML=html;$("infoDialog").showModal();}
function openPolicy(){openGuide("Policy configuration",'<h3>Current policy</h3><p>Limit: '+policy.limit+' request units per '+(policy.windowMs/1000)+' seconds.</p><p>The selected values are applied only to the synthetic replay. All three algorithms consume the same configured limit and time horizon, but their admission behavior differs.</p><h3>Production caveats</h3><ul><li>Choose a quota key based on authenticated client identity and route scope.</li><li>Define whether cost means request count or weighted units.</li><li>For multi-instance services, use atomic shared state and explicit clock assumptions.</li><li>Expose provider-specific remaining/reset headers only if their semantics are known.</li></ul>');}
function openRunbook(){openGuide("HTTP 429 incident runbook",'<h3>1. Scope the impact</h3><ul><li>Capture client, endpoint, request ID, window and timestamps.</li><li>Check whether the limit is per client, per route, per credential or account-wide.</li></ul><h3>2. Distinguish throttling from outage</h3><ul><li>429 usually indicates quota pressure; inspect provider response headers and documentation.</li><li>Do not blindly retry in a tight loop. Honor a valid Retry-After signal.</li><li>Use bounded exponential backoff with jitter when the provider has no more specific instruction.</li></ul><h3>3. Verify the policy</h3><ul><li>Compare burst patterns with fixed/sliding window or token-bucket semantics.</li><li>Check whether concurrent instances share atomic state.</li><li>Look for retry amplification and clients that ignore backoff.</li></ul><h3>4. Handoff</h3><ul><li>Export the scenario and per-algorithm evidence.</li><li>Redact API keys and customer data.</li><li>Record mitigation, owner and next update time.</li></ul>');}
for(const scenario of scenarios){const option=document.createElement("option");option.value=scenario.id;option.textContent=scenario.name;$("scenarioSelect").append(option);}
$("scenarioSelect").value=activeScenario.id;
$("runSimulation").addEventListener("click",runSimulation);$("exportReport").addEventListener("click",exportReport);
$("exportReport").insertAdjacentHTML("afterend",' <button class="mini-btn" id="exportJson">Export JSON</button>');
$("exportJson").addEventListener("click",exportJson);$("openPolicy").addEventListener("click",openPolicy);$("openRunbook").addEventListener("click",openRunbook);
$("decisionFilter").addEventListener("change",renderLedger);$("searchInput").addEventListener("input",renderLedger);
$("ledgerBody").addEventListener("click",e=>{const row=e.target.closest("tr[data-index]");if(!row)return;selectedIndex=Number(row.dataset.index);renderLedger();renderDetail();});
$("ledgerBody").addEventListener("keydown",e=>{if(!["Enter"," "].includes(e.key))return;const row=e.target.closest("tr[data-index]");if(!row)return;e.preventDefault();selectedIndex=Number(row.dataset.index);renderLedger();renderDetail();});
render();
