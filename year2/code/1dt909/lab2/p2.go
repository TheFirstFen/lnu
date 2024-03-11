package main

import (
	"fmt"
	"math"
	"sync"
)

// TODO: Make sure works correctly weights for floyd seems wrong

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
	n := g.vertices
	dist := make([]int, n)
	visited := make([]bool, n)
	for i := range dist {
		dist[i] = math.MaxInt32
	}
	dist[src] = 0

	for count := 0; count < n-1; count++ {
		u := minDistance(dist, visited)
		visited[u] = true
		for v := 0; v < n; v++ {
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
	n := g.vertices
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, n)
		copy(dist[i], g.edges[i])
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k < n; k++ {
				if dist[j][i]+dist[i][k] < dist[j][k] {
					dist[j][k] = dist[j][i] + dist[i][k]
				}
			}
		}
	}

	res <- dist
}

func print(graph *Graph, res [][]int) {
	for i, _ := range res {
		for j, _ := range res {
			if res[i][j] == 0 {
				fmt.Printf("Source %d: %v\n", j, res[i])
				break
			}
		}
	}
}

func main() {
	graph := NewGraph(6)
	graph.addEdge(0, 1, 10)
	graph.addEdge(0, 2, 3)
	graph.addEdge(1, 3, 2)
	graph.addEdge(1, 2, 1)
	graph.addEdge(2, 1, 4)
	graph.addEdge(2, 3, 8)
	graph.addEdge(2, 4, 2)
	graph.addEdge(3, 4, 7)
	graph.addEdge(4, 3, 9)
	graph.addEdge(4, 0, 7)
	graph.addEdge(4, 5, 1)
	graph.addEdge(5, 0, 4)
	graph.addEdge(5, 2, 6)

	dijkstraRes := graph.runDjikstras()
	fmt.Println("Dijkstra's algorithm:")
	print(graph, dijkstraRes)

	channelRes := make(chan [][]int)
	go graph.floydWarshall(channelRes)

	floydWarshallRes := <-channelRes
	fmt.Println("\nFloyd Warshall's algorithm:")
	for src, row := range floydWarshallRes {
		fmt.Printf("Source %d: %v\n", src, row)
	}
}
