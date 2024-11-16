# Defi Graph

![test](https://github.com/mmsaki/defigraph/actions/workflows/test.yml/badge.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/mmsaki/defigraph)
![GitHub last commit](https://img.shields.io/github/last-commit/mmsaki/defigraph)
![PyPI - Version](https://img.shields.io/pypi/v/defigraph)
![PyPI - Downloads](https://img.shields.io/pypi/dm/defigraph)
![GitHub top language](https://img.shields.io/github/languages/top/mmsaki/defigraph)

![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/msakiart)

This is package for creating and visualizing graphs in DeFi protocols.

## Install

Install using pip or uv

```sh
pip install defigraph

# or using uv

uv add defigraph
```

## Modules

- [x] [Edge](#edge-type) - describes a path between tokens
- [x] [Vertex](#vertex-type) - describes a token
- [x] [Graph](#graph-type) - describes a defi market
- [x] [Pool](#pool-type) - describes trading token pairs

## Edge type

Edges store two main state:

1. `self.weight` - a weight between two tokens
   - typeof `float`
   - `{0,1}` Depends on direction of edge
   - Calculated as `-Math.log(self.pool.token_price_{0,1})`
1. `self.pool` - an instance of a token pool
   - typeof `Pool`
1. `self._tuple` - Allows indexing/iteration of the edge object
   - typeof `iter`
   - Array of `[Vertex1, Vertex2, (self.weight, Pool)]`

## Pool type

A pool object describing tokens:

1. `self.address` - the address of the pool
   - typeof `Hex` checksum address
1. `self.token0` - a token described as a vertex
   - typeof `Vertex`
1. `self.token1` - a token described as a vertex
   - typeof `Vertex`
1. `self.token0_price` - the price of token0
   - typeof `float`
1. `self.token1_price` - the price of token1
   - typeof `float
1. `self.fee` - describes the pool fee e.g Uniswap (100 | 500 | 1000 | 3000)
   - typeof `int`

## Graph type

An adjacency list graph object desribing a defi market

1. `self.vertices` - contains a list of all vertices
   - typeof `List[Vertex]`
1. `self.adjascency_list` - a mapping describing edges in the graph
   - typeof `Dict[Vertex, List[Edge]]`
   - example: {Vertex: [Edge1, Edge2, Edge3, Edge4]}

## Vertex type

A node on the graph describing a token

1. `self.name` - name of the token
   - typeof `string`
1. `self.decimals` - number of decimals for token
   - typeof `int`
1. `self.address` - address of token
   - typeof `Hex` checksum address

## Tests

Run tests:

```sh
pytest
```
