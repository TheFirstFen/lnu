package main

import (
	"fmt"
	"math/rand"
)

func main() {
	counts := make([]int, 11)

	for i := 0; i < 10_000; i++ {
		die1 := rand.Intn(6) + 1
		die2 := rand.Intn(6) + 1
		sum := die1 + die2

		counts[sum - 2]++
	}

	fmt.Println("Sum Frequency")
	for idx, count := range counts {
		fmt.Printf("Sum %d: %d\n", idx+2, count)
	}
}
