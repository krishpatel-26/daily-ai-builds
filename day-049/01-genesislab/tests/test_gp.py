import unittest
from genesislab.gp import GaussianProcess,cholesky
from genesislab.domain import candidates
from genesislab.acquisition import propose,expected_improvement
class Tests(unittest.TestCase):
 def test_cholesky(self):
  l=cholesky([[4,2],[2,3]]);self.assertAlmostEqual(l[0][0]**2,4)
 def test_gp_uncertainty(self):
  c=candidates();gp=GaussianProcess(c[:3],[65,70,75]);mu,sd=gp.predict(c[1]);self.assertTrue(0<=sd<16)
 def test_acquisition_nonnegative(self):self.assertGreaterEqual(expected_improvement(80,3,85),0)
 def test_proposal_excludes_known(self):
  c=candidates();p,_=propose(c,[(c[0],60)]);self.assertNotEqual(p,c[0])
 def test_bad_training_size(self):
  with self.assertRaises(ValueError):GaussianProcess(candidates()[:2],[75])
