package main

import (
	"fmt"
	"math"
	"math/rand"
	"sync"
	"time"
)

const (
	GRAPH_SIZE = 5
	TESTING    = false // true == exectuion time print only, false == full print
)

type Graph struct {
	vertices int
	edges    [][]int
}

func NewGraph(vertices int) *Graph {
	edges := make([][]int, vertices)
	for i := range edges {
		edges[i] = make([]int, vertices)
		for j := range edges[i] {
			if i == j {
				edges[i][j] = 0
			} else {
				edges[i][j] = math.MaxInt32
			}
		}
	}
	return &Graph{vertices: vertices, edges: edges}
}

func (g *Graph) addEdge(src, dest, weight int) {
	g.edges[src][dest] = weight
}

func (g *Graph) djikstra(src int) []int {
	vert := g.vertices
	dist := make([]int, vert)
	visited := make([]bool, vert)
	for i := range dist {
		dist[i] = math.MaxInt32
	}
	dist[src] = 0

	for count := 0; count < vert-1; count++ {
		u := minDistance(dist, visited)
		visited[u] = true
		for v := 0; v < vert; v++ {
			if !visited[v] && g.edges[u][v] != math.MaxInt32 && dist[u]+g.edges[u][v] < dist[v] {
				dist[v] = dist[u] + g.edges[u][v]
			}
		}
	}

	return dist
}

func minDistance(dist []int, visited []bool) int {
	min := math.MaxInt32
	minIndex := -1
	for v, d := range dist {
		if !visited[v] && d <= min {
			min = d
			minIndex = v
		}
	}
	return minIndex
}

func (g *Graph) runDjikstras() [][]int {
	wg := sync.WaitGroup{}
	wg.Add(g.vertices)
	ch := make(chan []int, g.vertices)
	dist := make([][]int, g.vertices)
	for i := range dist {
		dist[i] = make([]int, g.vertices)
	}

	for i := 0; i < g.vertices; i++ {
		go func(src int) {
			defer wg.Done()
			ch <- g.djikstra(src)
		}(i)
	}

	go func() {
		wg.Wait()
		close(ch)
	}()

	for i := 0; i < g.vertices; i++ {
		dist[i] = <-ch
	}

	return dist
}

func (g *Graph) floydWarshall(res chan<- [][]int) {
	vert := g.vertices
	dist := make([][]int, vert)
	for i := range dist {
		dist[i] = make([]int, vert)
		copy(dist[i], g.edges[i])
	}

	for i := 0; i < vert; i++ {
		for j := 0; j < vert; j++ {
			for k := 0; k < vert; k++ {
				if dist[j][i]+dist[i][k] < dist[j][k] {
					dist[j][k] = dist[j][i] + dist[i][k]
				}
			}
		}
	}

	res <- dist
}

func timer() func() {
	start := time.Now()
	return func() {
		fmt.Printf("\nExecution time: %v", time.Since(start))
	}
}

func main() {
	graph := NewGraph(GRAPH_SIZE)
	for i := 0; i < GRAPH_SIZE; i++ {
		graph.addEdge(i, rand.Intn(GRAPH_SIZE), i*rand.Intn(5))
	}

	djikTimer := timer()
	dijkstraRes := graph.runDjikstras()
	djikTimer()

	fmt.Println("\nDijkstra's algorithm:")
	for src, row := range dijkstraRes {
		for dest, weight := range row {
			if weight == math.MaxInt32 {
				//fmt.Printf("Source %d - Destination %d: %v\n", src, dest, "Inf")
				continue
			} else if weight == 0 {
				continue
			} else if !TESTING {
				fmt.Printf("Source %d - Destination %d: %v\n", src, dest, weight)
			}
		}
	}

	floydWarshallChan := make(chan [][]int)

	floydTimer := timer()
	go graph.floydWarshall(floydWarshallChan)
	floydWarshallRes := <-floydWarshallChan
	floydTimer()

	fmt.Println("\nFloyd Warshall's algorithm:")
	for src, row := range floydWarshallRes {
		for dest, weight := range row {
			if weight == math.MaxInt32 {
				//fmt.Printf("Source %d - Destination %d: %v\n", src, dest, "Inf")
				continue
			} else if weight == 0 {
				continue
			} else if !TESTING {
				fmt.Printf("Source %d - Destination %d: %v\n", src, dest, weight)
			}
		}
	}
}
