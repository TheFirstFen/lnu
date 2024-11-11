package main

import "fmt"

func main() {
	ch := make(chan int)
	go func() {
		ch <- 23
	}()
	msg := <-ch
	fmt.Println(msg)
}
