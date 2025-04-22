package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var mux sync.Mutex
	buf := make([]int, 0, 10)

	producer := func() {
		for i := 0; i < 10; i++ {
			mux.Lock()
			buf = append(buf, i)
			fmt.Println("Produced", i)
			mux.Unlock()
			time.Sleep(1 * time.Millisecond)
		}
	}

	consumer := func() {
		for {
			mux.Lock()
			if len(buf) > 0 {
				fmt.Println("Consumed", buf[0])
				buf = buf[1:]
			}
			mux.Unlock()
			time.Sleep(1 * time.Millisecond)
		}
	}

	go producer()
	go consumer()

	time.Sleep(time.Second)
}
