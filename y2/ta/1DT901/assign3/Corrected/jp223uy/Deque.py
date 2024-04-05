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
        new = Node(n)
        if self.tail is None:  # If empty
            self.tail = new  # Tail and head the last number
            self.head = new
        else:
            self.tail.nxt = new  # The previous tail is now nxt
            self.tail = new  # New input is tail
        self.size += 1
    # Returns a string representation of the current deque content

    def to_string(self):
        n = "{ "
        node = self.head
        while node is not None:  # When it is not empty
            n += str(node.value) + " "
            node = node.nxt  # Change value, it gets bigger
        n += "}"
        return n

    # Add element n as first entry in deque

    def add_first(self, n):
        new = Node(n)
        if self.head is None:  # If empty, new = both head and tail
            self.head = new
            self.tail = new
        else:
            new.nxt = self.head  # Previous head is now second
            self.head = new  # New value is head
        self.size += 1
    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.

    def get_last(self):
        if self.tail is None:  # If deque is empty
            print("You can't access an empty queue")
            return None
        else:  # Simply take the tail value
            return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.head is None:  # If deque is empty
            print("You can't access an empty queue")
            return None
        else:  # Simply take head value
            return self.head.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.head is None:
            print("You can't acces an empty queue")
        elif self.head == self.tail:  # If deque only 1, special case
            res = self.head.value
            self.head = None  # Both head and tail will be no value
            self.tail = None
            self.size -= 1  # Size will decrease by only 1
            return res
        else:  # Normal case
            res = self.head.value
            self.head = self.head.nxt
            self.size -= 1
            return res
    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling

    def remove_last(self):
        if self.tail is None:  # If empty
            print("You can't acces an empty queue")
            return
        res = self.tail.value
        if self.size == 1:  # Size 1, special case
            self.head = None  # Both head and tail will be 0
            self.tail = None
            self.size -= 1  # Decrase the size to empty
        else:  # Regular case
            c_val = self.head
            while c_val.nxt != self.tail:  # As long as val not last
                c_val = c_val.nxt  # Val is the nxt
            self.tail = c_val  # Tail then becomes the nxt
            c_val.nxt = None
            self.size -= 1  # Size one less
        return res  # Return the tail value
