package main

import "fmt"

type List[T any] struct {
	head, tail *Node[T]
}

type Node[T any] struct {
	value T
	next  *Node[T]
}

func (l *List[T]) Push(v T) {
	node := &Node[T]{value: v}
	if l.head == nil {
		l.head = node
	} else {
		l.tail.next = node
	}
	l.tail = node
}

func (l *List[T]) GetAll() []T {
	values := make([]T, 0)
	for node := l.head; node != nil; node = node.next {
		values = append(values, node.value)
	}
	return values
}

func main() {
	lst := List[int]{}
	lst.Push(10)
	lst.Push(11)
	lst.Push(12)
	fmt.Println(lst.GetAll())
}