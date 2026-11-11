import unittest
from app.trainer import train
from app.evaluator import evaluate
class T(unittest.TestCase):
 def test_metrics(self):
  q=train(3)["q_tables"];r=evaluate(q,episodes=3);self.assertEqual(sum(r["wins"].values()),3)
 def test_random_baseline(self):self.assertEqual(evaluate(train(2)["q_tables"],2,opponent="random")["opponent"],"random")
if __name__=="__main__":unittest.main()