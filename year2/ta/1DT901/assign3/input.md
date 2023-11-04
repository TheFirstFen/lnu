# Note: run all from "assign3" folder

G:
recursive_print:
run()

read_numbers:
run() ->
mean= 501.5, std=290.1
mean= 2.4, std=289.4

occurrences:
run() -> random

deque_main:
run() -> [
{ 1 2 3 4 5 6 7 8 9 10 }
Size: 10
{ 20 19 18 17 16 15 14 13 12 11 1 2 3 4 5 6 7 8 9 10 }
Size: 20

    get_last(): 10
    You can't access an empty queue
    get_last() on empty deque: None

    get_first(): 20
    You can't access an empty queue
    get_first() on empty deque: None

    remove_first(): 20
    You can't access an empty queue
    remove_first() on empty deque: None

    remove_last(): 10
    You can't access an empty queue
    remove_last() on empty deque: None
    { 19 18 17 16 15 14 13 12 11 1 2 3 4 5 6 7 8 9 }
    Size: 18

    Test to remove all elements
    After adding elements: { 105 104 103 102 101 100 }
    After removing all elements: { }
    Size: 0

]

VG:
pretty_recursive_print:
run()

count_lines:
run() -> 6689 or ~5800 if not counting comments
