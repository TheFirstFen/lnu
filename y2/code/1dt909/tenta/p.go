package main

import "sync"

func main() {
	l1 := sync.Mutex{}
	l2 := sync.Mutex{}
	wg := sync.WaitGroup{}

	for i := 0; i < 10_000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			l1.Lock()
			l2.Lock()

			l1.Unlock()
			l2.Unlock()
		}()

		wg.Add(1)
		go func() {
			defer wg.Done()
			l2.Lock()
			l1.Lock()

			l1.Unlock()
			l2.Unlock()
		}()
	}
	wg.Wait()
}
