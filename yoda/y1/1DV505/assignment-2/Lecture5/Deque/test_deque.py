import pytest
import Deque as deq


def test_add_last():
    deque = deq.Deque()
    for i in range(1, 5):
        deque.add_last(i)

    excepted_output = "{ 1 2 3 4 }"
    assert str(deque) == excepted_output


def test_add_first():
    deque = deq.Deque()
    for i in range(1, 5):
        deque.add_first(i)

    excepted_output = "{ 4 3 2 1 }"
    assert str(deque) == excepted_output


def test_empty():
    deque = deq.Deque()
    assert deque.size == 0
    assert deque.is_empty() is True
    assert str(deque) == "{ }"

    deque.add_first(1)
    assert deque.is_empty() is False


def test_iteration():
    deque = deq.Deque()
    for i in range(5):
        deque.add_last(i)

    deque_output = [i for i in deque]
    assert deque_output == [0, 1, 2, 3, 4]


def test_get_first():
    deque = deq.Deque()

    for i in range(1, 11):
        deque.add_first(i)

    assert deque.get_first() == 10

    while not deque.is_empty():
        deque.remove_first()

    with pytest.raises(IndexError):
        deque.get_first()


def test_get_last():
    deque = deq.Deque()
    expected_output = 1

    for i in range(expected_output, 11):
        deque.add_first(i)

    assert deque.get_last() == expected_output

    while not deque.is_empty():
        deque.remove_first()

    with pytest.raises(IndexError):
        deque.get_last()


def test_remove_first():
    deque = deq.Deque()
    excepted_output = "{ 9 8 7 6 5 4 3 2 1 }"
    for i in range(1, 11):
        deque.add_first(i)

    deque.remove_first()
    assert str(deque) == excepted_output
    assert deque.size == 9

    while not deque.is_empty():
        deque.remove_first()

    assert str(deque) == "{ }"
    assert deque.is_empty() is True
    assert deque.size == 0


def test_remove_last():
    deque = deq.Deque()
    excepted_output = "{ 10 9 8 7 6 5 4 3 2 }"
    for i in range(1, 11):
        deque.add_first(i)

    deque.remove_last()
    assert str(deque) == excepted_output
    assert deque.size == 9

    while not deque.is_empty():
        deque.remove_last()

    assert str(deque) == "{ }"
    assert deque.is_empty() is True
    assert deque.size == 0
