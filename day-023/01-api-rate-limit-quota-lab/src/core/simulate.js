import { createFixedWindowState, fixedWindowDecision } from "./fixed-window.js";
import { createSlidingWindowState, slidingWindowDecision } from "./sliding-window.js";
import { createTokenBucketState, tokenBucketDecision } from "./token-bucket.js";
import { validatePolicy } from "./validate-config.js";
const algorithms={
 fixedWindow:{create:createFixedWindowState,decide:fixedWindowDecision},
 slidingWindow:{create:createSlidingWindowState,decide:slidingWindowDecision},
 tokenBucket:{create:createTokenBucketState,decide:tokenBucketDecision}
};
export function simulateTraffic(traffic,policy,algorithm="fixedWindow"){
 const errors=validatePolicy(policy);if(errors.length)throw new TypeError("Invalid policy: "+errors.join(" "));
 const selected=algorithms[algorithm];if(!selected)throw new TypeError("Unsupported algorithm: "+algorithm);
 const state=selected.create(),keyed=(traffic??[]).map((request,index)=>({request,index})).sort((a,b)=>Number(a.request.atMs)-Number(b.request.atMs)||a.index-b.index);
 const results=new Array((traffic??[]).length);
 for(const {request,index} of keyed){
  const key=String(request.clientId)+"|"+String(request.route),atMs=Math.max(0,Number(request.atMs)||0);
  const decision=selected.decide(state,key,atMs,policy,request.cost??1);
  results[index]={...decision,requestId:request.id,clientId:request.clientId,route:request.route,atMs,algorithm};
 }
 return results;
}
export function simulateAll(traffic,policy){
 return {fixedWindow:simulateTraffic(traffic,policy,"fixedWindow"),slidingWindow:simulateTraffic(traffic,policy,"slidingWindow"),tokenBucket:simulateTraffic(traffic,policy,"tokenBucket")};
}
