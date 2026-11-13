import unittest,torch
from app.networks import Actor,CentralCritic
class T(unittest.TestCase):
 def test_actor(self):self.assertEqual(Actor()(torch.zeros(2,6)).shape,(2,5))
 def test_critic(self):self.assertEqual(CentralCritic()(torch.zeros(3,14)).shape,(3,))
if __name__=="__main__":unittest.main()