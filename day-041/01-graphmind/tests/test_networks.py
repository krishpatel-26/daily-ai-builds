import unittest,torch
from app.networks import Actor,Critic
class NetTests(unittest.TestCase):
 def test_actor_shape(self):
  logits,w=Actor()(torch.zeros(4,6),torch.eye(4));self.assertEqual(tuple(logits.shape),(4,3));self.assertEqual(tuple(w.shape),(4,4))
 def test_critic_shape(self):self.assertEqual(Critic()(torch.zeros(4,6)).ndim,0)
if __name__=="__main__":unittest.main()