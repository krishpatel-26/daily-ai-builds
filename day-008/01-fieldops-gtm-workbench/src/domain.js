export const TYPES=["blocker","adoption","opportunity","product","risk"];
export const SEVERITIES=["high","medium","low"];
export function normalizeSignal(input,now=new Date()){
 const account=String(input.account??"").trim(),evidence=String(input.evidence??"").trim(),action=String(input.action??"").trim(),owner=String(input.owner??"").trim();
 if(!account||!evidence||!action||!owner)throw new Error("Account, evidence, owner, and next action are required.");
 if(!TYPES.includes(input.type))throw new Error("Choose a valid signal type.");
 if(!SEVERITIES.includes(input.severity))throw new Error("Choose a valid severity.");
 return {id:String(input.id||makeId()),account,evidence,action,owner,type:input.type,severity:input.severity,due:String(input.due||""),stage:input.stage==="done"?"done":"open",createdAt:input.createdAt||now.toISOString()};
}
export function scoreSignal(s){if(s.stage==="done")return 0;return (s.severity==="high"?60:s.severity==="medium"?30:10)+(s.type==="blocker"?30:s.type==="risk"?25:s.type==="opportunity"?15:0)+(s.due&&s.due<new Date().toISOString().slice(0,10)?10:0);}
export function priorityLabel(s){const score=scoreSignal(s);return score>=80?"P1 · Urgent":score>=45?"P2 · High":score>0?"P3 · Monitor":"Completed";}
export function summarize(signals){return {open:signals.filter(s=>s.stage==="open").length,high:signals.filter(s=>s.stage==="open"&&scoreSignal(s)>=60).length,blockers:signals.filter(s=>s.stage==="open"&&s.type==="blocker").length,done:signals.filter(s=>s.stage==="done").length};}
export function accountBrief(s){return ["ACCOUNT: "+s.account,"SIGNAL: "+s.type.toUpperCase()+" / "+s.severity.toUpperCase(),"EVIDENCE: "+s.evidence,"OWNER: "+s.owner,"NEXT ACTION: "+s.action,"DUE: "+(s.due||"Not set"),"STATUS: "+s.stage.toUpperCase(),"PRIORITY: "+priorityLabel(s),"","Decision principle: validate the customer evidence before making a product or GTM commitment."].join("\n");}
function makeId(){return globalThis.crypto?.randomUUID?.()??"signal-"+Date.now()+"-"+Math.random().toString(16).slice(2);}
