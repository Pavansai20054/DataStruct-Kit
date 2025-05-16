from typing import TypeVar, Generic, Optional, Any, Protocol

class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

T = TypeVar('T', bound=Comparable)

class AVLNode(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.left: Optional['AVLNode[T]'] = None
        self.right: Optional['AVLNode[T]'] = None
        self.height: int = 1

class AVLTree(Generic[T]):
    def __init__(self) -> None:
        self.root: Optional[AVLNode[T]] = None

    def insert(self, value: T) -> None:
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Optional[AVLNode[T]], value: T) -> AVLNode[T]:
        if node is None:
            return AVLNode(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return node

    def _get_height(self, node: Optional[AVLNode[T]]) -> int:
        return node.height if node else 0