import deque as deq


empty = deq.Deque()
deque = deq.Deque()

for i in range(1, 11):
    deque.add_last(i)
print(deque.to_string())
print("Size:", deque.size)

for i in range(11, 21):
    deque.add_first(i)
print(deque.to_string())
print("Size:", deque.size)

print("\nget_last():", deque.get_last())
print("get_last() on empty deque:", empty.get_last())

print("\nget_first():", deque.get_first())
print("get_first() on empty deque:", empty.get_first())

print("\nremove_first():", deque.remove_first())
print("remove_first() on empty deque:", empty.remove_first())

print("\nremove_last():", deque.remove_last())
print("remove_last() on empty deque:", empty.remove_last())

print(deque.to_string())
print("Size:", deque.size)

print("\nTest to remove all elements")
temp = deq.Deque()
for i in range(100, 106):
    temp.add_first(i)
print("After adding elements:", temp.to_string())
while temp.size > 0:
    temp.remove_last()
print("After removing all elements:", temp.to_string())
print("Size:", temp.size)
