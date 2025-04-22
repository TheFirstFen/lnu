package main

import (
	"fmt"
	"math"
	"sync"
)

func findParallelMin(arr []int) int {
	if len(arr) == 0 {
		return 0 // or math.MaxInt, depending on requirements
	}

	numGoroutines := 4 // Can be adjusted based on the list size and available cores
	if numGoroutines > len(arr) {
		numGoroutines = len(arr)
	}

	// Calculate chunk size
	chunkSize := len(arr) / numGoroutines

	// Channel to collect local minimums from each goroutine
	results := make(chan int, numGoroutines)

	var wg sync.WaitGroup

	// Distribute work among goroutines
	for i := 0; i < numGoroutines; i++ {
		wg.Add(1)
		go func(start int) {
			defer wg.Done()

			// Calculate the range for this goroutine
			end := start + chunkSize
			if end > len(arr) {
				end = len(arr)
			}

			// Find local minimum
			localMin := math.MaxInt
			for j := start; j < end; j++ {
				if arr[j] < localMin {
					localMin = arr[j]
				}
			}

			// Send local minimum
			results <- localMin
		}(i * chunkSize)
	}

	// Close the results channel when all goroutines are done
	go func() {
		wg.Wait()
		close(results)
	}()

	// Find the global minimum from local minimums
	globalMin := math.MaxInt
	for min := range results {
		if min < globalMin {
			globalMin = min
		}
	}

	return globalMin
}

func main() {
	arr := []int{42, 17, 8, 94, 23, 61, 12, 5, 38}
	fmt.Println("Array:", arr)

	min := findParallelMin(arr)
	fmt.Println("Minimum value:", min)
}
