from typing import TypeVar, Generic, Optional, Any, Protocol

class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

T = TypeVar('T', bound=Comparable)

class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.left: Optional['Node[T]'] = None
        self.right: Optional['Node[T]'] = None

class BinaryTree(Generic[T]):
    def __init__(self) -> None:
        self.root: Optional[Node[T]] = None

    def insert(self, value: T) -> None:
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Node[T], value: T) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)