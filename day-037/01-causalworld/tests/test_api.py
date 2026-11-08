import unittest
from fastapi.testclient import TestClient
from app.main import app
class T(unittest.TestCase):
 def setUp(self):self.c=TestClient(app)
 def test_model(self):self.assertTrue(self.c.get("/api/model").json()["validation"]["acyclic"])
 def test_simulate(self):
  r=self.c.post("/api/simulate",json={"name":"test","interventions":[{"variable":"player_reputation","value":90}]});self.assertEqual(r.status_code,200)
if __name__=="__main__":unittest.main()