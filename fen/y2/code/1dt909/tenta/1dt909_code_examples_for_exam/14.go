package main

import (
	"fmt"
	"sync"
)

func main() {
	data := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	results := make([]int, len(data))

	var wg sync.WaitGroup

	// Parallelize the for-loop using goroutines
	for i, val := range data {
		wg.Add(1)
		go func(i, val int) {
			defer wg.Done()

			// Perform some computation
			result := val * val

			// Store the result
			results[i] = result
		}(i, val) // Pass loop variables to avoid closure issues
	}

	// Wait for all goroutines to complete
	wg.Wait()

	fmt.Println("Original data:", data)
	fmt.Println("Processed results:", results)
}
