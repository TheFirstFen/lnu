package main

import (
	"fmt"
	"sync"
	"time"
)

const (
	SIZE = 10_000_000
)

// TODO: check and fix

func binarySearch(data []int, target int) int {
	low := 0
	high := len(data) - 1
	for low <= high {
		mid := (low + high) / 2
		if data[mid] == target {
			return mid
		} else if data[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}

func NarySearch(data []int, target int, numWorkers int, numValuesToCheck int) int {
	interval := len(data) / numWorkers
	res := make([]int, numWorkers)
	var wg sync.WaitGroup

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go func(start, end, idx int) {
			defer wg.Done()
			for j := start; j < end; j += numValuesToCheck {
				for k := j; k < j+numValuesToCheck && k < len(data); k++ {
					if data[k] == target {
						res[idx] = k
						return
					}
				}
			}
			res[idx] = -1
		}(i*interval, (i+1)*interval, i)
	}

	wg.Wait()

	for _, idx := range res {
		if idx != -1 {
			return idx
		}
	}

	return -1
}

func timer() func() {
	start := time.Now()
	return func() {
		fmt.Printf("Execution time: %v\n", time.Since(start))
	}
}

func main() {
	data := make([]int, SIZE)

	for i := 0; i < SIZE; i++ {
		data[i] = i
	}

	target := SIZE / 50000
	numWorkers := len(data) / 3
	numValuesToCheck := 2

	timer := timer()
	idx := NarySearch(data, target, numWorkers, numValuesToCheck)
	timer()
	if idx != -1 {
		fmt.Printf("Found %d at idx %d\n", target, idx)
	} else {
		fmt.Printf("%d not found in the list\n", target)
	}

	// timer = timer()
	idx = binarySearch(data, target)
	// timer()
	if idx != -1 {
		fmt.Printf("Found %d at idx %d\n", target, idx)
	} else {
		fmt.Printf("%d not found in the list\n", target)
	}
}
