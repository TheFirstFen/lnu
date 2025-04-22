package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var mux sync.Mutex
	counter := 0

	go func() {
		for i := 0; i < 1000; i++ {
			mux.Lock()
			counter++
			mux.Unlock()
		}
	}()

	go func() {
		for i := 0; i < 1000; i++ {
			mux.Lock()
			counter++
			mux.Unlock()
		}
	}()

	time.Sleep(time.Millisecond)
	fmt.Println(counter)
}
