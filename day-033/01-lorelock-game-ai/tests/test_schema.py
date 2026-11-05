import unittest
from app.schemas import ActionProposal
class SchemaTests(unittest.TestCase):
 def test_extra_fields_forbidden(self):
  with self.assertRaises(Exception):ActionProposal(request_id="case-001",actor_id="player",action="talk",target_id="elder",raw_script="run")
 def test_supported_action(self):
  self.assertEqual(ActionProposal(request_id="case-002",actor_id="player",action="talk",target_id="elder").action,"talk")
if __name__=="__main__":unittest.main()