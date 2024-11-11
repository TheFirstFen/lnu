package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"sync"
	"time"
)

const (
	targetHash = "755afdd46a18a25bd85ddd4004d5cfea"
	// targetHash  = "a74277500228f7b4cfa8694098443fc5 "
	charset     = "abcdefghijklmnopqrstuvwxyz0123456789"
	passwordLen = 5
)

func generatePasswords(ch chan<- string, numWorkers int, wg *sync.WaitGroup) {
	defer wg.Done()

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go func(id int) {
			defer wg.Done()
			for j := (id * len(charset) / numWorkers); j < ((id + 1) * len(charset) / numWorkers); j++ {
				generatePasswordHelper(charset, string(charset[j]), passwordLen-1, ch)
			}
		}(i)
	}
}

func generatePasswordHelper(charset string, prefix string, len int, ch chan<- string) {
	if len == 0 {
		ch <- prefix
		return
	}

	for _, char := range charset {
		generatePasswordHelper(charset, prefix+string(char), len-1, ch)
	}
}

func hashPassword(password string) string {
	hasher := md5.New()
	hasher.Write([]byte(password))
	return hex.EncodeToString(hasher.Sum(nil))
}

func hashPasswords(passwords <-chan string, found chan<- string, wg *sync.WaitGroup) {
	defer wg.Done()
	for password := range passwords {
		if hashPassword(password) == targetHash {
			found <- password
			return
		}
	}
}

func main() {
	workerNumbers := []int{4, 8, 16, 32, 64}
	for _, numWorkers := range workerNumbers {
		startTime := time.Now()

		passwords := make(chan string)
		found := make(chan string)
		var createWorkers sync.WaitGroup

		createWorkers.Add(1)
		go generatePasswords(passwords, numWorkers, &createWorkers)

		var hashWorkers sync.WaitGroup
		for i := 0; i < numWorkers; i++ {
			hashWorkers.Add(1)
			go hashPasswords(passwords, found, &hashWorkers)
		}

		go func() {
			hashWorkers.Wait()
			close(passwords)
		}()

		for password := range found {
			fmt.Print("Found - ", password)
			break
		}

		endTime := time.Now()
		fmt.Println("Number of workers:", numWorkers, " - Time:", endTime.Sub(startTime))
	}
}
