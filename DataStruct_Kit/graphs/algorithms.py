from typing import Dict, List, Any, Deque
from collections import deque

def dfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Depth-First Search implementation.
    
    Args:
        graph: Adjacency list representation {vertex: [neighbors]}
        start: Starting vertex
        
    Returns:
        List of vertices in DFS order
        
    Example:
        >>> graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        >>> dfs(graph, 2)
        [2, 0, 1, 3]
    """
    visited: List[Any] = []
    stack: List[Any] = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            # Push adjacent vertices in reverse order for proper DFS
            stack.extend(reversed(graph.get(vertex, [])))
    
    return visited

def bfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Breadth-First Search implementation.
    
    Args:
        graph: Adjacency list representation
        start: Starting vertex
        
    Returns:
        List of vertices in BFS order
        
    Example:
        >>> graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
        >>> bfs(graph, 0)
        [0, 1, 2, 3]
    """
    visited: List[Any] = []
    queue: Deque[Any] = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph.get(vertex, []))
    
    return visited