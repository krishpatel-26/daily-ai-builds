import test from "node:test";
import assert from "node:assert/strict";
import { parseOpenApi } from "../src/core/openapi.js";
import { compareContracts } from "../src/core/diff.js";

const oldDoc = {
  openapi: "3.0.3",
  paths: {
    "/orders": {
      post: {
        operationId: "create",
        requestBody: {
          content: { "application/json": { schema: {
            type: "object",
            required: ["id"],
            properties: { id: { type: "string" }, state: { type: "string", enum: ["new", "old"] } }
          } } }
        },
        responses: { "201": { description: "ok" } }
      },
      get: {
        parameters: [{ name: "limit", in: "query", required: false, schema: { type: "integer", maximum: 100 } }],
        responses: { "200": { description: "ok" } }
      }
    },
    "/gone": { get: { responses: { "200": { description: "ok" } } } }
  }
};
const newDoc = {
  openapi: "3.0.3",
  paths: {
    "/orders": {
      post: {
        operationId: "create",
        requestBody: {
          content: { "application/json": { schema: {
            type: "object",
            required: ["id", "region"],
            properties: { id: { type: "string" }, region: { type: "string" }, state: { type: "string", enum: ["new"] } }
          } } }
        },
        responses: { "201": { description: "ok" } }
      },
      get: {
        parameters: [{ name: "limit", in: "query", required: true, schema: { type: "integer", maximum: 50 } }],
        responses: { "200": { description: "ok" } }
      }
    }
  }
};

test("detects required request field and removed enum value", () => {
  const findings = compareContracts(parseOpenApi(oldDoc), parseOpenApi(newDoc));
  assert.ok(findings.some(item => item.category === "required-property" && item.severity === "breaking"));
  assert.ok(findings.some(item => item.category === "enum-value" && item.severity === "breaking"));
});
test("detects new required parameter and removed operation", () => {
  const findings = compareContracts(parseOpenApi(oldDoc), parseOpenApi(newDoc));
  assert.ok(findings.some(item => item.category === "parameter-required"));
  assert.ok(findings.some(item => item.category === "operation-removed"));
});
test("classifies added operation as safe", () => {
  const before = parseOpenApi({ openapi: "3.0.3", paths: {} });
  const after = parseOpenApi({ openapi: "3.0.3", paths: { "/new": { get: { responses: { "200": { description: "ok" } } } } } });
  assert.equal(compareContracts(before, after)[0].severity, "safe");
});
