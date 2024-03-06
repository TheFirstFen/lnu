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

func quicksortConcurrent(arr []int) {
	if len(arr) < 2 {
		return
	}

	channelL := make(chan []int, 1)
	channelR := make(chan []int, 1)

	p := arr[0]
	var l, r []int

	for _, val := range arr[1:] {
		if val <= p {
			l = append(l, val)
		} else {
			r = append(r, val)
		}
	}

	wg := sync.WaitGroup{}
	wg.Add(2)

	go func() {
		defer wg.Done()
		quicksortConcurrent(l)
		channelL <- l
	}()

	go func() {
		defer wg.Done()
		quicksortConcurrent(r)
		channelR <- r
	}()

	wg.Wait()

	sortedL := <-channelL
	sortedR := <-channelR

	copy(arr, sortedL)
	arr[len(sortedL)] = p
	copy(arr[len(sortedL)+1:], sortedR)
}

func quicksortSerial(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	p := medianOfThree(arr)
	var l, m, r []int

	for _, val := range arr {
		switch {
		case val < p:
			l = append(l, val)
		case val == p:
			m = append(m, val)
		case val > p:
			r = append(r, val)
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

func isSorted(arr []int) bool {
	n := len(arr)
	for i := 1; i < n; i++ {
		if arr[i] < arr[i-1] {
			return false
		}
	}
	return true
}

func timer() func() {
	start := time.Now()
	return func() {
		fmt.Printf("Execution time: %v\n", time.Since(start))
	}
}

func main() {
	arrSerial := make([]int, 0, SIZE)

	for i := 0; i < SIZE; i++ {
		arrSerial = append(arrSerial, rand.Int())
	}

	arrConcurrent := make([]int, len(arrSerial))
	copy(arrConcurrent, arrSerial)

	fmt.Println("Serial version:")
	fmt.Printf("Original array: %v, length: %d\n", isSorted(arrSerial), len(arrSerial))
	timerSerial := timer()
	arrSerial = quicksortSerial(arrSerial)
	timerSerial()
	fmt.Printf("Sorted array: %v, length: %d\n", isSorted(arrSerial), len(arrSerial))

	fmt.Println("\nConcurrent version:")
	fmt.Printf("Original array: %v, length: %d\n", isSorted(arrConcurrent), len(arrConcurrent))
	timerConcurrent := timer()
	quicksortConcurrent(arrConcurrent)
	timerConcurrent()
	fmt.Printf("Sorted array: %v, length: %d\n", isSorted(arrConcurrent), len(arrConcurrent))
}
