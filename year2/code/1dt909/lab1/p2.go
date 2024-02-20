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
	lockN sync.Mutex
}

type Deque struct {
	head  *Node
	tail  *Node
	size  int
	lockD sync.Mutex
}

func NewDeque() *Deque {
	return &Deque{}
}

func (d *Deque) PushFront(val int) {
	newNode := &Node{value: val}
	newNode.lockN.Lock()
	defer newNode.lockN.Unlock()

	if d.head == nil {
		d.head = newNode
		d.tail = newNode
	} else {
		d.head.prev = newNode
		newNode.next = d.head
		d.head = newNode
	}

	d.size++
}

func (d *Deque) PushBack(val int) {
	newNode := &Node{value: val}
	newNode.lockN.Lock()
	defer newNode.lockN.Unlock()

	if d.tail == nil {
		d.head = newNode
		d.tail = newNode
	} else {
		d.tail.next = newNode
		newNode.prev = d.tail
		d.tail = newNode
	}

	d.size++
}

func (d *Deque) PopFront() (int, error) {
	if d.head == nil {
		return 0, errors.New("Deque is empty")
	}

	d.head.lockN.Lock()
	defer d.head.lockN.Unlock()

	value := d.head.value
	if d.head == d.tail {
		d.head = nil
		d.tail = nil
	} else {
		d.head = d.head.next
		d.head.prev = nil
	}

	d.size--
	return value, nil
}

func (d *Deque) PopBack() (int, error) {
	if d.tail == nil {
		return 0, errors.New("Deque is empty")
	}

	d.tail.lockN.Lock()
	defer d.tail.lockN.Unlock()

	value := d.tail.value
	if d.tail == d.head {
		d.head = nil
		d.tail = nil
	} else {
		d.tail = d.tail.prev
		d.tail.next = nil
	}

	d.size--
	return value, nil
}

func (d *Deque) Size() int {
	d.lockD.Lock()
	defer d.lockD.Unlock()

	return d.size
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
				deque.PushFront(id)
			} else {
				deque.PushBack(id)
			}
		}(id)
	}

	wg.Wait()

	fmt.Println("Deque size:", deque.Size())
	fmt.Println()

	for i := 0; i < numWorkers/2; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()

			if i%2 == 0 {
				if val, err := deque.PopFront(); err != nil {
					fmt.Println(err)
					return
				} else {
					fmt.Println("Popping from front:", val)
				}
			} else {
				if val, err := deque.PopBack(); err != nil {
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
}
