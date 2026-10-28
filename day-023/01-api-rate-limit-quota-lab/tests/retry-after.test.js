import test from "node:test";import assert from "node:assert/strict";import {retryAfterSeconds,formatRetryAfter,parseRetryAfter} from "../src/core/retry-after.js";
test("Retry-After seconds round up to whole seconds",()=>{assert.equal(retryAfterSeconds(1),1);assert.equal(retryAfterSeconds(1001),2);assert.equal(formatRetryAfter(0),"0s");});
test("parses seconds and HTTP dates and rejects invalid values",()=>{assert.equal(parseRetryAfter("3",1000),3000);assert.equal(parseRetryAfter("invalid",1000),null);assert.equal(parseRetryAfter("Thu, 01 Jan 1970 00:00:05 GMT",1000),4000);});
