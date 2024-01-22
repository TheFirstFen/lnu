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
	list := List[int]{}
	list.Push(1)
	list.Push(2)
	list.Push(3)
	fmt.Println(list.GetAll())
}