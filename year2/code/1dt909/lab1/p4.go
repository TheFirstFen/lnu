package main

import (
	"fmt"
	"sync"
)

type CountingSemaphore struct {
	count int
	mut   sync.Mutex
	cond  *sync.Cond
}

func NewCountingSemaphore(initCount int) *CountingSemaphore {
	sem := &CountingSemaphore{count: initCount}

	sem.cond = sync.NewCond(&sem.mut)
	return sem
}

func (cs *CountingSemaphore) Acquire() {
	cs.mut.Lock()
	defer cs.mut.Unlock()

	for cs.count <= 0 {
		cs.cond.Wait()
	}

	cs.count--
}

func (cs *CountingSemaphore) Release() {
	cs.mut.Lock()
	defer cs.mut.Unlock()

	cs.count++
	cs.cond.Signal()
}

func main() {
	countingSemaphore := NewCountingSemaphore(2)
	wg := sync.WaitGroup{}
	numWorkers := 1024

	for i := 0; i < numWorkers; i++ {
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
