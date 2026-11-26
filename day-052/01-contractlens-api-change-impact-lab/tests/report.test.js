import test from "node:test";import assert from "node:assert/strict";
import {buildAnalysisReport,reportToMarkdown} from "../src/core/report.js";
const oldApi={title:"A",version:"1"},newApi={title:"A",version:"2"},findings=[{severity:"breaking",title:"Removed route",operation:"GET /x",path:"/paths/x",explanation:"Route removed."}];
test("builds report summary and carries static analysis disclaimer",()=>{const r=buildAnalysisReport({oldApi,newApi,findings,registry:{consumers:[]},generatedAt:"2026-01-01T00:00:00Z"});assert.equal(r.summary.breaking,1);assert.match(r.disclaimer,/Static contract analysis/);});
test("Markdown report includes findings and rollout checks",()=>{const r=buildAnalysisReport({oldApi,newApi,findings,registry:{consumers:[]}});const md=reportToMarkdown(r);assert.match(md,/API contract change impact report/);assert.match(md,/Removed route/);assert.match(md,/Release owner/);});
