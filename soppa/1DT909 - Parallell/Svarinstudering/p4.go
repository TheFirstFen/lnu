package main

import (
	"fmt"
	"sync"
)

func main() {
	counter := 1
	workers := 1000
	var wg sync.WaitGroup
	for i := 0; i < workers; i++ {
		wg.Add(1)
		go func() {
			counter++
			wg.Done()
		}()
	}
	wg.Wait()
	fmt.Println(counter)
}
