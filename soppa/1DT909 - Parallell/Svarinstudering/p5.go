package main

import (
	"fmt"
	"time"
)

var flag = []bool{false, false}
var turn int

func petersonsAlgorithm(id int) {
	otherId := 1 - id
	flag[id] = true
	turn = otherId
	for flag[otherId] && turn == otherId {

	}
	fmt.Println("Thread", id, "in critical section")
	time.Sleep(1 * time.Second)
	flag[id] = false
}

func main() {
	go petersonsAlgorithm(0)
	go petersonsAlgorithm(1)
	time.Sleep(3 * time.Second)

}
