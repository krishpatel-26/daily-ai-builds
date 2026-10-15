import {normalizeSignal,scoreSignal,priorityLabel,summarize,accountBrief} from "./src/domain.js";
import {loadSignals,saveSignals} from "./src/storage.js";
import {followupDraft} from "./src/followup.js";
import {DEMO_SIGNALS} from "./src/demo-data.js";
const $=id=>document.getElementById(id);let signals=loadSignals(),selected=null,briefText="",draftText="",toastTimer;
const esc=v=>String(v).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
function toast(s){$("toast").textContent=s;$("toast").classList.add("show");clearTimeout(toastTimer);toastTimer=setTimeout(()=>$("toast").classList.remove("show"),2200)}
function persist(){if(!saveSignals(signals).ok)toast("Could not save locally. Export a backup.");}
function render(){const sum=summarize(signals);$("openCount").textContent=sum.open;$("highCount").textContent=sum.high;$("blockerCount").textContent=sum.blockers;$("doneCount").textContent=sum.done;
const q=$("search").value.toLowerCase().trim(),filter=$("filter").value,sort=$("sort").value;let rows=signals.filter(s=>(s.account+" "+s.evidence+" "+s.action+" "+s.owner).toLowerCase().includes(q));
rows=rows.filter(s=>filter==="all"||(filter==="blocker"&&s.type==="blocker")||(filter==="high"&&s.stage==="open"&&scoreSignal(s)>=60)||(filter==="open"&&s.stage==="open")||(filter==="done"&&s.stage==="done"));
rows.sort((a,b)=>sort==="recent"?b.createdAt.localeCompare(a.createdAt):sort==="account"?a.account.localeCompare(b.account):scoreSignal(b)-scoreSignal(a));
$("signalList").innerHTML=rows.map(s=>`<article class="signal ${selected===s.id?"selected":""}" data-id="${esc(s.id)}" tabindex="0"><div class="signal-bar ${esc(s.severity)}"></div><div class="signal-main"><div class="signal-meta"><span class="tag ${esc(s.type)}">${esc(s.type)}</span><span>${esc(s.severity.toUpperCase())} SEVERITY</span><span>OWNER: ${esc(s.owner)}</span></div><h3>${esc(s.account)}</h3><p>${esc(s.evidence)}</p><div class="signal-next"><b>NEXT:</b> ${esc(s.action)}</div></div><div class="signal-side"><span class="priority">${esc(priorityLabel(s))}</span><button data-complete="${esc(s.id)}">${s.stage==="done"?"Reopen":"Mark done"}</button></div></article>`).join("");
$("empty").hidden=rows.length>0;updatePanels();}
function updatePanels(){const s=signals.find(x=>x.id===selected);briefText=s?accountBrief(s):"";draftText="";$("brief").textContent=briefText||"Select a signal from the field log.";$("brief").classList.toggle("emptybrief",!s);$("draft").textContent="No follow-up drafted yet.";$("copyBrief").disabled=!s;$("makeDraft").disabled=!s||s.stage==="done";$("copyDraft").disabled=true;}
function openDialog(){$("form").reset();$("dialog").showModal()}
function closeDialog(){$("dialog").close()}
$("newBtn").onclick=openDialog;$("emptyNew").onclick=openDialog;$("close").onclick=closeDialog;$("cancel").onclick=closeDialog;
$("form").addEventListener("submit",e=>{e.preventDefault();try{const s=normalizeSignal({account:$("account").value,type:$("type").value,severity:$("severity").value,owner:$("owner").value,evidence:$("evidence").value,action:$("action").value,due:$("due").value,stage:$("stage").value});signals.unshift(s);selected=s.id;persist();render();closeDialog();toast("Signal captured. Next action recorded.");}catch(err){toast(err.message)}});
$("signalList").addEventListener("click",e=>{const done=e.target.closest("[data-complete]");if(done){e.stopPropagation();const s=signals.find(x=>x.id===done.dataset.complete);if(s){s.stage=s.stage==="done"?"open":"done";persist();render();toast(s.stage==="done"?"Marked complete.":"Signal reopened.");}return;}const card=e.target.closest(".signal");if(card){selected=card.dataset.id;render();}});
$("signalList").addEventListener("keydown",e=>{if((e.key==="Enter"||e.key===" ")&&e.target.classList.contains("signal")){e.preventDefault();selected=e.target.dataset.id;render();}});
["search","filter","sort"].forEach(id=>$(id).addEventListener(id==="search"?"input":"change",render));
async function copy(text){try{await navigator.clipboard.writeText(text);toast("Copied to clipboard.");}catch{const t=document.createElement("textarea");t.value=text;document.body.append(t);t.select();document.execCommand("copy");t.remove();toast("Copied to clipboard.");}}
$("copyBrief").onclick=()=>briefText&&copy(briefText);
$("makeDraft").onclick=()=>{const s=signals.find(x=>x.id===selected);if(!s)return;try{draftText=followupDraft(s);$("draft").textContent=draftText;$("copyDraft").disabled=false;toast("Draft created. Review before sending.");}catch(e){toast(e.message)}};
$("copyDraft").onclick=()=>draftText&&copy(draftText);
$("exportBtn").onclick=()=>download("fieldops-signals.json",JSON.stringify(signals,null,2));
function download(name,text){const a=document.createElement("a"),url=URL.createObjectURL(new Blob([text],{type:"application/json"}));a.href=url;a.download=name;a.click();URL.revokeObjectURL(url);toast("Export prepared.");}
$("importFile").addEventListener("change",async e=>{const f=e.target.files?.[0];if(!f)return;try{const parsed=JSON.parse(await f.text());if(!Array.isArray(parsed))throw new Error("JSON must contain a list of signals.");const validated=parsed.map(x=>normalizeSignal(x));const ids=new Set(signals.map(x=>x.id));const fresh=validated.filter(x=>!ids.has(x.id));signals=[...fresh,...signals];persist();render();toast("Imported "+fresh.length+" new signal(s).");}catch(err){toast("Import failed: "+err.message)}finally{e.target.value="";}});
$("loadDemo").onclick=()=>{const ids=new Set(signals.map(x=>x.id));signals=[...DEMO_SIGNALS.filter(x=>!ids.has(x.id)),...signals];persist();render();toast("Synthetic examples loaded.");};
render();