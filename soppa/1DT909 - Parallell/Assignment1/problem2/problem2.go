package main

import (
	"fmt"
	"math"
	"sync"
)

type Node struct {
	nxt *Node
	key int
	mu  sync.Mutex
}

type Deque struct {
	head, tail *Node
	size       int
}

func NewDeque() *Deque {
	head := Node{key: math.MaxInt}
	tail := Node{key: math.MinInt}
	head.nxt = &tail

	return &Deque{head: &head, tail: &tail}
}

func (q *Deque) AddFront(k int) {
	prev := q.head
	prev.mu.Lock()
	defer prev.mu.Unlock()
	curr := prev.nxt
	n := Node{key: k, nxt: curr}
	prev.nxt = &n
	q.size++
}
func (q *Deque) RemoveFront() {
	prev := q.head
	prev.mu.Lock()
	defer prev.mu.Unlock()
	curr := prev.nxt
	prev.nxt = curr.nxt
	q.size--
}
func (q *Deque) find() (prev *Node, curr *Node) {
	prev = q.head
	prev.mu.Lock()
	curr = prev.nxt
	if curr == q.tail {
		curr.mu.Lock()
		return prev, curr
	}
	curr.mu.Lock()
	for curr.nxt != q.tail {
		prev.mu.Unlock()
		prev = curr
		curr = curr.nxt
		curr.mu.Lock()
	}
	return prev, curr
}
func (q *Deque) AddBack(k int) {
	prev, curr := q.find()
	defer prev.mu.Unlock()
	defer curr.mu.Unlock()
	n := Node{key: k, nxt: q.tail}
	curr.nxt = &n
	q.size++
}

func (q *Deque) RemoveBack() {
	prev, curr := q.find()
	defer prev.mu.Unlock()
	defer curr.mu.Unlock()
	prev.nxt = q.tail
	q.size--
}

func main() {
	q := NewDeque()

	wg := sync.WaitGroup{}
	numWorkers := 1000

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()

			if i%2 == 1 {
				q.AddFront(i)
			} else {
				q.AddBack(i)
			}
		}(i)
	}
	wg.Wait()

	fmt.Println("Deque size: ", q.size)

	for i := 0; i < numWorkers/4; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			if i%2 == 1 {
				q.RemoveFront()
			} else {
				q.RemoveBack()
			}
		}(i)
	}
	wg.Wait()

	fmt.Println("Deque size: ", q.size)
}
