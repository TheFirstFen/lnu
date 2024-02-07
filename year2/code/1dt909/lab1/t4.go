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

func NewSemaphore(initCount int) *CountingSemaphore {
	sem := &CountingSemaphore{
		count: initCount,
	}

	sem.cond = sync.NewCond(&sem.mu)
	return sem
}

func (s *CountingSemaphore) Acquire() {
	s.mu.Lock()
	defer s.mu.Unlock()

	for s.count <= 0 {
		s.cond.Wait()
	}
	s.count--
}

func (s *CountingSemaphore) Release() {
	s.mu.Lock()
	defer s.mu.Unlock()

	s.count++
	s.cond.Signal()
}

func main() {
	semaphore := NewSemaphore(4)
	wg := sync.WaitGroup{}

	for i := 0; i < 20; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			semaphore.Acquire()
			defer semaphore.Release()
			fmt.Printf("Worker %d is in the critical region\n", id)
		}(i)
	}

	wg.Wait()
}
