package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

const (
	SIZE = 10_000_000
)

// TODO: chack and fix

func NarySearch(data []int, target int, numGoroutines int, numValuesToCheck int) int {
	interval := len(data) / numGoroutines
	results := make([]int, numGoroutines)
	var wg sync.WaitGroup

	for i := 0; i < numGoroutines; i++ {
		wg.Add(1)
		go func(start, end, index int) {
			defer wg.Done()
			for j := start; j < end; j += numValuesToCheck {
				for k := j; k < j+numValuesToCheck && k < len(data); k++ {
					if data[k] == target {
						results[index] = k
						return
					}
				}
			}
			results[index] = -1
		}(i*interval, (i+1)*interval, i)
	}

	wg.Wait()

	for _, index := range results {
		if index != -1 {
			return index
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
		data[i] = rand.Int()
	}

	target := rand.Int()
	numGoroutines := len(data) / 3
	numValuesToCheck := 2

	timer := timer()
	index := NarySearch(data, target, numGoroutines, numValuesToCheck)
	timer()
	if index != -1 {
		fmt.Printf("Found %d at index %d\n", target, index)
	} else {
		fmt.Printf("%d not found in the list\n", target)
	}
}
