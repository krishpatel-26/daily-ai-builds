import test from "node:test";import assert from "node:assert/strict";
import {fixedWindowDecision,createFixedWindowState} from "../src/core/fixed-window.js";
import {slidingWindowDecision,createSlidingWindowState} from "../src/core/sliding-window.js";
import {tokenBucketDecision,createTokenBucketState} from "../src/core/token-bucket.js";
const policy={limit:2,windowMs:1000};
test("fixed window resets at aligned boundaries",()=>{const s=createFixedWindowState();assert.equal(fixedWindowDecision(s,"a",0,policy).allowed,true);assert.equal(fixedWindowDecision(s,"a",1,policy).allowed,true);assert.equal(fixedWindowDecision(s,"a",2,policy).allowed,false);assert.equal(fixedWindowDecision(s,"a",1000,policy).allowed,true);});
test("sliding window retains recent requests across boundary",()=>{const s=createSlidingWindowState();slidingWindowDecision(s,"a",900,policy);slidingWindowDecision(s,"a",990,policy);assert.equal(slidingWindowDecision(s,"a",1005,policy).allowed,false);assert.equal(slidingWindowDecision(s,"a",1901,policy).allowed,true);});
test("token bucket permits burst then refills gradually",()=>{const s=createTokenBucketState();assert.equal(tokenBucketDecision(s,"a",0,policy).allowed,true);assert.equal(tokenBucketDecision(s,"a",0,policy).allowed,true);assert.equal(tokenBucketDecision(s,"a",0,policy).allowed,false);assert.equal(tokenBucketDecision(s,"a",500,policy).allowed,true);});
