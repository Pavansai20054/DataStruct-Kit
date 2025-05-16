from typing import Any, List, Optional

class MinHeap:
    """A min-heap implementation with proper typing."""
    
    def __init__(self) -> None:
        self.heap: List[Any] = []  # Can be more specific if needed (e.g., List[int])

    def insert(self, value: Any) -> None:
        """Inserts a value into the heap."""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, index: int) -> None:
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._sift_up(parent)