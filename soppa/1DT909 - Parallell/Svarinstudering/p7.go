package main

import (
	"fmt"
	"time"
)

func producer(ch chan int) {
	for i := 0; i < 5; i++ {
		ch <- i
		time.Sleep(1 * time.Second)
	}
	close(ch)
}
func main() {
	ch := make(chan int)
	go producer(ch)

	for n := range ch {
		fmt.Println(n)
	}
}
