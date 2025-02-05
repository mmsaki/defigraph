from .Pool import Pool


class Edge:
    def __init__(self, pool: Pool):
        self.pool = pool
        self.weight = -self.pool.token0_price.log10()
        self._tuple = [self.pool.token0, self.pool.token1, (self.weight, self.pool)]

    def __repr__(self):
        return f"({[i for i in self._tuple]})"

    def __eq__(self, edge):
        return self.pool == edge.pool

    def __ne__(self, edge):
        return self.pool != edge.pool

    def __iter__(self):
        return (i for i in self._tuple)

    def __getitem__(self, index):
        return self._tuple[index]
