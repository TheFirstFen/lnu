from heap.Heap import Heap
from heap.Task import Task

heap = Heap()
todo = [Task(88, "Study physics"), Task(43, "Pay bills"),
        Task(60, "Go to school"), Task(60, "Buy dinner"),
        Task(99, "Drink beer"), Task(79, "Eat breakfast"), Task(7, "Sleep"),
        Task(1, "Go to the gym"), Task(100, "Eat dinner"),
        Task(100, "Study python2 course"),]

for task in todo:
    heap.add(task)


while not heap.is_empty():
    print(heap.pull_high())
