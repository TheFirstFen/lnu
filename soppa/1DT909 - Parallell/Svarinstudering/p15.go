package main

import (
	"fmt"
	"sync"
)

type barrier struct {
	total int
	count int
	mu    sync.Mutex
	cond  *sync.Cond
}

func newBarrier(n int) *barrier {
	barrier := &barrier{total: n}
	barrier.cond = sync.NewCond(&barrier.mu)
	return barrier
}

func (b *barrier) Wait() {
	b.mu.Lock()
	b.count++
	if b.count == b.total {
		b.count = 0
		b.cond.Broadcast()
	} else {
		b.cond.Wait()
	}
	b.mu.Unlock()
}

func main() {
	var wg sync.WaitGroup
	barrier := newBarrier(3)
	for i := 0; i < 3; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			fmt.Println("At barrier", i)
			barrier.Wait()
			fmt.Println("Past barrier", i)
		}(i)
	}
	wg.Wait()
}
