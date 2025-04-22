package main

import (
	"fmt"
	"time"
)

func main() {
	var flag [2]bool
	var turn int

	counter := 0

	go func() {
		for i := 0; i < 5; i++ {
			flag[0] = true
			turn = 1

			for flag[1] && turn == 1 {
			}

			counter++

			flag[0] = false
		}
		time.Sleep(time.Millisecond)
	}()

	go func() {
		for i := 0; i < 5; i++ {
			flag[1] = true
			turn = 0

			for flag[0] && turn == 0 {
			}

			counter++

			flag[1] = false
		}
		time.Sleep(time.Millisecond)
	}()

	time.Sleep(time.Millisecond)
	fmt.Printf("Counter: %d\n", counter)
}
