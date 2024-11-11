package main

import "fmt"

func QuickSort(arr []int) {
	if len(arr) < 2 {
		return
	}
	pivotIndex := getMedianOfThree(arr)
	pivotValue := arr[pivotIndex]

	arr[pivotIndex], arr[len(arr)-1] = arr[len(arr)-1], arr[pivotIndex]

	lo := 0
	hi := len(arr) - 2

	for lo <= hi {
		for arr[lo] < pivotValue {
			lo++
		}
		for arr[hi] > pivotValue {
			hi--
		}
		if lo <= hi {
			arr[lo], arr[hi] = arr[hi], arr[lo]
			lo++
			hi--
		}
	}
	pivotPos := lo
	arr[pivotPos], arr[len(arr)-1] = arr[len(arr)-1], arr[pivotPos]
	QuickSort(arr[:pivotPos])
	QuickSort(arr[pivotPos:])
}

func getMedianOfThree(arr []int) int {
	first := arr[0]
	second := arr[len(arr)-1]
	third := arr[len(arr)/2]

	if first < second && second < third {
		return len(arr) / 2
	} else if second < first && first < third {
		return 0
	} else {
		return len(arr) - 1
	}
}
func main() {
	arr := []int{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 4, 5, 4, 12, 34, 12, 76}
	fmt.Println("Original slice:", arr)

	QuickSort(arr)
	fmt.Println("Sorted slice:", arr)
}
