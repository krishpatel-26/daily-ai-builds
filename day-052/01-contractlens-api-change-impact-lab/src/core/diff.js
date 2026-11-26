import {operationKey,getJsonSchema} from "./openapi.js";
function finding(severity,category,title,path,explanation,before,after,operation){return {id:category+":"+path,severity,category,title,path,explanation,before:before??null,after:after??null,operation};}
function schemaDiff(before,after,basePath,operation,side){
 const out=[];if(!before||!after)return out;
 if(before.type&&after.type&&before.type!==after.type)out.push(finding("breaking","schema-type",side+" schema type changed",basePath+"/type","Changing a schema type can break serialization or parsing.",before.type,after.type,operation));
 const oldRequired=new Set(before.required??[]),newRequired=new Set(after.required??[]);
 for(const name of newRequired)if(!oldRequired.has(name))out.push(finding("breaking","required-property","New required property",basePath+"/required/"+name,"Existing request payloads may omit this field.",false,true,operation));
 const oldProps=before.properties??{},newProps=after.properties??{};
 for(const name of Object.keys(oldProps))if(!(name in newProps))out.push(finding(side==="response"?"review":"breaking","removed-property","Property removed",basePath+"/properties/"+name,side==="response"?"Strict response consumers may reference this property.":"Clients may still submit this property.",oldProps[name],null,operation));
 for(const [name,next] of Object.entries(newProps)){
  const previous=oldProps[name];if(!previous)continue;
  if(previous.type&&next.type&&previous.type!==next.type)out.push(finding("breaking","property-type","Property type changed",basePath+"/properties/"+name,"Existing clients may send or expect the previous type.",previous.type,next.type,operation));
  if(Array.isArray(previous.enum)&&Array.isArray(next.enum)){const removed=previous.enum.filter(v=>!next.enum.includes(v));if(removed.length)out.push(finding("breaking","enum-value","Enum values removed",basePath+"/properties/"+name+"/enum","Consumers may send or expect a value no longer accepted or returned.",removed,next.enum,operation));}
  if(previous.format&&next.format&&previous.format!==next.format)out.push(finding("review","format-change","Property format changed",basePath+"/properties/"+name+"/format","Format constraints may affect validation and parsing.",previous.format,next.format,operation));
 }
 return out;
}
function parameterDiff(oldOp,newOp,path,operation){
 const out=[],oldParams=oldOp.parameters??[],newParams=newOp.parameters??[],key=p=>String(p.in)+":"+String(p.name),nextByKey=new Map(newParams.map(p=>[key(p),p]));
 for(const p of oldParams){const k=key(p),next=nextByKey.get(k);
  if(!next){out.push(finding("breaking","parameter-removed","Parameter removed",path+"/parameters/"+k,"Existing clients may still send a parameter expected by their integration.",p,null,operation));continue;}
  if(!p.required&&next.required)out.push(finding("breaking","parameter-required","Parameter is now required",path+"/parameters/"+k+"/required","Existing requests may omit this parameter.",false,true,operation));
  const a=p.schema??{},b=next.schema??{};
  if(a.type&&b.type&&a.type!==b.type)out.push(finding("breaking","parameter-type","Parameter type changed",path+"/parameters/"+k+"/schema/type","Client serialization and validation may fail.",a.type,b.type,operation));
  if(a.maximum!==undefined&&b.maximum!==undefined&&b.maximum<a.maximum)out.push(finding("review","parameter-bound","Parameter maximum narrowed",path+"/parameters/"+k+"/schema/maximum","Previously valid values above the new maximum may be rejected.",a.maximum,b.maximum,operation));
 }
 return out;
}
export function compareContracts(oldApi,newApi){
 const findings=[],oldMap=new Map(oldApi.operations.map(o=>[operationKey(o.path,o.method),o])),newMap=new Map(newApi.operations.map(o=>[operationKey(o.path,o.method),o]));
 for(const [key,old] of oldMap){const next=newMap.get(key);
  if(!next){findings.push(finding("breaking","operation-removed","Operation removed","/paths"+old.path+"/"+old.method.toLowerCase(),"Existing consumers can no longer call this operation.",key,null,key));continue;}
  if(old.operation.operationId!==next.operation.operationId)findings.push(finding("review","operation-id","Operation ID changed","/paths"+old.path+"/"+old.method.toLowerCase()+"/operationId","Generated SDK method names may change.",old.operation.operationId,next.operation.operationId,key));
  findings.push(...parameterDiff(old.operation,next.operation,"/paths"+old.path+"/"+old.method.toLowerCase(),key));
  const oldReq=getJsonSchema(old.operation,"request"),newReq=getJsonSchema(next.operation,"request");
  if(oldReq&&newReq)findings.push(...schemaDiff(oldReq,newReq,"/paths"+old.path+"/"+old.method.toLowerCase()+"/requestBody/content/application~1json/schema",key,"request"));
  const oldRes=getJsonSchema(old.operation,"response"),newRes=getJsonSchema(next.operation,"response");
  if(oldRes&&newRes)findings.push(...schemaDiff(oldRes,newRes,"/paths"+old.path+"/"+old.method.toLowerCase()+"/responses/schema",key,"response"));
  const oldCodes=Object.keys(old.operation.responses??{}),newCodes=new Set(Object.keys(next.operation.responses??{}));
  for(const code of oldCodes)if(!newCodes.has(code))findings.push(finding("review","response-removed","Response code removed","/paths"+old.path+"/"+old.method.toLowerCase()+"/responses/"+code,"Clients may handle this documented response explicitly.",code,null,key));
 }
 for(const [key,next] of newMap)if(!oldMap.has(key))findings.push(finding("safe","operation-added","Operation added","/paths"+next.path+"/"+next.method.toLowerCase(),"New operation is generally additive for existing consumers.",null,key,key));
 const rank={breaking:0,review:1,safe:2};
 return findings.sort((a,b)=>rank[a.severity]-rank[b.severity]||a.path.localeCompare(b.path));
}
