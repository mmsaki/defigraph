import unittest
from defigraph.Vertex import Vertex

class TestVertexMethods(unittest.TestCase):
  def setUp(self):
    name = "WETH"
    decimals = 18
    addresss = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
    self.vertex = Vertex(name=name,decimals=decimals, address=addresss)

  def test_vertex_has_name(self):

    assert self.vertex.name is not None
  
  def test_vertex_has_decimals(self):
    assert self.vertex.decimals is not None

  def test_vertex_has_address(self):
    assert self.vertex.address is not None

  def test_address_length(self):
    assert len(self.vertex.address) == 42
  
  def tearDown(self):
    return super().tearDown()


if __name__ == "__main__":
  unittest.main()