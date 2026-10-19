import unittest

from agent_reliability.graders import grade_output


class GraderTests(unittest.TestCase):
    def test_contains_all_passes_case_insensitively(self):
        result = grade_output("Refunds are within 30 DAYS.", {"contains_all": ["30 days"]})
        self.assertTrue(result[0]["passed"])

    def test_missing_required_phrase_fails(self):
        result = grade_output("Refunds depend on approval.", {"contains_all": ["30 days"]})
        self.assertFalse(result[0]["passed"])

    def test_forbidden_phrase_fails(self):
        result = grade_output("We guarantee approval.", {"forbid_any": ["guarantee approval"]})
        self.assertFalse(result[0]["passed"])

    def test_bullet_limit(self):
        output = "- one\n- two\n- three"
        result = grade_output(output, {"max_bullets": 2})
        self.assertFalse(result[0]["passed"])

    def test_json_required_keys(self):
        result = grade_output('{"priority":"high"}', {"valid_json_keys": ["priority", "rationale"]})
        self.assertFalse(result[0]["passed"])

    def test_uncertainty_phrase(self):
        result = grade_output("I cannot determine this from the context.", {"requires_uncertainty": True})
        self.assertTrue(result[0]["passed"])


if __name__ == "__main__":
    unittest.main()
