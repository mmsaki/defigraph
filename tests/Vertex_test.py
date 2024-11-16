import unittest
from defigraph.Vertex import Vertex
import pytest
from web3 import Web3


class TestVertexMethods(unittest.TestCase):
    def setUp(self):
        self.pool = {
            "feeTier": "500",
            "id": "0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640",
            "token0": {
                "decimals": "6",
                "id": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
                "name": "USD Coin",
                "symbol": "USDC",
            },
            "token0Price": "2582.932548000005213781395752324381",
            "token1": {
                "decimals": "18",
                "id": "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",
                "name": "Wrapped Ether",
                "symbol": "WETH",
            },
            "token1Price": "0.0003871568387545821353167124452051942",
        }

    def test_address_should_be_valid_checksum(self):
        with pytest.raises(ValueError):
            name = self.pool["token0"]
            decimals = int(self.pool["token0"]["decimals"])
            address = self.pool["token0"]["id"]
            Vertex(name, decimals, address)

    def test_fails_if_decimals_is_string(self):
        with pytest.raises(TypeError):
            name = self.pool["token0"]
            decimals = self.pool["token0"]["decimals"]
            address = Web3.to_checksum_address(self.pool["token0"]["id"])
            Vertex(name, decimals, address)

    def tearDown(self):
        return super().tearDown()


if __name__ == "__main__":
    unittest.main()
