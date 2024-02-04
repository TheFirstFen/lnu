package main

import (
	"fmt"
	"sync"
)

type Heap struct {
	data []int
	mu   sync.Mutex
}

func NewHeap() *Heap {
	return &Heap{data: make([]int, 0)}
}

func (h *Heap) Push(value int) {
	h.mu.Lock()
	defer h.mu.Unlock()
	h.data = append(h.data, value)
	h.heapifyUp(len(h.data) - 1)
}

func (h *Heap) Pop() (int, error) {
	h.mu.Lock()
	defer h.mu.Unlock()
	if len(h.data) == 0 {
		return 0, fmt.Errorf("Heap is empty")
	}
	min := h.data[0]
	last := len(h.data) - 1
	h.data[0] = h.data[last]
	h.data = h.data[:last]
	if len(h.data) > 1 {
		h.heapifyDown(0)
	}
	return min, nil
}

func (h *Heap) heapifyUp(idx int) {
	parent := (idx - 1) / 2
	for idx > 0 && h.data[idx] < h.data[parent] {
		h.data[idx], h.data[parent] = h.data[parent], h.data[idx]
		idx = parent
		parent = (idx - 1) / 2
	}
}

func (h *Heap) heapifyDown(idx int) {
	last := len(h.data) - 1
	leftCh := 2*idx + 1
	for leftCh <= last {
		minC := leftCh
		rightCh := leftCh + 1
		if rightCh <= last && h.data[rightCh] < h.data[leftCh] {
			minC = rightCh
		}
		if h.data[idx] <= h.data[minC] {
			break
		}
		h.data[idx], h.data[minC] = h.data[minC], h.data[idx]
		idx = minC
		leftCh = 2*idx + 1
	}
}

func main() {
	heap := NewHeap()
	wg := sync.WaitGroup{}
	numWorkers := 4 // * Adjustable

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()

			for j := 0; j < 3; j++ {
				heap.Push(id*10 + j)
				fmt.Printf("Worker %d pushed %d\n", id, id*10+j)
			}

			for j := 0; j < 2; j++ {
				value, err := heap.Pop()
				if err != nil {
					fmt.Printf("Worker %d: %v\n", id, err)
					continue
				}
				fmt.Printf("Worker %d popped %d\n", id, value)
			}
		}(i)
	}

	wg.Wait()

	fmt.Println("Final heap:", heap.data)
}
