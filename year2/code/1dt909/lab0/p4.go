package main

import "fmt"

func quicksort(arr []int) []int {
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

	return append(append(quicksort(l), m...), quicksort(r)...)
}

func medianOfThree(arr []int) int {
	l := arr[1]
	r := arr[len(arr) - 1]
	m := arr[len(arr) / 2]

	return (l + r + m) / 3
}

func main() {
	arr := []int{3, 3, 6, 6, 8, 10, 1, 2, 1}
	fmt.Println("Original array:", arr)
	fmt.Println("Sorted array:", quicksort(arr))
}
