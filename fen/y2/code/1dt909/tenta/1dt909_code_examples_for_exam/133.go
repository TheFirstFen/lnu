package main

func fanOut(input <-chan int, n int) []<-chan int {
	outputs := make([]chan int, n)

	// Skapa output-kanaler
	for i := 0; i < n; i++ {
		outputs[i] = make(chan int)
	}

	// Starta goroutine för att distribuera värden
	go func() {
		defer func() {
			// Stäng alla output-kanaler när vi är klara
			for _, ch := range outputs {
				close(ch)
			}
		}()

		// Round-robin distribution
		i := 0
		for val := range input {
			outputs[i] <- val
			i = (i + 1) % n
		}
	}()

	// Konvertera till read-only kanaler
	results := make([]<-chan int, n)
	for i := range outputs {
		results[i] = outputs[i]
	}

	return results
}

// Alternativ implementation där alla värden skickas till alla kanaler
func broadcast(input <-chan int, n int) []<-chan int {
	outputs := make([]chan int, n)

	// Skapa output-kanaler
	for i := 0; i < n; i++ {
		outputs[i] = make(chan int)
	}

	// Starta en goroutine per output-kanal
	for i := range outputs {
		go func(ch chan int, index int) {
			defer close(ch)

			// Kopiera alla värden från input till denna output
			for val := range input {
				ch <- val
			}
		}(outputs[i], i)
	}

	// Konvertera till read-only kanaler
	results := make([]<-chan int, n)
	for i := range outputs {
		results[i] = outputs[i]
	}

	return results
}
