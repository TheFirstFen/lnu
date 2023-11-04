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
        # Create new node
        node = Node(n)

        # If deque is emty
        if self.head is None:
            # Set both to current node
            self.head = self.tail = node
        else:
            # If the deque is not empty:
            # Add the new node to the end
            node.nxt = None
            self.tail.nxt = node
            # Set the new node at the end
            self.tail = node
        self.size += 1  # add size

    # Returns a string representation of the current deque content
    def to_string(self):
        current = self.head
        s = "{ "
        # Loop trough deque
        for i in range(self.size):
            s += str(current.value) + " "
            current = current.nxt
        s += "}"
        return s

    # Current Head --> Node1 --> Node2 --> ... --> NodeN --> None
    # Add element n as first entry in deque
    def add_first(self, n):
        # Create new node
        node = Node(n)

        # If deque is emty
        if self.head is None:
            # Set both to current node
            self.head = self.tail = node
        else:
            # If the deque is not empty:
            # Set the new node to the current head
            node.nxt = self.head
            # Set the new node as the new head
            self.head = node
        self.size += 1  # add size

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.tail is None:
            print("You can't access an empty queue")
            return None
        else:
            return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        else:
            return self.head.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        # If Deque is emty
        if self.head is None:
            print("You can't access an empty queue")
            return None
        pre_remove = self.head.value
        if self.size == 1:
            # only one in Deque, remove
            # set head and tail to None
            self.head = self.tail = None
        else:
            # Set the next as head
            self.head = self.head.nxt
        self.size -= 1
        return pre_remove

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        # If Deque is emty
        if self.tail is None:
            print("You can't access an empty queue")
            return None

        pre_remove = self.tail.value
        if self.size == 1:
            # only one in Deque, remove
            # set head and tail to None
            self.head = self.tail = None
        else:
            # Set the pre as tail
            # Keep track of current and previous
            current = self.head
            previous = None
            # Loop until pre tail
            for i in range(self.size):
                previous = current
                # To the next node
                current = current.nxt
            # Set previous to current tail
            self.tail = previous
            previous.nxt = None
        self.size -= 1
        return pre_remove
