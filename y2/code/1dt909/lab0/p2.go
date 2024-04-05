package main

import (
	"fmt"
	"math/rand"
)

type Point struct {
	X, Y int
}

func main() {
	var gridSize int
	var numSteps int

	fmt.Print("Enter grid size: ")
	_, err := fmt.Scanf("%d", &gridSize)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Print("Enter number of steps: ")
	_, err = fmt.Scanf("%d", &numSteps)
	if err != nil {
		fmt.Println(err)
		return
	}

	finalPos := randWalk(gridSize, numSteps)
	fmt.Printf("Final position after %d steps: %v\n", numSteps, finalPos)
}

func randWalk(gridSize int, numSteps int) Point {
	curPos:= Point{0, 0}

	dirs := []Point{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	for i := 0; i < numSteps; i++ {
		step := dirs[rand.Intn(len(dirs))]

		newPos := Point{curPos.X + step.X, curPos.Y + step.Y}

		// fmt.Printf("Step: %v, Position: %v\n", step, newPos) // * Uncomment to see each step

		if abs(newPos.X) <= gridSize/2 && abs(newPos.Y) <= gridSize/2 {
			curPos = newPos
		} else {
			break
		}
	}

	return curPos
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}