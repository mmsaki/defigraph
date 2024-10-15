from defigraph.Vertex import Vertex
from defigraph.Pool import Pool

class Edge:
  def __init__(self, u: Vertex, v: Vertex, pool_address: str, weight: float=None):
    self.u = u
    self.v = v
    self.weight = weight
    self.pool = Pool(address=pool_address,token0=u, token1=v)

  def __repr__(self):
    if not self.weight:
      return f"({self.u}, {self.v})"
    else:
      return f"({self.u}, {self.v}, {self.weight})"