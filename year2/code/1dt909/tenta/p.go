package main

import (
	"fmt"
	"sync"
)

func oddEvenTranspositionSort(arr []int, wg *sync.WaitGroup, evenPhase bool) {
	defer wg.Done()
	length := len(arr)
	for i := 0; i < length/2; i++ {
		start := 1
		if evenPhase {
			start = 0
		}
		for j := start; j < length-1; j += 2 {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}
	wg.Wait()
}
func main() {
	arr := []int{9, 3, 6, 2, 8, 5, 1, 4, 7}
	fmt.Println("Unsorted array:", arr)
	wg1 := sync.WaitGroup{}
	wg2 := sync.WaitGroup{}

	wg2.Add(1)
	for phase := 0; phase < len(arr); phase++ {
		wg1.Add(1)
		go oddEvenTranspositionSort(arr, &wg1, phase%2 == 0)
	}
	wg2.Done()
	wg2.Wait()

	fmt.Println("Sorted array:", arr)
}
