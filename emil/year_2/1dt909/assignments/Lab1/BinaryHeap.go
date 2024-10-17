package main

import (
	"fmt"
	"sync"
    "math/rand"
)

const nr_insert = 100
const randInterval = 100
const numWorkers = 256

type BinaryHeap struct {
	arr  []int
	lock sync.Mutex
}

func NewBinaryHeap() *BinaryHeap {
	return &BinaryHeap{
        arr: make([]int, 0),
    }
}

func (h *BinaryHeap) Insert(value int) {
	h.lock.Lock()
	defer h.lock.Unlock()

	h.arr = append(h.arr, value)
    h.bubbleUp(len(h.arr) - 1)
}

func (h *BinaryHeap) bubbleUp(id int) {
    parentid := (id - 1) / 2
    for id > 0 && h.less(id, parentid) {
        h.swap(id, parentid)
        id = parentid
        parentid = (id - 1) / 2
    }
}

func (h *BinaryHeap) Pop() (interface{}, error) {
    h.lock.Lock()
    defer h.lock.Unlock()

    if h.IsEmpty() {
        return nil, fmt.Errorf("heap is empty")
    }

    root := h.arr[0]
    lastId := len(h.arr) - 1 
    h.arr[0] = h.arr[lastId]
    h.arr = h.arr[:lastId]

    if len(h.arr) > 1 {
        h.bubbleDown(0)
    }

    return root, nil
}

func (h *BinaryHeap) bubbleDown (id int) {
    lastId := len(h.arr) - 1

    for {
        left := 2 * id + 1
        right := left + 1
        smallest := id

        if left <= lastId && h.less(left, smallest) {
            smallest = left
        }
        if right <= lastId && h.less(right, smallest) {
            smallest = right
        }
        if smallest == id {
            break
        }
        h.swap(id, smallest)
        id = smallest
    }
}

func (h *BinaryHeap) less(i, j int) bool {
	return h.arr[i] < h.arr[j]
}

func (h *BinaryHeap) swap(i, j int) {
	h.arr[i], h.arr[j] = h.arr[j], h.arr[i]
}

func (h *BinaryHeap) IsEmpty() bool {
    return len(h.arr) == 0
}

func main() {
	heap := NewBinaryHeap()
    var wg sync.WaitGroup

    for i := 0; i < numWorkers ; i++ {
        wg.Add(1)

        go func(i int) {
            defer wg.Done()

            for j := 0; j < 10; j++ {
                randVal := rand.Intn(1000)
                heap.Insert(randVal)
                fmt.Printf("Inserted: %d\n", randVal)
            }

            for j := 0; j < 5; j++ {
                value, err := heap.Pop()
                if err != nil {
                    fmt.Printf("Worker %d: %v\n", i, err)
                    continue
                }
                fmt.Printf("Popped: %d\n", value)
            }
        }(i)
    }

    wg.Wait()
    fmt.Print("Heap: ", heap.arr)
}
