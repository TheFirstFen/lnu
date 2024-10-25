package main

import (
	"fmt"
)

func quickSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	pivot := arr[len(arr)/2]
	var left, m, right []int

	for _, v := range arr {
		if v < pivot {
			left = append(left, v)
		} else if v > pivot {
			right = append(right, v)
		}else {
			m = append(m, v)
		}
	}

	return append(append(quickSort(left), m...), quickSort(right)...)
}  

func main() {
	arr := []int{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}
	fmt.Println("Unsorted:", arr)

	arr = quickSort(arr)
	fmt.Println("Sorted:", arr)
}
