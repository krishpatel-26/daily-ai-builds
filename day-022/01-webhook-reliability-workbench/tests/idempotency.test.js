import test from "node:test";import assert from "node:assert/strict";
import {findDuplicateKeys,hasPriorSuccessfulDelivery} from "../src/core/idempotency.js";
const events=[{id:"a",idempotencyKey:"order-1",status:"failed"},{id:"b",idempotencyKey:"order-1",status:"delivered"},{id:"c",idempotencyKey:"order-2",status:"failed"},{id:"d",idempotencyKey:"",status:"failed"}];
test("duplicate groups exclude blank keys",()=>{assert.deepEqual(findDuplicateKeys(events),[{key:"order-1",count:2,eventIds:["a","b"]}]);});
test("prior successful delivery is checked by key",()=>{assert.equal(hasPriorSuccessfulDelivery(events,events[0]),true);assert.equal(hasPriorSuccessfulDelivery(events,events[2]),false);});
