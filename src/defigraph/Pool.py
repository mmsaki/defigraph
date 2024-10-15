from defigraph.Vertex import Vertex

class Pool:
  def __init__(self, address: str, token0: Vertex, token1: Vertex):
    self.address = address
    self.token0 = token0
    self.token1 = token1