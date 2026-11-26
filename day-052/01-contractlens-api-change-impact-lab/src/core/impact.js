export function assessConsumerImpact(findings,registry){
 const consumers=Array.isArray(registry?.consumers)?registry.consumers:[];
 return consumers.map(consumer=>{
  const matched=findings.filter(f=>consumer.operations?.includes(f.operation));
  const breaking=matched.filter(f=>f.severity==="breaking"),review=matched.filter(f=>f.severity==="review");
  const score=Math.min(100,breaking.length*35+review.length*12);
  const level=breaking.length?(consumer.criticality==="high"?"critical":"high"):review.length?"review":"none";
  return {consumerId:consumer.id,name:consumer.name,owner:consumer.owner,tier:consumer.tier,criticality:consumer.criticality,affected:matched.length>0,level,score,breakingCount:breaking.length,reviewCount:review.length,findings:matched};
 }).filter(item=>item.affected).sort((a,b)=>b.score-a.score||a.name.localeCompare(b.name));
}
export function buildRolloutActions(findings,impacts){
 const actions=[];
 for(const item of impacts)actions.push({priority:item.level==="critical"?"P0":item.level==="high"?"P1":"P2",owner:item.owner,action:"Contact "+item.name+" owner; confirm usage of "+item.findings.map(f=>f.operation).join(", "),evidence:item.findings.map(f=>f.title)});
 for(const f of findings.filter(x=>x.severity==="breaking"))actions.push({priority:"P1",owner:"API owner",action:"Provide a migration path for "+f.operation+": "+f.title,evidence:[f.path]});
 actions.push({priority:"P2",owner:"Release owner",action:"Run consumer contract tests and document rollback criteria before rollout.",evidence:["All affected operations"]});
 return actions;
}
