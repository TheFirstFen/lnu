package main

import (
	"fmt"
	"sync"
)

func quicksortConcurrent(arr []int, ch chan []int) {
	if len(arr) < 2 {
		ch <- arr
		defer close(ch)
		return
	}

	p := medianOfThree(arr)
	var l, m, r []int

	for _, num := range arr {
		switch {
		case num < p:
			l = append(l, num)
		case num == p:
			m = append(m, num)
		case num > p:
			r = append(r, num)
		}
	}
}

func quicksortSerial(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	p := medianOfThree(arr)
	var l, m, r []int

	for _, num := range arr {
		switch {
		case num < p:
			l = append(l, num)
		case num == p:
			m = append(m, num)
		case num > p:
			r = append(r, num)
		}
	}

	return append(append(quicksortSerial(l), m...), quicksortSerial(r)...)
}

func medianOfThree(arr []int) int {
	l := arr[0]
	r := arr[len(arr)-1]
	m := arr[len(arr)/2]

	if (l >= r && l <= m) || (l <= r && l >= m) {
		return l
	} else if (r >= l && r <= m) || (r <= l && r >= m) {
		return r
	} else {
		return m
	}
}

func isSorted(nums []int) bool {
	n := len(nums)
	for i := 1; i < n; i++ {
		if nums[i] < nums[i-1] {
			return false
		}
	}
	return true
}

func main() {
	arr := []int{5, 4, 3, 2, 1, 0}
	ch := make(chan []int)
	wg := sync.WaitGroup{}

	//for i := 0; i < 10_000; i++ {
	//	arr = append(arr, rand.Int())
	//}

	arrConcurrent := make([]int, len(arr))
	copy(arrConcurrent, arr)

	fmt.Printf("Original array: %v, length: %d\n", isSorted(arr), len(arr))
	arr = quicksortSerial(arr)
	fmt.Printf("Sorted array: %v, length: %d\n", isSorted(arr), len(arr))

	fmt.Printf("Original array: %v, length: %d\n", isSorted(arrConcurrent), len(arrConcurrent))
	wg.Add(1)
	go func() {
		defer wg.Done()
		quicksortConcurrent(arrConcurrent, ch)
	}()
	wg.Wait()
	var res []int
	for val := range ch {
		res = append(res, val...)
	}

	fmt.Printf("Sorted array: %v, length: %d\n", isSorted(res), len(res))
}
