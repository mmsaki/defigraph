import unittest
from defigraph.Vertex import Vertex

class TestVertexMethods(unittest.TestCase):
  """Test class for Edge methods"""

  def setUp(self):
    name = "WETH"
    decimals = 18
    self.vertex = Vertex(name=name,decimals=decimals)

  def test_vertex_has_name(self):
    assert self.vertex.name is not None
  
  def test_vertex_has_decimals(self):
    assert self.vertex.decimals is not None

  def tearDown(self):
    return super().tearDown()


if __name__ == "__main__":
  unittest.main()