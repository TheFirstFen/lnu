package main

import (
	"container/heap"
	"fmt"
	"math"
	"math/rand"
	"sync"
	"time"
)

const INF = math.MaxInt32

type Graph struct {
	vertices  int
	adjMatrix [][]int
}

func NewGraph(vertices int) *Graph {
	edges := make([][]int, vertices)
	for i := range edges {
		edges[i] = make([]int, vertices)
		for j := range edges[i] {
			if i == j {
				edges[i][j] = 0
			} else {
				edges[i][j] = INF
			}
		}
	}
	return &Graph{vertices: vertices, adjMatrix: edges}
}

func (g *Graph) addEdge(src, dest, weight int) {
	g.adjMatrix[src][dest] = weight
}

func (g *Graph) FloydWarshall() [][]int {
	n := g.vertices
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, n)
		copy(dist[i], g.adjMatrix[i])
	}

	done := make(chan bool, n)

	for k := 0; k < n; k++ {
		go func(k int) {
			for i := 0; i < n; i++ {
				for j := 0; j < n; j++ {
					if dist[i][k]+dist[k][j] < dist[i][j] {
						dist[i][j] = dist[i][k] + dist[k][j]
					}
				}
			}
			done <- true
		}(k)
	}

	for i := 0; i < n; i++ {
		<-done
	}

	return dist
}

func (g *Graph) Dijkstra(source int, wg *sync.WaitGroup) []int {
	defer wg.Done()
	n := g.vertices
	dist := make([]int, n)
	for i := range dist {
		dist[i] = INF
	}
	dist[source] = 0

	pq := &PrioQueue{}
	heap.Init(pq)
	heap.Push(pq, &Node{value: source, weight: 0})

	visited := make([]bool, n)
	for pq.Len() > 0 {
		u := heap.Pop(pq).(*Node).value
		if visited[u] {
			continue
		}
		visited[u] = true

		for v := 0; v < n; v++ {
			if !visited[v] && g.adjMatrix[u][v] != math.MaxInt32 {
				w := g.adjMatrix[u][v]
				if dist[u]+w < dist[v] {
					dist[v] = dist[u] + w
					heap.Push(pq, &Node{value: v, weight: dist[v]})
				}
			}
		}
	}

	return dist
}

type Node struct {
	value  int
	weight int
}

type PrioQueue []*Node

func (pq PrioQueue) Len() int { return len(pq) }

func (pq PrioQueue) Less(i, j int) bool {
	return pq[i].weight < pq[j].weight
}

func (pq PrioQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PrioQueue) Push(x interface{}) {
	item := x.(*Node)
	*pq = append(*pq, item)
}

func (pq *PrioQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[0 : n-1]
	return item
}

func main() {
	edges := 100
	vertices := 1000

	graph := createGraph(edges, vertices)

	fmt.Println("Floyd-Warshall:")
	startTime := time.Now()
	graph.FloydWarshall()
	endTime := time.Now()
	fmt.Println(endTime.Sub(startTime))

	fmt.Println("\nDijkstra's:")
	startTimeD := time.Now()
	wg := sync.WaitGroup{}
	wg.Add(vertices)
	for i := 0; i < vertices; i++ {
		go graph.Dijkstra(i, &wg)
	}
	wg.Wait()
	endTimeD := time.Now()
	fmt.Println(endTimeD.Sub(startTimeD))
}

func createGraph(edges, vertices int) *Graph {
	g := NewGraph(vertices)

	for i := 0; i < edges; i++ {
		src := rand.Intn(vertices)
		dest := rand.Intn(vertices)
		for dest == src {
			dest = rand.Intn(vertices)
		}
		weight := rand.Intn(201) - 100
		g.addEdge(src, dest, weight)
	}

	return g
}
