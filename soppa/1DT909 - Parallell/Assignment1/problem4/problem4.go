package main

import (
	"fmt"
	"sync"
)

type CountingSemaphore struct {
	mu       sync.Mutex
	cond     *sync.Cond
	count    int
	maxCount int
}

func NewCountingSemaphore(maxCount int) *CountingSemaphore {
	semaphore := &CountingSemaphore{count: 0, maxCount: maxCount}
	semaphore.cond = sync.NewCond(&semaphore.mu)
	return semaphore
}

func (semaphore *CountingSemaphore) Acquire() {
	semaphore.mu.Lock()
	defer semaphore.mu.Unlock()

	for semaphore.count >= semaphore.maxCount {
		semaphore.cond.Wait()
	}
	semaphore.count--
}

func (semaphore *CountingSemaphore) Release() {
	semaphore.mu.Lock()
	defer semaphore.mu.Unlock()

	semaphore.count++
	semaphore.cond.Signal()
}

func main() {

	var wg sync.WaitGroup

	numWorkers := 64
	N := 3

	semaphore := NewCountingSemaphore(N)
	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			semaphore.Acquire()
			defer semaphore.Release()

			fmt.Println("Goroutine", id, "in critical section")
		}(i)
	}

	wg.Wait()
}
