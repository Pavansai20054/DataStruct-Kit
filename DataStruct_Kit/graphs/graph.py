from typing import Dict, List, Any

class Graph:
    """Undirected graph implementation."""
    
    def __init__(self) -> None:
        self.adj_list: Dict[Any, List[Any]] = {}

    def add_vertex(self, vertex: Any) -> None:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1: Any, vertex2: Any) -> None:
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.adj_list[vertex1].append(vertex2)
        self.adj_list[vertex2].append(vertex1)