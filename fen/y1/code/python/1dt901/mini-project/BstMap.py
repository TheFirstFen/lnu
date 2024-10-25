from dataclasses import dataclass
from typing import Any, List, Tuple

from typing_extensions import Self

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
    key: Any = None  # the key
    value: Any = None  # the value
    left: Self = None  # left child (a Node)
    right: Self = None  # right child (a Node)

    def put(self, key: Any, value: Any) -> None:
        # If the key is equal to current nodes key then change
        # to value of the old node to the new given value
        if self.key == key:
            self.value = value
        # If the key if less then current nodes key and
        # the current node has no left branch create a
        # new node as its left branch with given key and value
        # otherwise call put recursively with given key and value
        elif key < self.key:
            if self.left is None:
                self.left = Node(key, value, None, None)
            else:
                self.left.put(key, value)
        # If the key if greater then current nodes key and
        # the current node has no right branch create a
        # new node as its right branch with given key and value
        # otherwise call put recursively with given key and value
        else:
            if self.right is None:
                self.right = Node(key, value, None, None)
            else:
                self.right.put(key, value)

    def to_string(self) -> str:
        # If current node has branches to both right and left
        # call first the left branch recursively then print
        # the current node and then call the right branch recursively
        if self.left is not None and self.right is not None:
            return (
                f"{self.left.to_string()} ({self.key},"
                + f"{self.value}) {self.right.to_string()}"
            )
        # If current node has a left branch call it recursively
        # for the left branch and then print out current node
        if self.left is not None:
            return f"{self.left.to_string()} ({self.key}, {self.value})"
        # If current node has a right branch print out current node
        # and then call it recursively for the right branch
        if self.right is not None:
            return f"({self.key}, {self.value}) " + self.right.to_string()
        # Lastly if leaf print out current node
        return f"({self.key}, {self.value})"

    def count(self) -> int:
        # If current node has branches to both right and left
        # call first the left branch recursively then add 1
        # and then add and call the right branch recursively
        # and return the value
        if self.left is not None and self.right is not None:
            return self.left.count() + 1 + self.right.count()
        # If current node has a left branch call it recursively
        # for the left branch and add 1 to its value and
        # return the value
        if self.left is not None:
            return self.left.count() + 1
        # If current node has a right branch  call it recursively
        # and then add its value to 1 and return the value
        if self.right is not None:
            return 1 + self.right.count()
        # Lastly if leaf return 1
        return 1

    def get(self, key: Any) -> Any:
        # Ifall nyckel passar, ge värde
        if self.key == key:
            return self.value
        # Ifall nyckel mindre, gå åt vänster
        elif key < self.key:
            if self.left is not None:
                return self.left.get(key)
        # Ifall nyckel större, gå höger
        else:
            if self.right is not None:
                return self.right.get(key)

    def max_depth(self) -> int:
        # Create variables for each sides depth
        left, right = 0, 0
        # If current nodes left or right is None ignore
        if self.left is not None:
            left = self.left.max_depth()
        if self.right is not None:
            right = self.right.max_depth()

        # The side which has the greater value add one to it
        return max(right, left) + 1

    def count_leafs(self) -> int:
        # Ifall vi är ett löv, ge tillbaka 1
        if self.left is None and self.right is None:
            return 1

        # Kolla rekursivt efter löv och lägg till i räknare
        counter = 0
        if self.left is not None:
            counter += self.left.count_leafs()
        if self.right is not None:
            counter += self.right.count_leafs()

        # Vi har kollat höger o vänster efter löv, ge tillbaka antalet
        return counter

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst: List[Tuple[Any, Any]]) -> List[Tuple[Any]]:
        # Goes to the furthest left point of the tree and adds it to the list
        if self.left is not None:
            self.left.as_list(lst)
        lst.append((self.key, self.value))

        # After adding the furthest left point to the list checks if there is
        # a right node to that point and if there is recursively calls as_list
        if self.right is not None:
            self.right.as_list(lst)

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
    def put(self, key, value) -> None:
        if self.root is None:  # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self) -> str:
        if self.root is None:  # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self) -> int:
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key) -> Any:
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self) -> int:
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a leaf node count. That is, the number of nodes
    # with no children
    def count_leafs(self) -> int:
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self) -> List[Tuple[Any]]:
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
