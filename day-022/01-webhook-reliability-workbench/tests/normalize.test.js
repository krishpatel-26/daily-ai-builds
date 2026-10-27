import test from "node:test";import assert from "node:assert/strict";
import {normalizeText,normalizeHeaderName,normalizeEventId,normalizeEndpoint} from "../src/core/normalize.js";
test("normalization trims inputs and headers",()=>{assert.equal(normalizeText("  abc  "),"abc");assert.equal(normalizeHeaderName(" X-Signature! "),"x-signature");assert.equal(normalizeEventId(" evt 42 "),"evt42");assert.equal(normalizeText(null),"");});
test("endpoint normalization removes fragments and rejects invalid URLs",()=>{assert.equal(normalizeEndpoint("https://example.com/path/#fragment"),"https://example.com/path");assert.equal(normalizeEndpoint("not a url"),"");});
