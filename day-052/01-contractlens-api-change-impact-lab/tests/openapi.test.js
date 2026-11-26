import test from "node:test";import assert from "node:assert/strict";
import {parseOpenApi,operationKey,getJsonSchema} from "../src/core/openapi.js";
const doc={openapi:"3.0.3",info:{title:"Demo",version:"1"},paths:{"/x":{get:{operationId:"getX",responses:{"200":{description:"ok"}}}}}};
test("parses OpenAPI operations and metadata",()=>{const api=parseOpenApi(doc);assert.equal(api.title,"Demo");assert.equal(api.operations.length,1);assert.equal(api.operations[0].method,"GET");});
test("rejects invalid JSON, non-OpenAPI and missing paths",()=>{assert.throws(()=>parseOpenApi("{"),/Invalid JSON/);assert.throws(()=>parseOpenApi({openapi:"2.0",paths:{}}),/OpenAPI 3/);assert.throws(()=>parseOpenApi({openapi:"3.1.0"}),/paths/);});
test("operation key and response schema selection",()=>{assert.equal(operationKey("/x","get"),"GET /x");assert.equal(getJsonSchema({responses:{"200":{description:"ok",content:{"application/json":{schema:{type:"string"}}}}}},"response").type,"string");});
