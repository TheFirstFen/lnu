package main

func findMax(values <-chan int) int {
	// Ta emot första värdet för att initialisera max
	max, ok := <-values
	if !ok {
		// Kanalen var tom och stängd
		return 0 // eller annat standardvärde eller fel
	}

	// Fortsätt ta emot värden och uppdatera max
	for val := range values {
		if val > max {
			max = val
		}
	}

	return max
}

// Alternativ implementation med done-kanal för avbrytning
func findMaxWithDone(values <-chan int, done <-chan struct{}) (int, bool) {
	// Flagga för att hålla reda på om vi tagit emot minst ett värde
	receivedAny := false
	max := 0 // Standardvärde om inget tas emot

	for {
		select {
		case <-done:
			// Avbryt operationen
			return max, receivedAny

		case val, ok := <-values:
			if !ok {
				// Kanalen stängd, returnera resultatet
				return max, receivedAny
			}

			if !receivedAny || val > max {
				max = val
				receivedAny = true
			}
		}
	}
}
