package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"sync"
	"time"
)

const (
	charset    = "abcdefghijklmnopqrstuvwxyz0123456789"
	numWorkers = len(charset) // * Adjustable to be lower then len(charset) due to numWorkers being part of divsion with len(charset)
	targetHash = "a74277500228f7b4cfa8694098443fc5"
	length     = 6
)

func generatePass(ch chan string, chasrset string, start int, end int, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := start; i < end; i++ {
		generatePassRec(ch, charset, string(charset[i]), length-1)
	}
}

func generatePassRec(ch chan string, charset string, prefix string, len int) {
	if len == 0 {
		ch <- prefix
		return
	}

	for _, char := range charset {
		generatePassRec(ch, charset, prefix+string(char), len-1)
	}
}

func hashAndCompare(ch chan string, res chan string, wg *sync.WaitGroup) {
	defer wg.Done()
	for pass := range ch {
		hash := md5.Sum([]byte(pass))
		hashStr := hex.EncodeToString(hash[:])

		// fmt.Printf("Password: %s (%s)\n", pass, hashStr) // ? DEBUG see all combinations tried in order

		if hashStr == targetHash {
			res <- pass
			return
		}
	}
}

func timer() func() {
	start := time.Now()
	return func() {
		fmt.Printf("Exection time: %v\n", time.Since(start))
	}
}

func main() {
	defer timer()()
	ch := make(chan string)
	res := make(chan string)
	wg := sync.WaitGroup{}

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go generatePass(ch, charset, (i * len(charset) / numWorkers), ((i + 1) * len(charset) / numWorkers), &wg)
	}

	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go hashAndCompare(ch, res, &wg)
	}

	go func() {
		wg.Wait()
		close(ch)
	}()

	pass := <-res
	fmt.Printf("Password found: %s\n", pass)
	close(res)
}
