class QuadHash:
    def __init__(self, capacity=11):
        self._size = capacity
        self._count = 0
        self._table = [None] * capacity

    def hash_function(self, key):
        hash_value = key.__hash__()

        if hash_value <= 0:
            hash_value = -hash_value

        return hash_value % self._size

    # It is always a good idea to increase the size of the table with a prime number
    # This is especially true for open addressing algorithms
    # This function calculates the next available prime when doubling
    # The return value should be that number
    def _next_prime(self, n):
        def is_prime(n):

            if n < 2:
                return False

            if n == 2:
                return True

            if n % 2 == 0:
                n += 1
            # checks from the first odd number to the square root of n
            # and skips all even numbers
            for i in range(3, (int(n**0.5)+1), 2):
                if n % i == 0:
                    return False
            return True

        if n % 2 == 0:
            n += 1

        while not is_prime(n):
            n += 1
        return n

    def _rehash(self):
        old_table = self._table

        new_size = self._next_prime(self._size * 2)
        self._table = [None] * new_size
        self._count = 0
        self._size = new_size

        for value in old_table:
            if value is not None:
                self.add(value)

    def add(self, key):
        # rehash?
        if self._count / self._size > 0.75:
            self._rehash()

        index = self.hash_function(key)
        original_index = index

        # quadratic probing
        i = 0
        while self._table[index] is not None:
            if self._table[index] == key:
                return     # key already exists
            i += 1
            index = (original_index + i ** 2) % self._size
        # insert new key and new index
        self._table[index] = key
        self._count += 1

    def contains(self, key):
        position = self.hash_function(key)
        original_index = position
        i = 1
        while self._table[position] is not None:
            if self._table[position] == key:
                return True
            position = (original_index + i ** 2) % self._size
            i += 1
            if position == original_index:
                break
        return False

    def get(self, key):
        position = self.hash_function(key)
        original_index = position
        i = 1
        while self._table[position] is not None:
            if self._table[position] == key:
                return self._table[position]
            position = (original_index + i ** 2) % self._size
            i += 1
            if position == original_index:
                break
        return None

    def __str__(self):
        result = ''
        for i in range(self._size):
            result += f'[{i}]: '
            result += str(self._table[i])

            result += '\n'

        return result

    def __iter__(self):
        return QuadHashIterator(self)


class QuadHashIterator:
    def __init__(self, hash_table):
        self._table = hash_table._table
        self._current = 0
        self._size = hash_table._size

    def __next__(self):
        while self._current < self._size:
            item = self._table[self._current]
            self._current += 1
            if item is not None:
                return item
        raise StopIteration
