package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

func main() {
	var counter int64 = 0

	increment := func() {
		for {
			cur := atomic.LoadInt64(&counter)

			new := counter + 1

			if atomic.CompareAndSwapInt64(&counter, cur, new) {
				break
			}

		}
	}

	var wg sync.WaitGroup
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			increment()
		}()
	}

	wg.Wait()
	fmt.Println("Final counter value:", atomic.LoadInt64(&counter))

	// Another example: atomically swap a flag value
	var flag int32 = 0

	// Atomically set flag to 1 if it's currently 0
	if atomic.CompareAndSwapInt32(&flag, 0, 1) {
		fmt.Println("Flag was 0, now set to 1")
	} else {
		fmt.Println("Flag was not 0, swap didn't happen")
	}

	// Try again (should fail this time)
	if atomic.CompareAndSwapInt32(&flag, 0, 1) {
		fmt.Println("Flag was 0, now set to 1")
	} else {
		fmt.Println("Flag was not 0, swap didn't happen")
	}
}
