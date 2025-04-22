package main

import (
	"fmt"
	"sync"
)

func main() {
	var mux1 sync.Mutex
	var mux2 sync.Mutex

	go func() {
		mux1.Lock()
		fmt.Println("Lock 1 acquired by goroutine 1")
		mux2.Lock()
		fmt.Println("Lock 2 acquired by goroutine 1")
		mux2.Unlock()
		mux1.Unlock()
	}()

	go func() {
		mux2.Lock()
		fmt.Println("Lock 2 acquired by goroutine 2")
		mux1.Lock()
		fmt.Println("Lock 1 acquired by goroutine 2")
		mux1.Unlock()
		mux2.Unlock()
	}()

	select {}
}
