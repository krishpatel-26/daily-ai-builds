import {assessConsumerImpact,buildRolloutActions} from "./impact.js";
export function buildAnalysisReport({oldApi,newApi,findings,registry,generatedAt=new Date().toISOString()}){
 const impacts=assessConsumerImpact(findings,registry);
 return {schemaVersion:"1.0",generatedAt,scope:"openapi-json-static-analysis",baseline:{title:oldApi.title,version:oldApi.version},candidate:{title:newApi.title,version:newApi.version},summary:{total:findings.length,breaking:findings.filter(f=>f.severity==="breaking").length,review:findings.filter(f=>f.severity==="review").length,safe:findings.filter(f=>f.severity==="safe").length,affectedConsumers:impacts.length},findings,consumerImpacts:impacts,rolloutActions:buildRolloutActions(findings,impacts),disclaimer:"Static contract analysis only. Consumer registry is synthetic unless separately verified. Confirm results with actual clients and contract tests before release."};
}
function cell(value){return String(value??"").replace(/\|/g,"\\|").replace(/[\r\n]+/g," ").replace(/</g,"&lt;").replace(/>/g,"&gt;");}
export function reportToMarkdown(report){
 const findingRows=report.findings.map(f=>"| "+[f.severity,f.title,f.operation,f.path,f.explanation].map(cell).join(" | ")+" |");
 const consumerRows=report.consumerImpacts.map(c=>"| "+[c.name,c.owner,c.level,c.breakingCount,c.reviewCount].map(cell).join(" | ")+" |");
 const actionRows=report.rolloutActions.map(a=>"| "+[a.priority,a.owner,a.action].map(cell).join(" | ")+" |");
 return ["# API contract change impact report","", "- Generated: "+report.generatedAt,"- Baseline: "+report.baseline.title+" "+report.baseline.version,"- Candidate: "+report.candidate.title+" "+report.candidate.version,"- Scope: "+report.scope,"","> "+report.disclaimer,"","## Summary","",JSON.stringify(report.summary,null,2),"","## Findings","","| Severity | Finding | Operation | Evidence path | Explanation |","|---|---|---|---|---|",...findingRows,"","## Affected consumers","","| Consumer | Owner | Impact | Breaking | Review |","|---|---|---|---:|---:|",...consumerRows,"","## Rollout actions","","| Priority | Owner | Action |","|---|---|---|",...actionRows,""].join("\n");
}
