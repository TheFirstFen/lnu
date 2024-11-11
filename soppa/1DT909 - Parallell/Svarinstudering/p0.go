package main

import "sync"

var mu sync.Mutex
var count int

func main() {
	go func() {
		mu.Lock()
		count++
	}()

}
