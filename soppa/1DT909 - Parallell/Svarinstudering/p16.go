package main

import (
	"fmt"
	"sync"
)

func main() {
	n := 5 // Antal gorutiner
	barrier := make(chan bool)
	wg := sync.WaitGroup{}
	wg.Add(n)

	// Funktion som väntar på tillstånd att fortsätta från barriären
	waitAtBarrier := func(id int) {
		fmt.Printf("Goroutine %d når barriären.\n", id)
		barrier <- true // Skickar signal till barriären
		<-barrier       // Väntar på signal från barriären
		fmt.Printf("Goroutine %d passerar barriären.\n", id)
		wg.Done()
	}

	// Starta gorutiner
	for i := 0; i < n; i++ {
		go waitAtBarrier(i)
	}

	// Barriärlogik
	for i := 0; i < n; i++ {
		<-barrier // Vänta tills alla gorutiner når barriären
	}

	for i := 0; i < n; i++ {
		barrier <- true // Låt alla gorutiner fortsätta
	}

	wg.Wait() // Vänta på att alla gorutiner är klara
}
