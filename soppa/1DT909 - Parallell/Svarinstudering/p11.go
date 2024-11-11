package main

import (
	"fmt"
	"sync"
)

func parPreSum(values []int) []int {
	var newValues = [5]int{}
	var wg sync.WaitGroup
	for i := 0; i < len(values); i++ {
		wg.Add(1)
		go func(i int) {
			temp := values[0]
			for j := 1; j < i+1; j++ {
				temp += values[j]
			}
			newValues[i] = temp
			wg.Done()
		}(i)
	}
	wg.Wait()
	return newValues[:]
}

func main() {
	var values = []int{1, 4, 2, 5, 8}
	calcValues := parPreSum(values)
	fmt.Println(calcValues)

}
