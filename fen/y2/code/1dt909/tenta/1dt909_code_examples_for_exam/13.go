package main

import (
	"fmt"
	"sync"
)

func parallelOddEvenSort(arr []int) {
	n := len(arr)
	sorted := false

	for !sorted {
		sorted = true
		var wg sync.WaitGroup
		var mutex sync.Mutex

		// Even phase (compare elements at positions 0-1, 2-3, 4-5, etc.)
		for i := 0; i < n-1; i += 2 {
			wg.Add(1)
			go func(i int) {
				defer wg.Done()
				if arr[i] > arr[i+1] {
					arr[i], arr[i+1] = arr[i+1], arr[i]
					mutex.Lock()
					sorted = false
					mutex.Unlock()
				}
			}(i)
		}
		wg.Wait()

		// Odd phase (compare elements at positions 1-2, 3-4, 5-6, etc.)
		for i := 1; i < n-1; i += 2 {
			wg.Add(1)
			go func(i int) {
				defer wg.Done()
				if arr[i] > arr[i+1] {
					arr[i], arr[i+1] = arr[i+1], arr[i]
					mutex.Lock()
					sorted = false
					mutex.Unlock()
				}
			}(i)
		}
		wg.Wait()
	}
}

func main() {
	arr := []int{8, 3, 1, 9, 4, 6, 2, 7, 5}
	fmt.Println("Original array:", arr)

	parallelOddEvenSort(arr)
	fmt.Println("Sorted array:", arr)
}
