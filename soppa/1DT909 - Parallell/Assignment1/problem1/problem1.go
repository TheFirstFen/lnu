package main

import (
	"fmt"
	"sync"
)

type BinaryHeap struct {
	values []int
	mu     sync.Mutex
}

func NewBinaryHeap() *BinaryHeap {
	return &BinaryHeap{}
}

func (h *BinaryHeap) Insert(value int) {
	h.mu.Lock()
	defer h.mu.Unlock()
	h.values = append(h.values, value)
	h.heapify(len(h.values) - 1)
}

func (h *BinaryHeap) heapify(index int) {
	for index > 0 {
		pIndex := (index - 1) / 2
		if h.values[index] >= h.values[pIndex] {
			break
		}
		h.values[index], h.values[pIndex] = h.values[pIndex], h.values[index]
		pIndex = index
	}
}

func (h *BinaryHeap) ExtractMin() int {
	h.mu.Lock()
	defer h.mu.Unlock()
	if len(h.values) == 0 {
		fmt.Println("Empty heap!")
		return 0
	}
	minVal := h.values[0]
	h.values[0] = h.values[len(h.values)-1]
	h.values = h.values[:len(h.values)-1]
	h.sink()
	return minVal
}

func (h *BinaryHeap) sink() {
	index := 0
	for {

		leftChildIndex := 2*index + 1
		rightChildIndex := 2*index + 2
		smallestIndex := index

		if leftChildIndex < len(h.values) && h.values[leftChildIndex] < h.values[smallestIndex] {
			smallestIndex = leftChildIndex
		}
		if rightChildIndex < len(h.values) && h.values[rightChildIndex] < h.values[smallestIndex] {
			smallestIndex = rightChildIndex
		}
		if smallestIndex == index {
			break
		}
		h.values[index], h.values[smallestIndex] = h.values[smallestIndex], h.values[index]

		index = smallestIndex
	}
}

func (h *BinaryHeap) Size() int {
	h.mu.Lock()
	defer h.mu.Unlock()
	return len(h.values)
}

func main() {
	var wg sync.WaitGroup

	heap := NewBinaryHeap()

	numWorkers := 10

	numOfOperations := 1000

	wg.Add(numWorkers)

	for i := 0; i < numWorkers; i++ {
		go func() {
			defer wg.Done()
			for j := 0; j < numOfOperations; j++ {
				heap.Insert(j)
				heap.ExtractMin()
			}
		}()
	}

	wg.Wait()

	fmt.Println(heap.Size())
}
