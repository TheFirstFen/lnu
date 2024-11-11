package main

import (
	"fmt"
	"math/rand"
	"sync"
	"time"
)

func NarySearch(values []int, target int, numWorkers int, intv int) int {
	length := len(values)
	result := make(chan int)

	var wg sync.WaitGroup

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		start := i * intv
		end := start + intv
		if end > length {
			end = length
		}

		go func(start, end int) {
			defer wg.Done()
			for j := start; j < end; j += 1 {
				if values[j] == target {
					result <- j
					return
				}
				if values[j] > target {
					result <- -1
					return
				}
			}
			result <- -1
		}(start, end)
	}

	go func() {
		wg.Wait()
		close(result)
	}()

	for index := range result {
		if index != -1 {
			return index
		}
	}

	return -1
}

func main() {
	timeArray := []float64{}
	AmountOfValues := 10_000_000
	numWorkers := 32
	intv := AmountOfValues / numWorkers
	if AmountOfValues%numWorkers != 0 {
		intv++
	}

	values := []int{}
	for i := 1; i <= AmountOfValues; i++ {
		values = append(values, i)
	}

	randomTargetsAmount := 1000

	for i := 0; i < randomTargetsAmount; i++ {
		target := rand.Intn(AmountOfValues)

		startTime := time.Now()
		NarySearch(values, target, numWorkers, intv)
		endTime := time.Now()
		timeArray = append(timeArray, endTime.Sub(startTime).Seconds())
	}

	var sum float64
	for _, num := range timeArray {
		sum += num
	}

	fmt.Println("Random searches with N-ary\nSize:", AmountOfValues)
	fmt.Println("Amount of workers:", numWorkers, "\nAvg time:", (sum/float64(randomTargetsAmount))*1000, " ms")

}
