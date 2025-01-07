import heap.Heap as hp

print("Heap demo starts\n")
heap = hp.Heap()

for i in range(1, 11):
    heap.add(i)

print(heap)
print("Size:", heap.get_size())

print("\npeek():", heap.peek())
print("pull_high():", heap.pull_high())
print(heap)
print("Size:", heap.get_size())
print("is_empty():", heap.is_empty())

print("\nTest iteration")
for j in heap:
    print(j, end=" ")
print()

print("\nTest remove all elements")
heap = hp.Heap()
for i in range(20, 31):
    heap.add(i)
print("After adding elements:", heap)

while not heap.is_empty():
    heap.pull_high()

print("After removing all elements:", heap)
print("Size:", heap.get_size())
print("is_empty():", heap.is_empty())

print("\nAccessing an empty heap")
empty = hp.Heap()
try:
    heap.peek()
except IndexError as exc:
    print("peek:", exc)

try:
    heap.pull_high()
except IndexError as exc:
    print("pull_high:", exc)
