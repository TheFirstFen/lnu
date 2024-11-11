package main

import (
	"fmt"
	"math/rand"
)

func main() {
	valueCount := make([]int, 11)
	for i := 0; i < 20; i++ {
		firstDice := rand.Intn(6) + 1
		secondDice := rand.Intn(6) + 1
		sum := firstDice + secondDice
		valueCount[sum-2] += 1

	}
	for j := 0; j < 11; j++ {
		fmt.Println(j+2, " - ", valueCount[j])
	}
}
