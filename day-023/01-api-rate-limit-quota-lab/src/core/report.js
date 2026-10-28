import { compareAlgorithms } from "./metrics.js";
import { formatRetryAfter } from "./retry-after.js";
export function buildQuotaReport({scenario,policy,results,generatedAt=new Date().toISOString()}){
 const summary=compareAlgorithms(results);
 const requests=(scenario?.traffic??[]).map((request,index)=>({request,decisions:Object.fromEntries(Object.entries(results??{}).map(([name,rows])=>[name,rows[index]]))}));
 return {schemaVersion:"1.0",generatedAt,scope:"synthetic-local-simulation",disclaimer:"Simulated algorithm output; not a provider-confirmed quota or live API response.",scenario:{id:scenario?.id??"unknown",name:scenario?.name??"Unknown scenario"},policy:{limit:policy.limit,windowMs:policy.windowMs},summary,requests};
}
function cell(value){return String(value??"").replace(/\|/g,"\\|").replace(/[\r\n]+/g," ").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
export function reportToMarkdown(report){
 const rows=report.requests.map(({request,decisions})=>"| "+[request.id,request.clientId,request.route,...Object.values(decisions).map(d=>d.allowed?"Allowed":"429"),...Object.values(decisions).map(d=>formatRetryAfter(d.retryAfterMs))].map(cell).join(" | ")+" |");
 return ["# API rate limit incident handoff","", "- Generated: "+report.generatedAt,"- Scenario: "+report.scenario.name,"- Scope: "+report.scope,"- Policy: "+report.policy.limit+" requests / "+report.policy.windowMs+" ms","","> "+report.disclaimer,"","## Algorithm summary","","| Algorithm | Allowed | HTTP 429 | Estimated retry wait |","|---|---:|---:|---:|",...Object.entries(report.summary).map(([name,s])=>"| "+cell(name)+" | "+s.allowed+" | "+s.limited+" | "+formatRetryAfter(s.totalRetryAfterMs)+" |"),"","## Request evidence","","| Request | Client | Route | Fixed window | Sliding window | Token bucket | Fixed retry | Sliding retry | Bucket retry |","|---|---|---|---|---|---|---|---|---|",...rows,"","## Human review checks","","- Compare estimates with provider documentation and actual response headers.","- Check if retry attempts can amplify the incident or create duplicate side effects.","- Confirm whether quotas are scoped by credential, client, route or account.","- For production, verify distributed atomic state and clock assumptions.",""].join("\n");
}
