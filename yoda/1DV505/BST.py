from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    value: int
    left: Any = None
    right: Any = None

@dataclass
class BinaryTree:
    root: Node = None  # root node

    def insert(self, n: Node, currValue: Node = None):
        if self.root is None:
            # if tree is empty set parent to n
            self.root = n
        else:
            if currValue is None:
                currValue = self.root  # Start from the root
            
            # Check where to insert
            if n.value < currValue.value: # left is lower values
                # move left
                if currValue.left is None:
                    currValue.left = n
                else:
                    # Go to left child
                    self.insert(n, currValue.left)
            elif n.value > currValue.value: # right is increasing values
                # Move right
                if currValue.right is None:
                    currValue.right = n
                else:
                    # Go to the right child
                    self.insert(n, currValue.right)

    def printTree(self, currValue: Node = None):
        if currValue is None:
            currValue = self.root  # Start at the root value
        
        if currValue is not None:
            if currValue.left is not None:
                self.printTree(currValue.left)  # move into left tree
            
            print(currValue.value)           # Print the current node's value
            if currValue.right is not None:    
                self.printTree(currValue.right)  # move into right tree
    
    def remove():
        pass

# Create a binary tree and insert nodes
tree = BinaryTree()
tree.insert(Node(10))
tree.insert(Node(5))
tree.insert(Node(15))
tree.insert(Node(3))
tree.insert(Node(7))
tree.insert(Node(13))
tree.insert(Node(17))

# Print the tree
tree.printTree()  # This should print the values in sorted order

