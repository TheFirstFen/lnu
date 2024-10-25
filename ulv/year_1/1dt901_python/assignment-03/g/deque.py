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
    # Creat a node called new and if the head is None we assign
    # a head as the node and the tail as the head.
    # Else we add a tail to the node and if the next element is not None
    # we go to that element. We add the next node to the existing one.
    # Add one to size and last we return the node.
    def add_last(self, n):
        new = Node(n, None)
        if self.head is None:
            self.head = new
            self.tail = self.head
        else:
            node = self.tail
            while node.nxt is not None:
                node = node.nxt
            node.nxt = new
        self.size += 1
        return new

    # Returns a string representation of the current deque content
    # while the value of the node is not None we string the value and add
    # to a string. Then the next node is added if it meats the criteria.
    def to_string(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s

    # Add element n as first entry in deque
    # if self.head is None we create a new head and tail.
    # else we push in a element in the first place and add on to the count.
    def add_first(self, n):
        new = Node(n, None)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.head = Node(n, self.head)
        self.size += 1
        return new

    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # If the head is None its an empty list. Otherwise we move thrue the
    # deque and take the value of the last node.
    def get_last(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        else:
            node = self.head
            for i in range(self.size - 1):
                node = node.nxt
        return node.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    # aslong as the head is not None we just take the value from the head.
    def get_first(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        else:
            node = self.head
        return node.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    # aslong as head is not None a node is assigned the head and then that
    # value is stored in a variable and the head is set to None while the
    # second node is set to the head. size decresses by one.
    def remove_first(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        else:
            node = self.head
            node_val = node.value
            self.head = node.nxt
            node = None
            self.size -= 1
        return node_val

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    # if size = 1 the same thing as in remove first happends. If size larger
    # than one we move thrue to the second to last node and redirect that
    # to aim at null.
    def remove_last(self):
        if self.head is None:
            print("You can't access an empty queue")
            return None
        elif self.size - 1 == 0:
            self.head = self.head.nxt
            self.size -= 1
        else:
            node = self.head
            for i in range(self.size - 2):
                node = node.nxt
            removing = node.nxt
            remove_val = removing.value
            node.nxt = removing.nxt
            self.size -= 1
            return remove_val
