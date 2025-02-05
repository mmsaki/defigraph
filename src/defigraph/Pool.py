from .Vertex import Vertex
from web3 import Web3
from decimal import Decimal


class Pool:
    def __init__(
        self,
        pool_address: str,
        token0: Vertex,
        token1: Vertex,
        fee: int,
        token0_price: Decimal,
        token1_price: Decimal,
    ):
        if token1 == token0:
            raise ValueError("Token0 should not equal Token1")
        if not Web3.is_checksum_address(pool_address):
            raise ValueError("Address is not a valid checksum address")

        self.address = pool_address
        self.token0 = token0
        self.token1 = token1
        self.token0_price = token0_price
        self.token1_price = token1_price
        self.fee = fee

    def __repr__(self):
        return f"{(self.token0, self.token1, self.fee)}"

    def __eq__(self, pool):
        return self.address == pool.address

    def __ne__(self, pool):
        return self.address != pool.address

    def __hash__(self):
        return hash(str(self))
