import numpy as np
from .config import COMM_RADIUS
def build_adjacency(observations,radius=COMM_RADIUS):
 pos=np.asarray(observations)[:,0]*9; dist=np.abs(pos[:,None]-pos[None,:]); adj=(dist<=radius).astype(np.float32); np.fill_diagonal(adj,1.); return adj
def edge_count(adjacency): return int((np.triu(np.asarray(adjacency),1)>0).sum())