package main

import (
	"fmt"
	"math/rand"
)

func main() {
	numSimulations := 10000
	sumCounts := make([]int, 11)

	for i := 0; i < numSimulations; i++ {
		dice1 := rand.Intn(6) + 1
		dice2 := rand.Intn(6) + 1
		sum := dice1 + dice2

		sumCounts[sum-2]++
	}

	fmt.Println("Sum\tCount")
	for i := 0; i < len(sumCounts); i++ {
		fmt.Printf("%d\t%d\n", i+2, sumCounts[i])
	}
}