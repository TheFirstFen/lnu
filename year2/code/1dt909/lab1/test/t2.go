package main

//TODO: Implement all functions

import (
	"fmt"
	"sync"
)

type Node struct {
	val int
	nxt *Node
	sync.Mutex
}

type Deque struct {
	head *Node
	tail *Node
	sync.Mutex
}

func NewDeque() *Deque {
	return &Deque{}
}

// ? Is this needed when only adding at front and back????
func (dq *Deque) Find(k int) (pred *Node, curr *Node) {
	pred = dq.head
	curr = dq.head.nxt
	pred.Lock()
	curr.Lock()
	for curr.val < k {
		pred.Unlock()
		pred = curr
		curr = curr.nxt
		curr.Lock()
	}

	return pred, curr
}

func (dq *Deque) Contains(k int) bool {
	pred, curr := dq.Find(k)
	defer pred.Unlock()
	defer curr.Unlock()

	return curr.val == k
}

// * Works sequentially
func (dq *Deque) PushFront(k int) {
	if dq.head == nil { // * Size: 0
		dq.Lock()
		if dq.head == nil {
			dq.head = &Node{val: k}
			dq.tail = dq.head
			dq.Unlock()
		} else {
			dq.Unlock()
			dq.PushFront(k)
		}
	} else if dq.head == dq.tail { // * Size: 1
		dq.Lock()
		if dq.head == dq.tail {
			dq.head = &Node{val: k, nxt: dq.tail}
			dq.Unlock()
		} else {
			dq.Unlock()
			dq.PushFront(k)
		}
	} else { // * Size: >1
		prevHead := dq.head
		prevHead.Lock()
		dq.head = &Node{val: k, nxt: prevHead}
		prevHead.Unlock()
	}
}

// * Works sequentially
func (dq *Deque) PushBack(k int) {
	dq.Lock()
	if dq.tail == nil { // * Size: 0
		dq.tail = &Node{val: k}
		dq.head = dq.tail
		dq.Unlock()
	} else if dq.tail == dq.head { // * Size: 1
		dq.tail = &Node{val: k}
		dq.head.nxt = dq.tail
		dq.Unlock()
	} else { // * Size: >1
		dq.Unlock()
		newNode := &Node{val: k}
		newNode.Lock()
		dq.tail.Lock()
		defer dq.tail.Unlock()
		// * Need to unlock old tail
		dq.tail.nxt = newNode
		dq.tail = newNode
	}
}

func (dq *Deque) PopFront() bool {
	return false
}

func (dq *Deque) PopBack() bool {
	return false
}

func (dq *Deque) Print() {
	dq.Lock()
	defer dq.Unlock()

	for curr := dq.head; curr != nil; curr = curr.nxt {
		fmt.Printf("%d ", curr.val)
	}
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
				//fmt.Printf("Worker %d, skipped\n", id)
				// deque.PushBack(id)
			}
		}(id)
	}

	wg.Wait()

	deque.Print()
}
