package main

import (
	"fmt"
	"math"
	"sync"
)

const numWorkers = 1024

type Deque struct {
    head *Node
    tail *Node
	mu   sync.Mutex
   
}

type Node struct {
    value int
    next  *Node
	mu    sync.Mutex
}

func NewDeque() *Deque {
	max := math.MaxInt
	min := math.MinInt
	startTail := &Node{value: max, next: nil}
	startHead := &Node{value: min, next: startTail}
	return &Deque{head: startHead, tail: startTail}
}

func (d *Deque) PushHead(value int) {
    pred := d.head
	pred.mu.Lock()
	curr := d.head.next
	curr.mu.Lock()
	defer pred.mu.Unlock()
	defer curr.mu.Unlock()

	newNode := &Node{value: value, next: curr}
	pred.next = newNode
}

func (d *Deque) PopHead() {
	pred := d.head
	pred.mu.Lock()
	curr := d.head.next
	curr.mu.Lock()
	defer pred.mu.Unlock()
	defer curr.mu.Unlock()

	if curr.value != math.MaxInt {
		pred.next = curr.next
	}
}

func (d *Deque) PushTail(value int) {
	pred, curr := d.FindPushTail()
	defer pred.mu.Unlock()
	defer curr.mu.Unlock()

	newNode := &Node{value: value, next: curr}
	pred.next = newNode
}

func (d *Deque) FindPushTail() (pred *Node, curr *Node) {
	pred = d.head
	pred.mu.Lock()
	curr = d.head.next
	curr.mu.Lock()

	for curr.value != math.MaxInt {
		pred.mu.Unlock()
		pred = curr
		curr = curr.next
		curr.mu.Lock()
	}

	return pred, curr
}

func (d *Deque) PopTail() {
	pred, curr := d.FindPopTail()
	defer pred.mu.Unlock()
	defer curr.mu.Unlock()

	if curr.value != math.MaxInt {
		pred.next = curr.next
	}
}

func (d *Deque) FindPopTail() (pred *Node, curr *Node) {
	pred = d.head
	pred.mu.Lock()
	curr = d.head.next
	curr.mu.Lock()

	for curr.value != math.MaxInt {
		pred.mu.Unlock()
		pred = curr
		curr = curr.next
		curr.mu.Lock()
	}

	return pred, curr
}

func (d *Deque) Contains(value int) bool {
	pred, curr := d.FindContains(value)
	defer pred.mu.Unlock()
	defer curr.mu.Unlock()

	return curr.value == value
}

func (d *Deque) FindContains(value any) (pred *Node, curr *Node) {
	pred = d.head
	pred.mu.Lock()
	curr = d.head.next
	curr.mu.Lock()

	for curr.value != value {
		if curr.value == math.MaxInt {
			break
		}
		pred.mu.Unlock()
		pred = curr
		curr = curr.next
		curr.mu.Lock()
	}

	return pred, curr
}

func (d *Deque) PrintQueue() {
	d.mu.Lock()
	defer d.mu.Unlock()
	count := 0

	for curr := d.head; curr != nil; curr = curr.next {
		if (curr == d.head) || (curr == d.tail) {
			continue
		}
		fmt.Printf("%d ", curr.value)
		count++
	}
}

func main() {
	deque := NewDeque()
	wg := sync.WaitGroup{}

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			if i%2 == 0 {
				deque.PushHead(i)
			} else {
				deque.PushTail(i)
			}
		}(i)
	}

	for i := 0; i < numWorkers/2; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			if i%2 == 0 {
				deque.PopHead()
			} else {
				deque.PopTail()
			}
		}(i)
	}

	wg.Wait()

	deque.PrintQueue()

	fmt.Println("\nDeque contains 25: ", deque.Contains(25)) // Might be false due to race condition
	fmt.Println("Deque contains 1025: ", deque.Contains(1025)) // always false due to numWorers < 1025
}
