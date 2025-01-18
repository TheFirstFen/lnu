class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element

    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    def addFirst(self, e):
        newNode = Node(e)
        newNode.next = self.__head
        self.__head = newNode
        self.__size += 1

        if self.__tail is None:
            self.__tail = self.__head

    def addLast(self, e):
        newNode = Node(e)
        if self.__tail is None:
            self.__head = self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = self.__tail.next

        self.__size += 1

    def add(self, e):
        self.addLast(e)

    def insert(self, index, e):
        if index == 0:
            self.addFirst(e)
        elif index >= self.__size:
            self.addLast(e)
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    def removeFirst(self):
        if self.__size == 0:
            return None
        else:
            temp = self.__head
            self.__head = self.__head.next
            self.__size -= 1
            if self.__head is None:
                self.__tail = None
            return temp.element

    def removeLast(self):
        if self.__size == 0:
            return None
        elif self.__size == 1:
            temp = self.__head
            self.__head = self.__tail = None
            self.__size = 0
            return temp.element
        else:
            current = self.__head
            for i in range(self.__size - 2):
                current = current.next

            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None
        elif index == 0:
            return self.removeFirst()
        elif index == self.__size - 1:
            return self.removeLast()
        else:
            previous = self.__head
            for i in range(1, index):
                previous = previous.next

            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    def isEmpty(self):
        return self.__size == 0

    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["
        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current is not None:
                result += ", "
            else:
                result += "]"
        return result

    def clear(self):
        self.__head = self.__tail = None
        self.__size = 0

    def contains(self, e):
        current = self.__head
        while current is not None:
            if current.element == e:
                return True
            current = current.next
        return False

    def remove(self, e):
        current = self.__head
        previous = None
        while current is not None:
            if current.element == e:
                if previous is None:
                    self.__head = current.next
                else:
                    previous.next = current.next
                self.__size -= 1
                if current.next is None:
                    self.__tail = previous
                return True
            previous = current
            current = current.next
        return False

    def get(self, index):
        if index < 0 or index >= self.__size:
            return None
        current = self.__head
        for i in range(index):
            current = current.next
        return current.element

    def indexOf(self, e):
        current = self.__head
        index = 0
        while current is not None:
            if current.element == e:
                return index
            current = current.next
            index += 1
        return -1

    def lastIndexOf(self, e):
        current = self.__head
        index = 0
        last_index = -1
        while current is not None:
            if current.element == e:
                last_index = index
            current = current.next
            index += 1
        return last_index

    def set(self, index, e):
        if index < 0 or index >= self.__size:
            return None
        current = self.__head
        for i in range(index):
            current = current.next
        old_value = current.element
        current.element = e
        return old_value

    def __getitem__(self, index):
        return self.get(index)

    def __iter__(self):
        return LinkedListIterator(self.__head)

class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element
