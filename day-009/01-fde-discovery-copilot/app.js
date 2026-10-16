const $ = (id) => document.getElementById(id);
const sample = `Customer wants to launch the integration in the next 6 weeks.
Their operations team currently exports CSV files manually every morning. The API authentication setup has blocked the pilot for 10 days.
The team says onboarding is confusing and they are not sure which events need to be configured. They would consider expanding to 3 more warehouses if the first site reaches 90% successful syncs.
They need a clear implementation owner, a sandbox walkthrough, and a weekly progress update. Security review must be completed before production access. The customer asked whether our product supports custom event mapping; this needs product confirmation before we promise anything.`;
const patterns = [
  {type:"Implementation blocker", terms:["blocked","blocker","error","failed","failure","integration","authentication","api","sandbox"], action:"Assign an implementation owner and reproduce the blocker", owner:"Forward-deployed engineer"},
  {type:"Adoption friction", terms:["confusing","manual","not sure","onboarding","training","workaround","exports csv"], action:"Map the current workflow and validate the smallest adoption fix", owner:"FDE + Customer success"},
  {type:"Success criterion", terms:["success","target","reach","within","launch","weeks","deadline","pilot"], action:"Convert the stated target into a measurable milestone", owner:"FDE + Customer"},
  {type:"Expansion signal", terms:["expand","expanding","more warehouses","additional sites","upgrade"], action:"Validate expansion criteria against observed product usage", owner:"GTM / Account owner"},
  {type:"Security / delivery risk", terms:["security","review","production access","compliance","risk","approval"], action:"Record the dependency and confirm its reviewer and due date", owner:"Implementation owner"},
  {type:"Product feedback", terms:["feature","custom","supports","product","requested","mapping"], action:"Verify capability with product before making a customer commitment", owner:"Product + FDE"}
];
let latest = null;
function analyzeText(text, account) {
  const clean = text.trim();
  if (clean.length < 25) throw new Error("Add at least 25 characters of notes to analyze.");
  const sentences = clean.replace(/\s+/g," ").match(/[^.!?]+[.!?]?/g) || [clean];
  const signals = [];
  for (const sentence of sentences) {
    const lower = sentence.toLowerCase();
    for (const p of patterns) {
      const hits = p.terms.filter(t => lower.includes(t));
      if (hits.length && !signals.some(s => s.evidence === sentence.trim() && s.type === p.type)) {
        signals.push({type:p.type,evidence:sentence.trim(),matchedTerms:hits});
      }
    }
  }
  const uniqueTypes = [...new Set(signals.map(s=>s.type))];
  const actions = uniqueTypes.map(type => {
    const p = patterns.find(x=>x.type===type);
    const related = signals.filter(s=>s.type===type);
    return {type,title:p.action,owner:p.owner,evidence:related.map(s=>s.evidence)};
  });
  const confidence = signals.length ? Math.min(95, Math.round(45 + Math.min(signals.length,6)*7 + Math.min(uniqueTypes.length,4)*3)) : 0;
  return {account:account.trim() || "Unnamed account", createdAt:new Date().toISOString(), signals, actions, confidence, noteLength:clean.length, method:"keyword heuristics", caveat:"Signals are candidate matches, not verified facts. Review evidence and ownership with the customer."};
}
function render(data) {
  latest=data; $("empty").hidden=true; $("results").hidden=false; $("status").textContent="DRAFT · REVIEW REQUIRED";
  $("signal-count").textContent=data.signals.length; $("action-count").textContent=data.actions.length; $("confidence").textContent=data.confidence+"%";
  $("signals").innerHTML="";
  if (!data.signals.length) $("signals").innerHTML='<div class="signal"><p>No signals matched the current keyword rules. Review the notes manually or add more context.</p></div>';
  data.signals.forEach(s=>{
    const card=document.createElement("article");card.className="signal";
    const top=document.createElement("div");top.className="signal-top";
    const tag=document.createElement("span");tag.className="tag";tag.textContent=s.type;
    const hits=document.createElement("span");hits.className="tag";hits.textContent=s.matchedTerms.slice(0,3).join(" · ");
    top.append(tag,hits);
    const evidence=document.createElement("div");evidence.className="evidence";evidence.textContent='“'+s.evidence+'”';
    card.append(top,evidence);$("signals").append(card);
  });
  $("actions").innerHTML="";
  data.actions.forEach((a,i)=>{
    const card=document.createElement("article");card.className="action";
    const num=document.createElement("span");num.className="action-num";num.textContent=String(i+1).padStart(2,"0");
    const body=document.createElement("div");const title=document.createElement("strong");title.textContent=a.title;
    const desc=document.createElement("p");desc.textContent="Suggested owner: "+a.owner+" · Validate with customer before assigning.";
    body.append(title,desc);card.append(num,body);$("actions").append(card);
  });
  $("followup-wrap").hidden=true;
}
function briefText() {
  if(!latest) return "";
  return [`FDE DISCOVERY BRIEF — ${latest.account}`,`Created: ${latest.createdAt}`,`Signals: ${latest.signals.length} | Suggested actions: ${latest.actions.length} | Heuristic confidence: ${latest.confidence}%`,"","SIGNALS",...latest.signals.map(s=>`- [${s.type}] ${s.evidence} (matched: ${s.matchedTerms.join(", ")})`),"","NEXT ACTIONS",...latest.actions.map((a,i)=>`${i+1}. ${a.title} | Suggested owner: ${a.owner}`),"",latest.caveat].join("\n");
}
function followupDraft() {
  const signals = latest.signals;
  const blockers=signals.filter(s=>s.type==="Implementation blocker"||s.type==="Security / delivery risk");
  const success=signals.filter(s=>s.type==="Success criterion");
  const adoption=signals.filter(s=>s.type==="Adoption friction");
  return `Subject: ${latest.account} — discovery recap and next steps\n\nHi team,\n\nThanks for walking us through your current workflow. I captured the following items from our conversation:\n\n${signals.slice(0,5).map(s=>"- "+s.type+": "+s.evidence).join("\n") || "- We will review the notes and confirm the key priorities."}\n\nProposed next steps:\n${latest.actions.slice(0,5).map((a,i)=>`${i+1}. ${a.title} (proposed owner: ${a.owner})`).join("\n") || "1. Confirm the primary problem and agree on a next step."}\n\n${blockers.length?"We will validate the implementation and delivery dependencies before confirming dates.\n\n":""}${success.length?"We will align on measurable success criteria and how they will be verified.\n\n":""}${adoption.length?"We will review the current workflow and identify the smallest useful onboarding improvement.\n\n":""}Please reply with any corrections, the right owners, and your preferred time for a follow-up. These are proposed actions, not confirmed commitments.\n\nBest,\n[Your name]\n\nDraft generated locally from keyword matches. Review all details before sending.`;
}
function download(name, text, type) { const blob=new Blob([text],{type});const url=URL.createObjectURL(blob);const a=document.createElement("a");a.href=url;a.download=name;a.click();URL.revokeObjectURL(url); }
$("notes").addEventListener("input",()=>{$("char-count").textContent=$("notes").value.length+" characters";});
$("load-demo").addEventListener("click",()=>{$("account").value="Northstar Logistics";$("notes").value=sample;$("char-count").textContent=sample.length+" characters";});
$("analyze").addEventListener("click",()=>{try{render(analyzeText($("notes").value,$("account").value));}catch(e){$("status").textContent="NEEDS INPUT";alert(e.message);}});
$("copy-brief").addEventListener("click",async()=>{await navigator.clipboard.writeText(briefText());$("copy-brief").textContent="Copied ✓";});
$("download-json").addEventListener("click",()=>{if(latest)download("fde-discovery-brief.json",JSON.stringify(latest,null,2),"application/json");});
$("draft-followup").addEventListener("click",()=>{if(!latest)return;$("followup").value=followupDraft();$("followup-wrap").hidden=false;$("followup").scrollIntoView({behavior:"smooth",block:"nearest"});});
$("copy-followup").addEventListener("click",async()=>{await navigator.clipboard.writeText($("followup").value);$("copy-followup").textContent="Copied ✓";});
