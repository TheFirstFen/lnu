package main

import (
	"fmt"
	"sync"
)

type CountingSemaphore struct {
	count int
	mu    sync.Mutex
	cond  *sync.Cond
}

func NewCountingSemaphore(initCount int) *CountingSemaphore {
	sem := &CountingSemaphore{count: initCount}

	sem.cond = sync.NewCond(&sem.mu)
	return sem
}

func (cs *CountingSemaphore) Acquire() {
	cs.mu.Lock()
	defer cs.mu.Unlock()

	for cs.count <= 0 {
		cs.cond.Wait()
	}

	cs.count--
}

func (cs *CountingSemaphore) Release() {
	cs.mu.Lock()
	defer cs.mu.Unlock()

	cs.count++
	cs.cond.Signal()
}

func main() {
	countingSemaphore := NewCountingSemaphore(2)
	wg := sync.WaitGroup{}

	for i := 0; i < 1024; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()

			countingSemaphore.Acquire()
			defer countingSemaphore.Release()
			fmt.Printf("Worker %d, in critical region\n", id)
		}(i)
	}

	wg.Wait()
}
