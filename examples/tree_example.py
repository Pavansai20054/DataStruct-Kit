# Example of using trees
from DataStruct_Kit.trees.binary_tree import BinaryTree

if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    print("Root:", bt.root.value)
    print("Left child:", bt.root.left.value)
    print("Right child:", bt.root.right.value)