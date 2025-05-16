# Tests for trees
from DataStruct_Kit.trees.binary_tree import BinaryTree
from DataStruct_Kit.trees.avl_tree import AVLTree
from DataStruct_Kit.trees.heap import MinHeap


def test_binary_tree():
    """Tests binary tree operations."""
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    assert bt.root.value == 5
    assert bt.root.left.value == 3
    assert bt.root.right.value == 7


def test_avl_tree():
    """Tests AVL tree operations."""
    avl = AVLTree()
    avl.insert(5)
    avl.insert(3)
    avl.insert(7)
    assert avl.root.value == 5
    assert avl.root.left.value == 3
    assert avl.root.right.value == 7


def test_min_heap():
    """Tests min-heap operations."""
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    assert heap.heap[0] == 3