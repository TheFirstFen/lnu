from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n, None)
        # check if there's nodes, if not. add..
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            # There's already nodes, make new ones
            node = self.head
            while node.nxt is not None:
                node = node.nxt
            node.nxt = new
            self.tail = new
        # Increase size by 1
        self.size += 1

    # Returns a string representation of the current deque content
    def to_string(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n, None)
        # check if there's nodes, if not. add..
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            # There's already nodes, make new ones
            new.nxt = self.head
            self.head = new
        # Increase size by 1
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.tail is None:
            print("You can't access an empty queue")
        else:
            # Return tail value.
            return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head is None:
            print("You can't access an empty queue")
        else:
            # Return head value.
            return self.head.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.head is None:
            print("You can't access an empty queue")
        elif self.size == 1:
            del_val = self.head
            self.head.nxt = None
            self.tail.nxt = None
            return del_val.value
        else:
            # Remove the pointer and set the next node to head.
            del_val = self.head
            self.head = self.head.nxt
            self.size -= 1
            # Return deleted value
            return del_val.value

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        elif self.size == 1:
            # List is only 1 node large. remove by setting head, tail to None
            value = self.tail.value
            self.head = None
            self.tail = None
            self.size = 0
            return value
        else:
            # Go through the nodes until next node is tail. set current to tail
            node = self.head
            del_val = self.tail.value
            while node.nxt is not self.tail:
                node = node.nxt
            node.nxt = None
            self.tail = node
            self.size -= 1
            # Return deleted value
            return del_val
