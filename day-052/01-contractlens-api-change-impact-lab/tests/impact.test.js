import test from "node:test";import assert from "node:assert/strict";
import {assessConsumerImpact,buildRolloutActions} from "../src/core/impact.js";
const findings=[{severity:"breaking",operation:"POST /orders",title:"New required field"},{severity:"review",operation:"GET /customers",title:"Format changed"}];
const registry={consumers:[{id:"a",name:"Priority Client",owner:"FDE A",tier:"Tier 1",criticality:"high",operations:["POST /orders"]},{id:"b",name:"Other Client",owner:"FDE B",tier:"Tier 2",criticality:"medium",operations:["GET /customers"]}]};
test("maps findings to matching consumer integrations",()=>{const impacts=assessConsumerImpact(findings,registry);assert.equal(impacts.length,2);assert.equal(impacts[0].level,"critical");assert.equal(impacts[0].name,"Priority Client");});
test("generates owned rollout actions including release review",()=>{const impacts=assessConsumerImpact(findings,registry),actions=buildRolloutActions(findings,impacts);assert.ok(actions.some(a=>a.priority==="P0"&&a.owner==="FDE A"));assert.ok(actions.some(a=>a.owner==="Release owner"));});
