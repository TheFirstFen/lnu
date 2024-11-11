package main

import (
	"fmt"
	"sync"
)

type node struct {
	val       int
	mu        sync.Mutex
	rightNode *node
}

func EnQueue(firstNode *node, value int) *node {
	n := &node{val: value}
	if firstNode == nil {
		return n
	}
	firstNode.mu.Lock()
	defer firstNode.mu.Unlock()
	curr := firstNode
	for curr.rightNode != nil {
		curr = curr.rightNode
	}
	curr.rightNode = n
	return firstNode
}

func (n *node) DeQueue() (*node, int) {
	n.mu.Lock()
	defer n.mu.Unlock()
	if n == nil || n.rightNode == nil {
		return nil, 0
	}
	firstNode := n.rightNode
	n.rightNode = firstNode.rightNode
	return firstNode, n.val
}

func (n *node) GetList(array []int) []int {
	curr := n
	for curr != nil {
		array = append(array, curr.val)
		curr = curr.rightNode
	}
	return array
}

func main() {
	var firstNode *node
	var array []int
	var wg sync.WaitGroup

	numWorkers := 10

	numOfOperations := 10

	wg.Add(numWorkers)

	for i := 0; i < numWorkers; i++ {
		go func() {
			defer wg.Done()
			for j := 0; j < numOfOperations; j++ {
				firstNode = EnQueue(firstNode, j)
				firstNode, _ = firstNode.DeQueue()
			}
		}()
	}

	wg.Wait()

	fmt.Println(firstNode.GetList(array))
	fmt.Println(len(firstNode.GetList(array)))
}
