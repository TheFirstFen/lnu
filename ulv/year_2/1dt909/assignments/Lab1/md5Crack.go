package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"sync"
	"time"
)

const chars = "abcdefghijklmnopqrstuvwxyz0123456789"
const targetHash = "a74277500228f7b4cfa8694098443fc5"
const passwordLength = 6
const numWorkers = 1
//const targetHash = "755afdd46a18a25bd85ddd4004d5cfea"
//const passwordLength = 5

func generatePasswords(passwords chan<- string, length int, wg *sync.WaitGroup, start int, end int) {
	defer wg.Done()
	for i := start; i < end; i++ {
		password := string(chars[i])
		generators(passwords, length-1, password)
	}
}

func generators(passwords chan<- string, length int, password string) {
	if length == 0 {
		passwords <- password
		
		return
	}
	for i := 0; i < len(chars); i++ {
		generators(passwords, length-1, password+string(chars[i]))
	}
}

func worker(passwords <-chan string, found chan<- string, targetHash string, wg *sync.WaitGroup) {
	for password := range passwords {
		//fmt.Println(password)
		hash := md5.Sum([]byte(password))
		if hex.EncodeToString(hash[:]) == targetHash {
			found <- password
			return
		}
	}
}

func main() {
	start := time.Now()
	
	passwords := make(chan string)
	found := make(chan string)
	var wg sync.WaitGroup

	for i := 0; i < len(chars); i++ {
		wg.Add(1)
		go generatePasswords(passwords, passwordLength, &wg, i, i + 1)
	}
	
	for i := 0; i < numWorkers; i++ {
		go worker(passwords, found, targetHash, &wg)
	}

	go func() {
		wg.Wait()
		close(passwords)
		close(found)
	}()

	password := <- found

	duration := time.Since(start)
	
	fmt.Println("Password found: " + password)
	fmt.Println("Time taken: " + duration.String())
}
