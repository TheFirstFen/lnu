import Deque as deq

# Program starts
print("Deque demo starts\n")
deque = deq.Deque()

# Add 10 integers using add_last and print list content
for i in range(1, 11):
    deque.add_last(i)
print(deque)
print("Size:", deque.size)

# Add 10 integers using add_first and print list content
for i in range(11, 21):
    deque.add_first(i)
print(deque)
print("Size:", deque.size)

# Demo get_last, get_first, remove_first, remove_last
print("\nget_last():", deque.get_last())
print("get_first():", deque.get_first())
print("remove_first():", deque.remove_first())
print("remove_last():", deque.remove_last())
print(deque)
print("Size:", deque.size)
print("is_empty():", deque.is_empty())


# Test add and remove all
print("\nTest to remove all elements")
deque = deq.Deque()   # A new empty deque
for i in range(100, 106):
    deque.add_first(i)
print("After adding elements:", deque)

while not deque.is_empty():
    deque.remove_last()
print("After removing all elements:", deque)
print("Size:", deque.size)
print("is_empty():", deque.is_empty())

# Demo iterator  (Part of Lecture 6)
print("\nIterator test")
deque = deq.Deque()   # A new empty deque
for i in range(1, 11):  # ==> 1,2,3,...,9,10
    deque.add_last(i)
for n in deque:
    print(n, end=" ")
print()

# Demo exceptions
print("\nAccessing an empty deque")
empty = deq.Deque()     # An empty deque
try:
    empty.get_last()
except IndexError as exc:
    print("get_last:", exc)

try:
    empty.get_first()
except IndexError as exc:
    print("get_first:", exc)

try:
    empty.remove_first()
except IndexError as exc:
    print("remove_first:", exc)

try:
    empty.remove_last()
except IndexError as exc:
    print("remove_last:", exc)
