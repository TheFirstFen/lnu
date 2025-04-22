package main

import (
	"fmt"
	"sync"
	"time"
)

// Barrier implementation using mutex and condition variable
type Barrier struct {
	mutex      sync.Mutex
	cond       *sync.Cond
	count      int
	threshold  int
	generation int
}

func NewBarrier(threshold int) *Barrier {
	b := &Barrier{
		threshold:  threshold,
		count:      0,
		generation: 0,
	}
	b.cond = sync.NewCond(&b.mutex)
	return b
}

func (b *Barrier) Wait() {
	b.mutex.Lock()
	defer b.mutex.Unlock()

	gen := b.generation

	// Increment count of waiting goroutines
	b.count++

	if b.count == b.threshold {
		// Last goroutine to reach the barrier
		b.count = 0        // Reset count for next use
		b.generation++     // Increment generation
		b.cond.Broadcast() // Wake up all waiting goroutines
		return
	}

	// Wait until threshold is reached and generation changes
	for gen == b.generation {
		b.cond.Wait()
	}
}

func main() {
	numWorkers := 5
	barrier := NewBarrier(numWorkers)

	var wg sync.WaitGroup

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()

			// Phase 1
			fmt.Printf("Worker %d completed phase 1\n", id)
			barrier.Wait()

			// Phase 2 - starts only after all workers have completed phase 1
			fmt.Printf("Worker %d completed phase 2\n", id)
			barrier.Wait()

			// Phase 3 - starts only after all workers have completed phase 2
			fmt.Printf("Worker %d completed phase 3\n", id)
		}(i)

		// Stagger worker start times
		time.Sleep(100 * time.Millisecond)
	}

	wg.Wait()
	fmt.Println("All workers completed all phases")
}
