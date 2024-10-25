package main

import (
	"fmt"
	"math/rand"
)

type Point struct {
	X, Y int
}

func TakeStep() Point {
	directions := []Point{
		{0, 1},
		{0, -1},
		{1, 0},
		{-1, 0},
	}
	randomIndex := rand.Intn(len(directions))
	return directions[randomIndex]
}

func randWalk(k int, maxSteps int) Point {
	currentPosition := Point{0, 0}
	for step := 0; step < maxSteps; step++ {
		move := TakeStep()
		nextX := currentPosition.X + move.X
		nextY := currentPosition.Y + move.Y

		if nextX >= -k && nextX <= k && nextY >= -k && nextY <= k {
			currentPosition.X = nextX
			currentPosition.Y = nextY
		}else {
			break
		}
	} 
	return currentPosition
}

func main() {
	k := 5
	maxSteps := 100000

	finalposition := randWalk(k, maxSteps)
	fmt.Printf("Final position: (%d, %d)\n", finalposition.X, finalposition.Y)

}
