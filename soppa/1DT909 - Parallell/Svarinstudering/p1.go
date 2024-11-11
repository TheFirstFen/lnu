package main

import (
	"fmt"
	"time"
)

func main() {
	go func() {
		fmt.Println("Hello")
	}()
	time.Sleep(1 * time.Second)
}
