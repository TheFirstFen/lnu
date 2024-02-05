package main

import (
	"fmt"
	"sync"
)

type CountingSemaphore struct {
	mutex    sync.Mutex
	counter  int
	maxCount int
}

func NewCountingSemaphore(maxCount int) *CountingSemaphore {
	return &CountingSemaphore{
		maxCount: maxCount,
	}
}

func (s *CountingSemaphore) Acquire() {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	for s.counter >= s.maxCount {
	}
	s.counter++
}

func (s *CountingSemaphore) Release() {
	s.mutex.Lock()
	defer s.mutex.Unlock()

	if s.counter > 0 {
		s.counter--
	}
}

func main() {
	semaphore := NewCountingSemaphore(2)
	wg := sync.WaitGroup{}

	worker := func(id int) {
		defer wg.Done()
		semaphore.Acquire()
		defer semaphore.Release()
		fmt.Printf("Worker %d is in the critical region\n", id)
	}

	for i := 0; i < 5; i++ {
		wg.Add(1)
		go worker(i)
	}

	wg.Wait()
}
