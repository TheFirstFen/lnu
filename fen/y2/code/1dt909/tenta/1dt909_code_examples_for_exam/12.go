package main

import (
	"fmt"
	"sync"
)

func parallelPrefixScan(input []int) []int {
	n := len(input)
	output := make([]int, n)

	if n <= 1 {
		copy(output, input)
		return output
	}

	// Up-sweep phase (reduction)
	temp := make([]int, n)
	copy(temp, input)

	for d := 1; d < n; d *= 2 {
		var wg sync.WaitGroup
		stride := 2 * d

		for i := 0; i < n; i += stride {
			if i+d < n {
				wg.Add(1)
				go func(i int) {
					defer wg.Done()
					temp[i+stride-1] = temp[i+d-1] + temp[i+stride-1]
				}(i)
			}
		}

		wg.Wait()
	}

	// Set the last element to identity (0 for sum)
	temp[n-1] = 0

	// Down-sweep phase
	for d := n / 2; d > 0; d /= 2 {
		var wg sync.WaitGroup
		stride := 2 * d

		for i := 0; i < n; i += stride {
			if i+d < n {
				wg.Add(1)
				go func(i int) {
					defer wg.Done()
					t := temp[i+d-1]
					temp[i+d-1] = temp[i+stride-1]
					temp[i+stride-1] += t
				}(i)
			}
		}

		wg.Wait()
	}

	// Calculate final output (exclusive scan)
	var wg sync.WaitGroup
	for i := 0; i < n; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			if i == 0 {
				output[i] = 0
			} else {
				output[i] = temp[i-1] + input[i-1]
			}
		}(i)
	}
	wg.Wait()

	return output
}

func main() {
	input := []int{3, 1, 7, 0, 4, 1, 6, 3}
	fmt.Println("Input:", input)

	result := parallelPrefixScan(input)
	fmt.Println("Parallel prefix scan:", result)

	// Verify with sequential calculation (exclusive scan)
	sequential := make([]int, len(input))
	sequential[0] = 0
	for i := 1; i < len(input); i++ {
		sequential[i] = sequential[i-1] + input[i-1]
	}
	fmt.Println("Sequential prefix scan:", sequential)
}
