# A head-and-tail implementation of a deque

# Each node is an instance of class Node
class Node:
    def __init__(self, value, next):
        self.value = value
        self.nxt = next


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n, None)
        if self.head is None:   # Empty queue
            self.head = new
            self.tail = new
        else:
            self.tail.nxt = new
            self.tail = new
        self.size += 1

    # Returns a string representation of the current deque content
    def __str__(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s

    # True if deque empty
    def is_empty(self):
        return self.size == 0

    # Add element n as first entry in deque
    def add_first(self, n):
        new_node = Node(n, None)
        if self.size == 0:
            self.head = self.tail = new_node

        else:
            new_node.nxt = self.head
            self.head = new_node
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Raises IndexError when accessing empty deque.
    def get_last(self):
        if self.head is None:
            raise IndexError("You can't access an empty queue")
        return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Raises IndexError when accessing empty deque.
    def get_first(self):
        if self.head is None:
            raise IndexError("You can't access an empty queue")
        return self.head.value

    # Removes and returns the first entry in the deque.
    # Raises IndexError when accessing empty deque.
    # The case size = 1 requires special handling
    def remove_first(self):
        if self.is_empty():
            raise IndexError("You can't remove from an empty queue")

        first = self.head.value

        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.nxt

        self.size -= 1
        return first

    # Removes and returns the last entry in the deque.
    # Raises IndexError when accessing empty deque.
    # The case size = 1 requires special handling
    def remove_last(self):
        if self.is_empty():
            raise IndexError("You can't remove from an empty queue")

        last = self.tail.value

        if self.size == 1:
            self.head = self.tail = None
        else:
            current = self.head     # current acts as a pointer to head

            while current.nxt != self.tail:
                current = current.nxt
            current.nxt = None
            self.tail = current

        self.size -= 1
        return last

    def __next__(self):
        if self.iteration is None:
            raise StopIteration
        current = self.iteration
        self.iteration = self.iteration.nxt
        return current.value

    # Returns an iterator over the deque
    # allowing for simple iteration over all elements
    # Part of Lecture 6
    def __iter__(self):
        self.iteration = self.head
        return self
