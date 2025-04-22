package main

import (
	"fmt"
	"time"
)

func main() {
	go func() {
		fmt.Println("1")
	}()
	time.Sleep(time.Second)
}
