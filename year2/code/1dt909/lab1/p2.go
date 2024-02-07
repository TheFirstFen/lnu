package main

// ? Lås Noden du arbetar på samt next & prev
// * Sök upp hand over hand locking

import (
	"errors"
	"fmt"
	"sync"
)

type Node struct {
	value int
	next  *Node
	prev  *Node
	sync.Mutex
}

type Deque struct {
	head *Node
	tail *Node
	size int
	sync.Mutex
}

func NewDeque() *Deque {
	return &Deque{}
}

func (dq *Deque) AddFront(value int) {
	dq.Lock()
	defer dq.Unlock()

	newNode := &Node{value: value}

	if dq.head == nil {
		dq.head = newNode
		dq.tail = newNode
	} else {
		newNode.next = dq.head
		dq.head.prev = newNode
		dq.head = newNode
	}

	dq.size++
}

func (dq *Deque) AddBack(value int) {
	dq.Lock()
	defer dq.Unlock()

	newNode := &Node{value: value}

	if dq.tail == nil {
		dq.head = newNode
		dq.tail = newNode
	} else {
		newNode.prev = dq.tail
		dq.tail.next = newNode
		dq.tail = newNode
	}

	dq.size++
}

func (dq *Deque) RemoveFront() (int, error) {
	dq.Lock()
	defer dq.Unlock()

	if dq.size == 0 {
		return 0, errors.New("Deque is empty")
	}

	value := dq.head.value
	dq.head = dq.head.next
	if dq.head != nil {
		dq.head.prev = nil
	} else {
		dq.tail = nil
	}
	dq.size--
	return value, nil
}

func (dq *Deque) RemoveBack() (int, error) {
	dq.Lock()
	defer dq.Unlock()

	if dq.size == 0 {
		return 0, errors.New("Deque is empty")
	}

	value := dq.tail.value
	dq.tail = dq.tail.prev
	if dq.tail != nil {
		dq.tail.next = nil
	} else {
		dq.head = nil
	}
	dq.size--
	return value, nil
}

func (dq *Deque) Size() int {
	dq.Lock()
	defer dq.Unlock()

	return dq.size
}

func (dq *Deque) Print() {
	dq.Lock()
	defer dq.Unlock()

	fmt.Print("Deque: ")
	current := dq.head
	for current != nil {
		fmt.Print(current.value, " ")
		current = current.next
	}
	fmt.Println()
}

func main() {
	deque := NewDeque()
	wg := sync.WaitGroup{}
	numWorkers := 1024

	for id := 0; id < numWorkers; id++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()

			if id%2 == 0 {
				deque.AddFront(id*10 + 1)
			} else {
				deque.AddBack(id*10 + 2)
			}
		}(id)
	}

	wg.Wait()

	fmt.Println("Deque size:", deque.Size())
	//deque.Print()
	fmt.Println()

	for i := 0; i < numWorkers/2; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()

			if i%2 == 0 {
				if val, err := deque.RemoveFront(); err != nil {
					fmt.Println(err)
					return
				} else {
					fmt.Println("Popping from front:", val)
				}
			} else {
				if val, err := deque.RemoveBack(); err != nil {
					fmt.Println(err)
					return
				} else {
					fmt.Println("Popping from back:", val)
				}
			}
		}(i)
	}

	wg.Wait()

	fmt.Println("\nDeque size:", deque.Size())
	//deque.Print()
}
