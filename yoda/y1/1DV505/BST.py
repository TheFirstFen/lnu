from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: int
    left: Any = None # smaller value
    right: Any = None # bigger value

@dataclass
class BinaryTree:
    root: Node = None  # root node

    def insert(self, n: Node, currValue: Node = None):
        if self.findNode(n) is not None:
            # checks for dups
            return 
        if self.root is None:
            # if tree is empty set parent to n
            self.root = n
        else:
            if currValue is None:
                currValue = self.root  # Start from the root
            
            # check where to insert
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
    
    
    def findNode(self, n: Node, currValue: Node = None, parent = None):
        if currValue is None:
            currValue = self.root
        if currValue is None:
            return None # leaf value found
        if n.value == currValue.value:
            print("Found it")
            return currValue, parent
        if n.value < currValue.value:
            parent = currValue
            if currValue.left is not None:
                self.findNode(n, currValue.left, parent)
        if n.value > currValue.value:
            parent = currValue
            if currValue.right is not None:
                self.findNode(n, currValue.right, parent)
    
    def findLeftMostValue(self, subTree: Node):
        while subTree.left is not None:
            subTree = subTree.left
        return subTree

    def remove(self, n: Node):
        searchResult = self.findNode(n)
        
        if searchResult is None:
            return False
        
        value, parent = searchResult
        left = value.left
        right = value.right
        
        # handle leaf
        if left is None and right is None: 
            if parent:
                if parent.left == value:
                    parent.left = None
                else:
                    parent.right = None
            else: # if parent is none than empty tree
                self.root = None

        # parent has exactly one child
        if parent:
            if parent.left = value:
                parent.left = right
            else:
                parent.right = right
        else:
            self.root = right
    
        furthestValueLeft = self.findLeftMostValue(right.left)
        parent = furthestValueLeft
