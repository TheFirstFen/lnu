package main

import (
	"fmt"
	"sync"
	"time"
)

// Barrier implementation using channels
type ChannelBarrier struct {
	count      int
	threshold  int
	generation int
	arrival    chan int
	departure  chan int
}

func NewChannelBarrier(threshold int) *ChannelBarrier {
	return &ChannelBarrier{
		threshold:  threshold,
		count:      0,
		generation: 0,
		arrival:    make(chan int),
		departure:  make(chan int),
	}
}

func (b *ChannelBarrier) Start() {
	go func() {
		for {
			// Wait for all goroutines to arrive
			for i := 0; i < b.threshold; i++ {
				<-b.arrival
			}

			// Signal all goroutines to depart
			b.generation++
			for i := 0; i < b.threshold; i++ {
				b.departure <- b.generation
			}
		}
	}()
}

func (b *ChannelBarrier) Wait() {
	b.arrival <- 1 // Signal arrival
	<-b.departure  // Wait for departure signal
	return
}

func main() {
	numWorkers := 5
	barrier := NewChannelBarrier(numWorkers)
	barrier.Start()

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
