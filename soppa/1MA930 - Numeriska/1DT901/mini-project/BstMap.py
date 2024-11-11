from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    # inputs provided key and value into tree
    def put(self, key, value):
        # check side of root to put new key and value into
        if key < self.key:
            # if its an empty spot, create a new node
            if self.left is None:
                self.left = Node(key, value)
            # if not empty call for function again
            else:
                self.left.put(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.put(key, value)
        # if key already exist replace with new value
        else:
            self.key = key
            self.value = value

    # prints bst to string using in-order traversal
    def to_string(self):
        if self.left is not None:
            if self.right is not None:
                return self.left.to_string() + \
                    f"({self.key},{self.value}) " + \
                    self.right.to_string()
            else:
                return self.left.to_string() + \
                    f"({self.key},{self.value}) "
        if self.left is None:
            if self.right is not None:
                return f"({self.key},{self.value}) " + self.right.to_string()
            else:
                return f"({self.key},{self.value}) "

    # count bst by counting each side of node
    def count(self):
        # if there is a node on each side add their values and add 1
        if self.left is not None and self.right is not None:
            return 1 + self.left.count() + self.right.count()
        # if only a left node exist call function again and return 1 + count
        if self.left is not None:
            return 1 + self.left.count()
        # if only a right node exist call function again and return 1 + count
        elif self.right is not None:
            return 1 + self.right.count()
        # if leaf node return 1
        else:
            return 1

    # gets a value from bst corresponding to key provided
    def get(self, key):
        # if current nodes key corresponds to key
        if self.key == key:
            return self.value
        # chooses side where key is
        if key < self.key:
            if self.left is not None:
                return self.left.get(key)
        else:
            if self.right is not None:
                return self.right.get(key)

    # counts the maximum depth of tree by comparing left to right side
    def max_depth(self):
        # if there is a node on each side compare both sides
        if self.left is not None and self.right is not None:
            le = self.left.max_depth()
            ri = self.right.max_depth()
            # if left side is deeper return its max depth + 1
            if le > ri:
                return le + 1
            else:
                return ri + 1
        # if node exists on left side count its max depth and return value
        if self.left is not None:
            return 1 + self.left.max_depth()
        # if node exists on right side count its max depth and return value
        elif self.right is not None:
            return 1 + self.right.max_depth()
        # if node has no child return 1
        else:
            return 1

    # counts amount of leafs in tree
    def count_leafs(self):
        # if node has two childs count leafs on each side and return amount
        if self.left is not None and self.right is not None:
            return self.left.count_leafs() + self.right.count_leafs()
        # if there is a node on the left count its leaf nodes
        if self.left is not None:
            return self.left.count_leafs()
        # if there is a node on the right count its leaf nodes
        elif self.right is not None:
            return self.right.count_leafs()
        # if leaf node, return 1
        else:
            return 1

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        # first check left side of each node
        if self.left is not None:
            # if there also exists a right child append both sides + node
            if self.right is not None:
                self.left.as_list(lst)
                lst.append((self.key, self.value))
                self.right.as_list(lst)
            # if only left child exists append its key,val and nodes key,val
            else:
                self.left.as_list(lst)
                lst.append((self.key, self.value))
        # if no left child exists go to the right child
        if self.left is None:
            # if only right child exist append its key,val and children
            if self.right is not None:
                lst.append((self.key, self.value))
                self.right.as_list(lst)
            # if leaf node append its value
            else:
                lst.append((self.key, self.value))
        # return the created list
        return lst


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a leaf node count. That is, the number of nodes
    # with no children
    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
