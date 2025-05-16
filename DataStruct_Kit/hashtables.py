from typing import Any, Optional, Tuple, List

class HashTable:
    """Hash table implementation with linear probing."""
    
    def __init__(self, size: int = 10) -> None:
        self.size: int = size
        self.table: List[Optional[Tuple[str, Any]]] = [None] * size
        self.count: int = 0

    def _hash(self, key: str) -> int:
        return sum(ord(c) for c in key) % self.size

    def put(self, key: str, value: Any) -> None:
        if self.count >= self.size:
            raise MemoryError("Hash table is full")
            
        index = self._hash(key)
        while self.table[index] is not None:
            stored_key, _ = self.table[index]  # type: ignore  # Safe due to None check
            if stored_key == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)
        self.count += 1

    def get(self, key: str) -> Optional[Any]:
        index = self._hash(key)
        original_index = index
        while self.table[index] is not None:
            stored_key, value = self.table[index]  # type: ignore  # Safe due to None check
            if stored_key == key:
                return value
            index = (index + 1) % self.size
            if index == original_index:
                break
        return None