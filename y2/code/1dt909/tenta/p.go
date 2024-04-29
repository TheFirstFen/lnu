package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup
var mutex sync.Mutex
var sharedVar int

func increment() {
	mutex.Lock()
	sharedVar++
	mutex.Unlock()
	wg.Done()
}
func main() {
	for i := 0; i < 2; i++ {
		wg.Add(1)
		go increment()
	}
	wg.Wait()
	fmt.Println("Value of sharedVar:", sharedVar)

}
