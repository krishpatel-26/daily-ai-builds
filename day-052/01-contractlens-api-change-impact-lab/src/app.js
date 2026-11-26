import {parseOpenApi} from "./core/openapi.js";
import {compareContracts} from "./core/diff.js";
import {buildAnalysisReport,reportToMarkdown} from "./core/report.js";
import {assessConsumerImpact} from "./core/impact.js";
const $=id=>document.getElementById(id);
let currentReport=null,consumers=[];
function escapeHtml(value){return String(value??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"})[c]);}
function showError(message){$("error").textContent=message;$("error").classList.remove("hidden");}
function clearError(){$("error").classList.add("hidden");}
function loadSample(){
 Promise.all([fetch("./fixtures/openapi-v1.json").then(r=>r.json()),fetch("./fixtures/openapi-v2.json").then(r=>r.json()),fetch("./fixtures/consumers.json").then(r=>r.json())]).then(([a,b,c])=>{
  $("baselineText").value=JSON.stringify(a,null,2);$("candidateText").value=JSON.stringify(b,null,2);consumers=c.consumers;
  $("baselineName").textContent="openapi-v1.json · loaded sample";$("candidateName").textContent="openapi-v2.json · loaded sample";clearError();analyze();
 }).catch(e=>showError("Could not load sample fixtures: "+e.message));
}
function renderMetrics(report){
 const s=report.summary,cards=[["TOTAL FINDINGS",s.total,"All detected contract changes","blue"],["BREAKING",s.breaking,"Requires compatibility plan","red"],["NEEDS REVIEW",s.review,"Confirm consumer behavior","amber"],["AFFECTED CONSUMERS",s.affectedConsumers,"Mapped synthetic integrations","blue"]];
 $("metrics").innerHTML=cards.map(c=>'<article class="metric panel"><small>'+c[0]+'</small><strong class="'+c[3]+'">'+c[1]+'</strong><span>'+c[2]+'</span></article>').join("");
}
function filteredFindings(){
 if(!currentReport)return [];
 const value=$("threshold").value;
 return currentReport.findings.filter(f=>value==="all"||(value==="breaking"&&f.severity==="breaking")||(value==="high"&&f.severity==="breaking"));
}
function renderFindings(){
 const rows=filteredFindings(),list=$("findingList");
 $("findingCaption").textContent=rows.length+" findings shown · "+(currentReport?.findings.length??0)+" total";
 list.classList.toggle("empty",rows.length===0);
 list.innerHTML=rows.length?rows.map(f=>'<article class="finding-card"><div class="finding-top"><div class="finding-title">'+escapeHtml(f.title)+'</div><span class="severity severity-'+f.severity+'">'+escapeHtml(f.severity.toUpperCase())+'</span></div><div class="finding-meta">'+escapeHtml(f.category)+' · '+escapeHtml(f.operation)+'</div><div class="finding-path">'+escapeHtml(f.path)+'</div><div class="finding-explain">'+escapeHtml(f.explanation)+'</div></article>').join(""):"No findings match this filter.";
}
function renderImpact(){
 const impacts=currentReport?.consumerImpacts??[];
 $("impactCaption").textContent=impacts.length+" mapped consumers affected";
 $("impactList").classList.toggle("empty",impacts.length===0);
 $("impactList").innerHTML=impacts.length?impacts.map(c=>'<article class="impact-card"><b>'+escapeHtml(c.name)+'</b><p>Owner: '+escapeHtml(c.owner)+' · '+escapeHtml(c.tier)+'</p><span class="impact-tag">'+escapeHtml(c.level.toUpperCase())+'</span><span class="impact-tag">'+c.breakingCount+' breaking</span><span class="impact-tag">'+c.reviewCount+' review</span><p>'+c.findings.map(f=>escapeHtml(f.operation)).join("<br>")+'</p></article>').join(""):"No registered consumers map to the detected findings. Verify the consumer registry before sign-off.";
}
function renderHandoff(){
 const actions=currentReport?.rolloutActions??[];
 $("handoffList").innerHTML=actions.length?"<ol>"+actions.map(a=>"<li><b>"+escapeHtml(a.priority)+" · "+escapeHtml(a.owner)+":</b> "+escapeHtml(a.action)+"</li>").join("")+"</ol>":"Run analysis to generate a checklist.";
}
function analyze(){
 clearError();
 try{
  const oldApi=parseOpenApi($("baselineText").value),newApi=parseOpenApi($("candidateText").value);
  const findings=compareContracts(oldApi,newApi);
  currentReport=buildAnalysisReport({oldApi,newApi,findings,registry:{consumers},generatedAt:new Date().toISOString()});
  renderMetrics(currentReport);renderFindings();renderImpact();renderHandoff();$("exportMarkdown").disabled=false;
 }catch(e){currentReport=null;$("exportMarkdown").disabled=true;showError(e.message);}
}
function download(name,text,type){
 const blob=new Blob([text],{type}),url=URL.createObjectURL(blob),a=document.createElement("a");a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),300);
}
$("loadSample").addEventListener("click",loadSample);
$("analyze").addEventListener("click",analyze);
$("threshold").addEventListener("change",renderFindings);
$("exportMarkdown").addEventListener("click",()=>{if(currentReport)download("contractlens-release-handoff.md",reportToMarkdown(currentReport),"text/markdown;charset=utf-8");});
$("baselineFile").addEventListener("change",async e=>{const file=e.target.files?.[0];if(!file)return;if(file.size>2_000_000){showError("Baseline JSON exceeds the 2 MB prototype limit.");return;}$("baselineText").value=await file.text();$("baselineName").textContent=file.name;});
$("candidateFile").addEventListener("change",async e=>{const file=e.target.files?.[0];if(!file)return;if(file.size>2_000_000){showError("Candidate JSON exceeds the 2 MB prototype limit.");return;}$("candidateText").value=await file.text();$("candidateName").textContent=file.name;});
loadSample();
