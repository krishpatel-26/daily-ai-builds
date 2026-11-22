import unittest
from trustlayer.models import Evidence,Proposal
from trustlayer.engine import Engine
from trustlayer.approvals import ApprovalRegistry
from trustlayer.corpus import fixtures
class EngineTests(unittest.TestCase):
 def setUp(self):self.facts,self.proposals=fixtures()
 def test_valid_read(self):self.assertTrue(Engine().evaluate(self.proposals[0],self.facts).accepted)
 def test_forbidden_action(self):self.assertEqual(Engine().evaluate(self.proposals[1],self.facts).code,'ACTION_FORBIDDEN')
 def test_approval_required(self):self.assertEqual(Engine().evaluate(self.proposals[2],self.facts).code,'APPROVAL_REQUIRED')
 def test_human_approval_simulation(self):
  a=ApprovalRegistry();a.grant('P-03','demo-reviewer',1020)
  self.assertTrue(Engine(a).evaluate(self.proposals[2],self.facts).accepted)
 def test_expired_approval(self):
  a=ApprovalRegistry();a.grant('P-03','demo-reviewer',999)
  self.assertEqual(Engine(a).evaluate(self.proposals[2],self.facts).code,'APPROVAL_REQUIRED')
 def test_untrusted_source(self):self.assertEqual(Engine().evaluate(self.proposals[3],self.facts).code,'UNTRUSTED_SOURCE')
 def test_expired_fact(self):self.assertEqual(Engine().evaluate(self.proposals[4],self.facts).code,'EXPIRED_EVIDENCE')
 def test_prompt_injection(self):self.assertEqual(Engine().evaluate(self.proposals[5],self.facts).code,'INJECTION_INDICATOR')
 def test_resource_mismatch(self):self.assertEqual(Engine().evaluate(self.proposals[8],self.facts).code,'EVIDENCE_SCOPE_MISMATCH')
 def test_missing_evidence(self):
  p=Proposal('P-test','assistant','read_report','report:release-47',())
  self.assertEqual(Engine().evaluate(p,self.facts).code,'MISSING_EVIDENCE')