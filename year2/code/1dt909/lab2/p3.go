package main

import (
	"fmt"
	"sync"
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

func main() {
	data := []int{1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
	target := 13
	numGoroutines := len(data) / 3
	numValuesToCheck := 2

	index := NarySearch(data, target, numGoroutines, numValuesToCheck)
	if index != -1 {
		fmt.Printf("Found %d at index %d\n", target, index)
	} else {
		fmt.Printf("%d not found in the list\n", target)
	}
}
