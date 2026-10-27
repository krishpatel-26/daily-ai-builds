import { sampleEvents } from "./core/sample-events.js";
import { createMemoryStore } from "./core/storage.js";
import { validateEvent } from "./core/validate-event.js";
import { classifyFailure } from "./core/triage.js";
import { retryDecision, retryDelayMs } from "./core/retry-policy.js";
import { findDuplicateKeys, hasPriorSuccessfulDelivery } from "./core/idempotency.js";
import { summarizeHealth } from "./core/health-score.js";
import { filterEvents } from "./core/filter-events.js";
import { formatRelativeAge, formatDuration, safeFileName } from "./core/format.js";
import { buildIncidentReport, reportToMarkdown } from "./core/incident-report.js";
const store=createMemoryStore(sampleEvents); let selectedId="evt_8a34"; let toastTimer;
const $=(selector)=>document.querySelector(selector);
function escapeHtml(value){return String(value??"").replace(/[&<>"']/g,(char)=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"})[char]);}
function statusLabel(status){return ({delivered:"Delivered",failed:"Failed",retrying:"Retrying","dead-letter":"Dead letter"})[status]??status;}
function statusClass(status){return "state state-"+status;}
function showToast(message){document.querySelector(".toast")?.remove();const node=document.createElement("div");node.className="toast";node.textContent=message;document.body.append(node);clearTimeout(toastTimer);toastTimer=setTimeout(()=>node.remove(),2600);}
function renderMetrics(){
 const events=store.all(),metrics=summarizeHealth(events),duplicateCount=findDuplicateKeys(events).length;
 const cards=[["Delivery health",metrics.healthScore+"/100","Heuristic score · sample only","metric-accent"],["Success rate",metrics.successRate+"%",metrics.delivered+" successful attempts","metric-accent"],["Needs attention",String(metrics.failed),metrics.deadLetter+" in dead letter","metric-danger"],["Duplicate keys",String(duplicateCount),"Key groups with multiple attempts","metric-warn"]];
 $("#metrics").innerHTML=cards.map((item)=>'<article class="metric-card"><div class="metric-label">'+item[0]+'</div><div class="metric-number '+item[3]+'">'+item[1]+'</div><div class="metric-foot">'+item[2]+'</div></article>').join("");
}
function renderEvents(){
 const events=filterEvents(store.all(),{status:$("#statusFilter").value,query:$("#searchInput").value});
 $("#eventsBody").innerHTML=events.map((event)=>{
  const selected=event.id===selectedId?" selected":"";
  return '<tr class="event-row'+selected+'" data-id="'+escapeHtml(event.id)+'" tabindex="0" aria-selected="'+(event.id===selectedId)+'"><td><div class="event-name">'+escapeHtml(event.eventType)+'</div><div class="event-sub">'+escapeHtml(event.id)+' · '+escapeHtml(event.customer)+'</div></td><td><div class="destination" title="'+escapeHtml(event.endpoint)+'">'+escapeHtml(new URL(event.endpoint).host)+'</div><div class="event-sub">'+escapeHtml(event.httpStatus??"—")+' · '+escapeHtml(event.requestId)+'</div></td><td>Attempt '+event.attempt+'</td><td><span class="'+statusClass(event.status)+'">'+statusLabel(event.status)+'</span></td><td>'+formatRelativeAge(event.createdAt)+'</td></tr>';
 }).join("");
 $("#resultCount").textContent=events.length+" of "+store.all().length+" attempts";$("#emptyState").classList.toggle("hidden",events.length!==0);
}
function renderDetail(){
 const event=store.get(selectedId),panel=$("#detailPanel");
 if(!event){panel.innerHTML='<div class="panel-heading"><div><h2>Delivery evidence</h2><p>Choose a visible attempt to inspect.</p></div></div><div class="detail-empty"><div class="empty-icon">⌁</div><strong>No selection</strong><p>Change filters or reset the demo dataset.</p></div>';return;}
 const triage=classifyFailure(event),decision=retryDecision(event),duplicate=findDuplicateKeys(store.all()).find((group)=>group.key===event.idempotencyKey),deliveredDuplicate=hasPriorSuccessfulDelivery(store.all(),event),validation=validateEvent(event);
 const timeline=(event.timeline??[]).map((entry)=>'<div class="timeline-item"><span class="timeline-marker"></span><span>'+escapeHtml(entry)+'</span></div>').join("");
 panel.innerHTML='<div class="panel-heading"><div><h2>Delivery evidence</h2><p>Inspect this attempt and its next action.</p></div><span class="tag">'+escapeHtml(triage.severity.toUpperCase())+'</span></div>'+
 '<div class="detail-body"><div class="detail-headline"><div><div class="detail-id">'+escapeHtml(event.id)+'</div><div class="event-sub">'+escapeHtml(event.eventType)+' · '+escapeHtml(event.customer)+'</div></div><span class="'+statusClass(event.status)+'">'+statusLabel(event.status)+'</span></div>'+
 '<div class="detail-section"><div class="section-label">OBSERVED ERROR</div><div class="error-box">'+escapeHtml(event.error||(event.status==="delivered"?"No error recorded for this successful attempt.":"No provider response body was captured."))+'</div><div class="fact-row"><span>HTTP status</span><strong>'+escapeHtml(event.httpStatus??"Not captured")+'</strong></div><div class="fact-row"><span>Response latency</span><strong>'+(event.latencyMs==null?"Not captured":formatDuration(event.latencyMs))+'</strong></div><div class="fact-row"><span>Request ID</span><strong>'+escapeHtml(event.requestId||"Not captured")+'</strong></div></div>'+
 '<div class="detail-section"><div class="section-label">IDEMPOTENCY CHECK</div><div class="fact-row"><span>Key</span><strong>'+escapeHtml(event.idempotencyKey||"Missing")+'</strong></div><div class="fact-row"><span>Other attempts with key</span><strong>'+(duplicate?duplicate.eventIds.length-1:0)+'</strong></div><div class="fact-row"><span>Prior success found</span><strong>'+(deliveredDuplicate?"Yes — review before replay":"No in this sample")+'</strong></div></div>'+
 '<div class="detail-section"><div class="section-label">TRIAGE / '+escapeHtml(triage.category.toUpperCase())+'</div><div class="action-callout">'+escapeHtml(triage.action)+'</div><div class="fact-row"><span>Retry recommendation</span><strong>'+(decision.retry?"Allowed by demo policy":"Blocked by demo policy")+'</strong></div><div class="fact-row"><span>Next backoff</span><strong>'+(retryDelayMs(event.attempt)==null?"Attempt ceiling":formatDuration(retryDelayMs(event.attempt)))+'</strong></div><div class="fact-row"><span>Envelope validation</span><strong>'+(validation.valid?"Passed":validation.errors.length+" issue(s)")+'</strong></div></div>'+
 '<div class="detail-section"><div class="section-label">ATTEMPT TIMELINE</div>'+(timeline||'<p class="event-sub">No timeline entries captured.</p>')+'</div>'+
 '<div class="detail-actions"><button class="button button-primary" id="simulateReplay" '+(!decision.retry?"disabled":"")+'>Simulate retry</button><button class="button button-secondary" id="copyEvidence">Copy evidence JSON</button></div><p class="event-sub">Simulated actions change only in-memory demo state. No network request is sent.</p></div>';
 $("#simulateReplay")?.addEventListener("click",simulateRetry);$("#copyEvidence")?.addEventListener("click",copyEvidence);
}
function render(){renderMetrics();renderEvents();renderDetail();}
function simulateRetry(){
 const event=store.get(selectedId);if(!event)return;const decision=retryDecision(event);
 if(!decision.retry){showToast("Retry blocked: "+decision.reason);return;}
 store.update(event.id,{attempt:event.attempt+1,status:"delivered",httpStatus:200,latencyMs:173,failureType:"none",error:"",requestId:"req_sim_"+event.id.replace(/[^a-z0-9]/gi,"")+"_"+(event.attempt+1),timeline:[...(event.timeline??[]),"Local demo: retry simulated","Local demo: synthetic HTTP 200 returned"]});
 render();showToast("Local retry simulated — no endpoint was contacted.");
}
async function copyEvidence(){
 const event=store.get(selectedId);if(!event)return;
 try{await navigator.clipboard.writeText(JSON.stringify({event,triage:classifyFailure(event),validation:validateEvent(event),duplicateKeys:findDuplicateKeys(store.all())},null,2));showToast("Evidence JSON copied.");}
 catch{showToast("Clipboard unavailable. Export the handoff report instead.");}
}
function exportReport(){
 const report=buildIncidentReport(store.all());const blob=new Blob([reportToMarkdown(report)],{type:"text/markdown;charset=utf-8"});
 const url=URL.createObjectURL(blob),anchor=document.createElement("a");anchor.href=url;anchor.download=safeFileName("webhook-incident-handoff")+".md";anchor.click();URL.revokeObjectURL(url);showToast("Incident handoff exported.");
}
function showRunbook(){
 $("#runbookContent").innerHTML='<h3>1. Confirm the symptom</h3><ul><li>Capture event ID, request ID, destination and UTC timestamp.</li><li>Compare response status and latency with destination logs.</li></ul><h3>2. Classify before retrying</h3><ul><li>Timeout / 5xx: check destination health and bounded retry policy.</li><li>401 / 403: resolve credentials or authorization first.</li><li>422 / 400: repair the payload contract; do not replay unchanged.</li><li>429: honor Retry-After and use bounded backoff.</li></ul><h3>3. Protect side effects</h3><ul><li>Check if the same idempotency key has already succeeded.</li><li>Verify receiver deduplication before replaying payment or order events.</li><li>Do not blindly retry dead-lettered or irreversible operations.</li></ul><h3>4. Create a handoff</h3><ul><li>Export evidence and redact sensitive values.</li><li>Record an owner, customer impact, mitigation and next update time.</li></ul>';
 $("#runbookDialog").showModal();
}
$("#statusFilter").addEventListener("change",renderEvents);$("#searchInput").addEventListener("input",renderEvents);
$("#eventsBody").addEventListener("click",(event)=>{const row=event.target.closest("tr[data-id]");if(!row)return;selectedId=row.dataset.id;renderEvents();renderDetail();});
$("#eventsBody").addEventListener("keydown",(event)=>{if(event.key!=="Enter"&&event.key!==" ")return;const row=event.target.closest("tr[data-id]");if(!row)return;event.preventDefault();selectedId=row.dataset.id;renderEvents();renderDetail();});
$("#exportReport").addEventListener("click",exportReport);$("#showRunbook").addEventListener("click",showRunbook);
$("#resetDemo").addEventListener("click",()=>{store.reset(sampleEvents);selectedId="evt_8a34";$("#statusFilter").value="all";$("#searchInput").value="";render();showToast("Demo data reset.");});
render();
