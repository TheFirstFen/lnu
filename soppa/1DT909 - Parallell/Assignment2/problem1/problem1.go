package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

type QS struct {
	wg sync.WaitGroup
}

func (s *QS) QuickSort(list []int) []int {
	if len(list) <= 1 {
		return list
	}

	result := make([]int, len(list))
	copy(result, list)

	s.wg.Add(1)
	s._sort(result, 0, len(result)-1)
	s.wg.Wait()

	return result
}

func (s *QS) _sort(list []int, lo, hi int) {
	defer s.wg.Done()

	if lo < hi {
		pivot := partition(list, lo, hi)

		s.wg.Add(2)
		go s._sort(list, lo, pivot-1)
		go s._sort(list, pivot+1, hi)
	}
}

func partition(list []int, lo, hi int) int {
	pivot := list[hi]
	i := lo - 1

	for j := lo; j < hi; j++ {
		if list[j] < pivot {
			i++
			list[i], list[j] = list[j], list[i]
		}
	}
	list[i+1], list[hi] = list[hi], list[i+1]
	return i + 1
}

func QuickSortSerial(arr []int, lo, hi int) {
	if lo >= hi {
		return
	}

	pivot := arr[hi]
	i := lo

	for j := lo; j < hi; j++ {
		if arr[j] < pivot {
			arr[j], arr[i] = arr[i], arr[j]
			i++
		}
	}
	arr[i], arr[hi] = arr[hi], arr[i]

	QuickSortSerial(arr, lo, i-1)
	QuickSortSerial(arr, i+1, hi)
}

func generateRandomList(size int) []int {
	list := make([]int, size)
	for i := 0; i < size; i++ {
		list[i] = rand.Intn(size)
	}
	return list
}

func main() {
	sizes := []int{1000, 10000, 100_000, 1_000_000, 10_000_000, 100_000_000}
	timesConc := [6]float64{}
	timesSerial := [6]float64{}
	for i := 0; i < 6; i++ {
		qs := &QS{}
		originalList := generateRandomList(sizes[i])

		listConc := make([]int, len(originalList))
		copy(listConc, originalList)

		listSerial := make([]int, len(originalList))
		copy(listSerial, originalList)
		startTime := time.Now()
		qs.QuickSort(listConc)
		endTime := time.Now()
		timesConc[i] = float64(endTime.Sub(startTime).Seconds())

		startTimeS := time.Now()
		QuickSortSerial(listSerial, 0, len(listSerial)-1)
		endTimeS := time.Now()
		timesSerial[i] = float64(endTimeS.Sub(startTimeS).Seconds())
	}

	fmt.Println("Time taken for concurrent quicksort")
	for i := 0; i < 6; i++ {
		fmt.Println("Concurrent - Size:", sizes[i], "Time:", timesConc[i], "seconds")
		fmt.Println("Serial - Size:", sizes[i], "Time:", timesSerial[i], "seconds")
	}
}
