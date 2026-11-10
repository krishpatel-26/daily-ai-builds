import unittest
from app.engine import evaluate
from app.models import ActionProposal

def proposal(**kw):
    data = dict(actor="bot", role="support_agent", action="read", resource_type="ticket",
                resource_id="T-1", payload={}, current_state={}, expected_state={})
    data.update(kw)
    return ActionProposal(**data)

class EngineTests(unittest.TestCase):
    def test_allowed_low_risk_read(self):
        d = evaluate(proposal())
        self.assertEqual(d.status, "allowed")
        self.assertFalse(d.requires_approval)
    def test_unknown_action_denied(self):
        d = evaluate(proposal(action="delete"))
        self.assertEqual(d.status, "denied")
    def test_customer_update_requires_approval(self):
        d = evaluate(proposal(resource_type="customer", action="update_contact"))
        self.assertEqual(d.status, "pending_approval")
        self.assertTrue(d.requires_approval)
    def test_precondition_mismatch_denied(self):
        d = evaluate(proposal(current_state={"status":"closed"}, expected_state={"status":"open"}))
        self.assertEqual(d.status, "denied")
    def test_secret_payload_denied(self):
        d = evaluate(proposal(payload={"api_key":"leak"}))
        self.assertEqual(d.status, "denied")
if __name__ == "__main__": unittest.main()
