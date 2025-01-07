class Heap:
    def __init__(self):
        self.array = []

    def __str__(self):  # String repr. of heap content
        output = "["
        for i in range(self.get_size()):
            if i < self.get_size()-1:
                output += str(self.array[i]) + ", "
            else:
                output += str(self.array[i])
        output += "]"
        return output

    def get_size(self):     # Current heap size
        return len(self.array)

    def is_empty(self):     # True if heap empty, otherwise False
        return self.get_size() == 0

    def peek(self):     # Return (without removing) top element
        if self.is_empty():
            raise IndexError("You can't get the peek value in an empty heap")
        return self.array[0]

    def add(self, elem):    # Add element to heap
        size = self.get_size()

        self.array.append(elem)
        elem_pos = size

        while elem_pos > 0:
            parent_pos = (elem_pos-1) // 2
            parent_val = self.array[parent_pos]

            # if new element is  bigger than parent swap them
            if elem > parent_val:
                self.array[parent_pos] = elem
                self.array[elem_pos] = parent_val
                elem_pos = parent_pos
            else:
                break

    def pull_high(self):  # Pull highest from heap (Tricky!)
        if self.is_empty():
            raise IndexError("You can't pull from an empty heap")

        # base case
        if self.get_size() == 1:
            return self.array.pop()

        largest = self.array[0]

        self.array[0] = self.array.pop()
        size = self.get_size()
        index = 0

        while (index * 2) + 1 < size:
            left_child = (2 * index) + 1
            right_child = (2 * index) + 2
            left_value = self.array[left_child]

            largest_child = left_child

            if right_child < size:
                right_value = self.array[right_child]
                if right_value > left_value:
                    largest_child = right_child

            if self.array[index] >= self.array[largest_child]:
                break

            temp = self.array[index]
            self.array[index] = self.array[largest_child]
            self.array[largest_child] = temp
            index = largest_child

        return largest

    def __next__(self):
        if self.pos < self.get_size():
            res = self.array[self.pos]
            if res is None:
                self.pos += 1
                res = self.array[self.pos]
            self.pos += 1
            return res
        else:
            raise StopIteration

    def __iter__(self):     # Support for iteration over all elements
        self.pos = 0
        return self
