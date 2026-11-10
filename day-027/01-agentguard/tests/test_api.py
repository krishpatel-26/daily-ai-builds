import unittest
from fastapi.testclient import TestClient
from app.main import app
from app import store

class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        store.init_db()
        cls.client = TestClient(app)
    def test_health(self):
        self.assertEqual(self.client.get("/health").status_code, 200)
    def test_evaluate_returns_decision(self):
        payload={"actor":"qa-bot","role":"support_agent","action":"read","resource_type":"ticket","resource_id":"T-9","payload":{}}
        r=self.client.post("/api/evaluate",json=payload)
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()["status"],"allowed")
if __name__ == "__main__": unittest.main()
