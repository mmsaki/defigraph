from defigraph.Pool import Pool
from defigraph.Vertex import Vertex
import unittest
import pytest
from web3 import Web3

class TestPoolMethods(unittest.TestCase):
  pool = {
    "feeTier": "500",
    "id": "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
    "token0": {
      "decimals": "6",
      "id": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
      "name": "USD Coin",
      "symbol": "USDC"
    },
    "token0Price": "2582.932548000005213781395752324381",
    "token1": {
      "decimals": "18",
      "id": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
      "name": "Wrapped Ether",
      "symbol": "WETH"
    },
    "token1Price": "0.0003871568387545821353167124452051942"
  }
  fee = pool['feeTier']  
  token0 = pool['token0']['symbol']
  token0_decimals = int(pool['token0']['decimals'])
  token0_address =  Web3.to_checksum_address(pool['token0']['id'])
  token0Price = float(pool['token0Price'])

  token1 = pool['token1']['symbol']
  token1_decimals = int(pool['token1']['decimals'])
  token1_address = Web3.to_checksum_address(pool['token1']['id'])
  token1Price = float(pool['token1Price'])

  pool_address = Web3.to_checksum_address(pool['id'])

  u = Vertex(token0, token0_decimals, token0_address)
  v = Vertex(token1, token1_decimals, token1_address)
  
  def test_token0_not_equal_to_token1(self):
    with pytest.raises(ValueError, match="Token0 should not equal Token1"):
      Pool(pool_address=self.pool_address, token0=self.u, token1=self.u, fee=self.fee, token0_price=self.token0Price, token1_price=self.token1Price)
  
  def test_pool_address_should_be_valid_checksum(self):
    with pytest.raises(ValueError, match="Address is not a valud checksum address"):
      Pool(pool_address=self.pool['id'], token0=self.u, token1=self.v, fee=self.fee, token0_price=self.token0Price, token1_price=self.token1Price)

  def test_token_prices_should_be_type_float(self):
    with pytest.raises(ValueError, match=f"Token prices should be of type {float}"):
      Pool(pool_address=self.pool_address, token0=self.u, token1=self.v, fee=self.fee, token0_price=str(self.token0Price), token1_price=str(self.token1Price))
if __name__ == "__main__":
  unittest.main()