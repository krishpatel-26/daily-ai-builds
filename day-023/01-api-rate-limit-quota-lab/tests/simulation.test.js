import test from "node:test";import assert from "node:assert/strict";
import {simulateTraffic,simulateAll} from "../src/core/simulate.js";
import {scenarios} from "../src/data/scenarios.js";
const policy={limit:2,windowMs:1000};
test("simulation preserves input row order even when replay sorts by time",()=>{const input=[{id:"late",atMs:900,clientId:"a",route:"/x"},{id:"early",atMs:0,clientId:"a",route:"/x"}];const result=simulateTraffic(input,policy);assert.equal(result[0].requestId,"late");assert.equal(result[1].requestId,"early");assert.equal(result[1].allowed,true);});
test("client and route keys get isolated counters",()=>{const input=[{id:"a",atMs:0,clientId:"a",route:"/x"},{id:"b",atMs:1,clientId:"b",route:"/x"},{id:"c",atMs:2,clientId:"a",route:"/y"}];const result=simulateTraffic(input,policy,"fixedWindow");assert.ok(result.every(row=>row.allowed));});
test("all algorithms return a decision per scenario request",()=>{const result=simulateAll(scenarios[0].traffic,policy);assert.deepEqual(Object.keys(result),["fixedWindow","slidingWindow","tokenBucket"]);assert.ok(Object.values(result).every(rows=>rows.length===scenarios[0].traffic.length));});
