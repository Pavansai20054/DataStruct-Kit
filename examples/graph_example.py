# Example of using graphs
from DataStruct_Kit.graphs.graph import Graph
from DataStruct_Kit.graphs.algorithms import dfs

if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    print("Graph adjacency list:", g.adj_list)
    print("DFS from 1:", dfs(g.adj_list, 1))