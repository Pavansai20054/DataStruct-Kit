import pytest
from DataStruct_Kit.graphs.algorithms import dfs, bfs
from DataStruct_Kit.graphs import Graph, DirectedGraph

def test_dfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    assert dfs(graph, 'A') == ['A', 'B', 'D', 'E', 'F', 'C']

def test_bfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    assert bfs(graph, 'A') == ['A', 'B', 'C', 'D', 'E', 'F']

def test_graph_class():
    g = Graph()
    g.add_edge('A', 'B')
    assert 'A' in g.adj_list
    assert 'B' in g.adj_list['A']
    assert 'A' in g.adj_list['B']