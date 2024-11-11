package main

import (
	"fmt"
	"math/rand"
)

func main() {
	posx := 0
	posy := 0

	var size int
	var maxSteps int
	var stepCount int

	fmt.Print("Input grid size: ")
	fmt.Scan(&size)
	fmt.Print("Input max steps: ")
	fmt.Scan(&maxSteps)
	for i := 0; i < maxSteps; i++ {
		temp := rand.Intn(4)
		switch temp {
		case 0:
			posx += 1
		case 1:
			posx -= 1
		case 2:
			posy += 1
		case 3:
			posy -= 1
		}
		if abs(posx) > size || abs(posy) > size {
			fmt.Println("Out of bounds after ", stepCount, " steps")
			break
		}
		fmt.Println("Current pos: x-", posx, "y-", posy)
		stepCount += 1
	}
	fmt.Println("Out of steps")

}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
