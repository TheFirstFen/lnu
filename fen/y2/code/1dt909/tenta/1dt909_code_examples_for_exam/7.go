package main

import (
	"fmt"
	"time"
)

func main() {
	items := make(chan int, 10)

	producer := func() {
		for i := 0; i < 10; i++ {

			// Critical section
			items <- i
			fmt.Println("Produced", i)

			time.Sleep(1 * time.Millisecond)
		}
		close(items)
	}

	consumer := func() {
		for item := range items {

			// Critical section
			fmt.Println("Consumed", item)

			time.Sleep(1 * time.Millisecond)
		}
	}

	go producer()
	go consumer()

	time.Sleep(time.Second)
}
