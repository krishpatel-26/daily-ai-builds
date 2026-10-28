export function summarizeResults(results){
 const rows=Array.isArray(results)?results:[],total=rows.length,allowed=rows.filter(item=>item.allowed).length,limited=total-allowed;
 return {total,allowed,limited,successRate:total?allowed/total:0,totalRetryAfterMs:rows.reduce((sum,item)=>sum+(item.allowed?0:item.retryAfterMs),0),maxRetryAfterMs:rows.reduce((max,item)=>Math.max(max,item.retryAfterMs??0),0)};
}
export function compareAlgorithms(results){
 return Object.fromEntries(Object.entries(results??{}).map(([name,items])=>[name,summarizeResults(items)]));
}
export function percent(numerator,denominator){return denominator?Math.round(Number(numerator)/Number(denominator)*100)+"%":"0%";}
