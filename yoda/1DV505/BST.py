from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    value: int
    left: Any = None
    right: Any = None


class BinaryTree:
    root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.value)
            self._inorder_traversal_recursive(node.right, result)

# Create the binary tree
tree = BinaryTree()

# Insert nodes
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(13)
tree.insert(17)

# In-order traversal
print("In-order Traversal:", tree.inorder_traversal())


