import test from "node:test";import assert from "node:assert/strict";
import {normalizeText,normalizeRoute,normalizeClientId,normalizeRequestId} from "../src/core/normalize.js";
test("normalizes routes, query strings and trailing slashes",()=>{assert.equal(normalizeRoute("/v1//orders/?page=2"),"/v1/orders");assert.equal(normalizeRoute("/"),"/");assert.equal(normalizeRoute("v1/orders"),"");});
test("normalizes client and request identifiers",()=>{assert.equal(normalizeText(" x "),"x");assert.equal(normalizeClientId(" Acme/Client! "),"acmeclient");assert.equal(normalizeRequestId(" req  123 "),"req123");});
