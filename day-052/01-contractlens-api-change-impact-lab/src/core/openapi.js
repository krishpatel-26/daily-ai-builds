const HTTP_METHODS=new Set(["get","post","put","patch","delete","options","head","trace"]);
export function parseOpenApi(input){
 let document;try{document=typeof input==="string"?JSON.parse(input):input;}catch(error){throw new Error("Invalid JSON: "+error.message);}
 if(!document||typeof document!=="object"||Array.isArray(document))throw new TypeError("OpenAPI document must be a JSON object.");
 if(!String(document.openapi??"").startsWith("3."))throw new TypeError("Only OpenAPI 3.0 and 3.1 JSON documents are supported.");
 if(!document.paths||typeof document.paths!=="object"||Array.isArray(document.paths))throw new TypeError("OpenAPI document must contain a paths object.");
 const operations=[];for(const [path,pathItem] of Object.entries(document.paths)){
  if(!path.startsWith("/")||!pathItem||typeof pathItem!=="object")continue;
  for(const [method,operation] of Object.entries(pathItem))if(HTTP_METHODS.has(method.toLowerCase())&&operation&&typeof operation==="object")operations.push({path,method:method.toUpperCase(),operationId:operation.operationId??"",operation,pathItem});
 }
 return {document,operations,title:document.info?.title??"Untitled API",version:document.info?.version??"unknown"};
}
export function operationKey(path,method){return String(method).toUpperCase()+" "+path;}
export function getJsonSchema(operation,kind){
 if(kind==="request")return operation?.requestBody?.content?.["application/json"]?.schema??null;
 const codes=Object.keys(operation?.responses??{}).filter(code=>/^2\d\d$/.test(code)).sort();
 return operation?.responses?.[codes[0]]?.content?.["application/json"]?.schema??null;
}
