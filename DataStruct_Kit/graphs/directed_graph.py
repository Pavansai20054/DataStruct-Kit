from typing import Dict, List, Any

class DirectedGraph:
    """Directed graph implementation."""
    
    def __init__(self) -> None:
        self.adj_list: Dict[Any, List[Any]] = {}

    def add_vertex(self, vertex: Any) -> None:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src: Any, dest: Any) -> None:
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adj_list[src].append(dest)