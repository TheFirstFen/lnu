package main

import (
	"fmt"
	"time"
)

func main() {
	counter := 0

	go func() {
		for i := 0; i < 100_000; i++ {
			counter++
		}
	}()

	go func() {
		for i := 0; i < 100_000; i++ {
			counter++
		}
	}()

	time.Sleep(time.Second)
	if counter == 200_000 {
		fmt.Println("Assertion passed: ", counter)
	} else {
		fmt.Println("Assertion failed: ", counter)
	}
}
