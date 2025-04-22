package main

import (
	"fmt"
)

func main() {
	ch := make(chan string, 1)
	ch <- "2"

	fmt.Println(<-ch)
}
