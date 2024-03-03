package main

import (
	"fmt"
	"math"
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
	fixedTail := &Node{val: math.MaxInt, nxt: nil}
	fixedHead := &Node{val: math.MinInt, nxt: fixedTail}
	return &Deque{head: fixedHead, tail: fixedTail}
}

func (dq *Deque) Find(k string, val any) (pred *Node, curr *Node) {
	pred = dq.head
	pred.Lock()
	curr = dq.head.nxt
	curr.Lock()
	if k == "pushBack" {
		for curr.val != math.MaxInt {
			pred.Unlock()
			pred = curr
			curr = curr.nxt
			curr.Lock()
		}
	} else if k == "popBack" {
		for curr.nxt.val != math.MaxInt {
			pred.Unlock()
			pred = curr
			curr = curr.nxt
			curr.Lock()
		}
	} else if k == "contains" && val != nil {
		for curr.val != val {
			if curr.val == math.MaxInt {
				break
			}
			pred.Unlock()
			pred = curr
			curr = curr.nxt
			curr.Lock()
		}
	}

	return pred, curr
}

func (dq *Deque) Contains(k int) bool {
	pred, curr := dq.Find("contains", k)
	defer pred.Unlock()
	defer curr.Unlock()

	return curr.val == k
}

func (dq *Deque) PushFront(k int) {
	pred := dq.head
	pred.Lock()
	curr := dq.head.nxt
	curr.Lock()
	defer pred.Unlock()
	defer curr.Unlock()

	n := Node{val: k, nxt: curr}
	pred.nxt = &n
}

func (dq *Deque) PushBack(k int) {
	pred, curr := dq.Find("pushBack", nil)
	defer pred.Unlock()
	defer curr.Unlock()

	n := Node{val: k, nxt: curr}
	pred.nxt = &n
}

func (dq *Deque) PopFront() {
	pred := dq.head
	pred.Lock()
	curr := dq.head.nxt
	curr.Lock()
	defer pred.Unlock()
	defer curr.Unlock()

	if curr.val != math.MaxInt {
		pred.nxt = curr.nxt
	}
}

func (dq *Deque) PopBack() {
	pred, curr := dq.Find("popBack", nil)
	defer pred.Unlock()
	defer curr.Unlock()

	if curr.val != math.MaxInt {
		pred.nxt = curr.nxt
	}
}

func (dq *Deque) Print() {
	dq.Lock()
	defer dq.Unlock()

	c := 0

	fmt.Print("[ ")
	for curr := dq.head; curr != nil; curr = curr.nxt {
		if (curr == dq.head) || (curr == dq.tail) {
			continue
		}
		fmt.Printf("%d ", curr.val)
		c++
	}
	fmt.Print("]\n")
	fmt.Printf("Count: %d\n", c)
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

	for id := 0; id < numWorkers/2; id++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()

			if id%2 == 0 {
				deque.PopBack()
			} else {
				deque.PopFront()
			}
		}(id)
	}

	wg.Wait()

	deque.Print()
}
