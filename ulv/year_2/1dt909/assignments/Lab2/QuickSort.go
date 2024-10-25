package main

import (
	"fmt"
	"math/rand"
	"sync"
)

const randNumbers = 100

func quickSort(arr []int, wg *sync.WaitGroup, c chan<- []int) {
	defer wg.Done()
	if len(arr) <= 1 {
		c <- arr
		return
	}

	pivot := arr[0]
	var left, right []int
	for _, val := range arr[1:] {
		if val <= pivot {
			left = append(left, val)
		} else {
			right = append(right, val)
		}
	}

	leftchan := make(chan []int)
	rightchan := make(chan []int)

	wg.Add(2)
	go quickSort(left, wg, leftchan)
	go quickSort(right, wg, rightchan)

	sortedLeft := <-leftchan
	sortedRight := <-rightchan

	close(leftchan)
	close(rightchan)

	sorted := append(sortedLeft, pivot)
	sorted = append(sorted, sortedRight...)

	c <- sorted
}

func generateRandomArray(size int) []int {
	arr := make([]int, size)
	for i := 0; i < size; i++ {
		arr[i] = rand.Intn(randNumbers)
	}
	return arr
}

func main() {
	arr := generateRandomArray(randNumbers)
	fmt.Println("Original array:", arr)

	wg := sync.WaitGroup{}
	c := make(chan []int)

	wg.Add(1)
	go quickSort(arr, &wg, c)

	sortedArr := <-c
	close(c)
	wg.Wait()
	
	fmt.Println("\nSorted array:", sortedArr)
}
