package main

import (
	"fmt"
	"time"
)

func worker(done <-chan struct{}, values <-chan int, results chan<- int) {
	for {
		select {
		case <-done:
			// Done-kanal stängd, avsluta goroutine
			fmt.Println("Worker: Avslutning begärd, avslutar...")
			return

		case value, ok := <-values:
			if !ok {
				// Values-kanalen stängd, men fortsätt lyssna på done-kanalen
				fmt.Println("Worker: Inga fler värden, väntar på avslutningssignal...")
				// Blocka tills done-kanalen signalerar
				<-done
				return
			}

			// Bearbeta värdet
			result := value * 2
			results <- result
		}
	}
}

func main() {
	done := make(chan struct{})
	values := make(chan int)
	results := make(chan int)

	// Starta worker
	go worker(done, values, results)

	// Skicka några värden
	go func() {
		for i := 0; i < 5; i++ {
			values <- i
		}
		close(values)
	}()

	// Samla in resultat
	go func() {
		for result := range results {
			fmt.Println("Resultat:", result)
		}
	}()

	// Låt det köra en stund
	time.Sleep(2 * time.Second)

	// Signalera avslutning genom att stänga done-kanalen
	fmt.Println("Main: Signalerar avslutning...")
	close(done)

	// Vänta lite så att vi ser avslutningsmeddelandet
	time.Sleep(time.Second)
}
