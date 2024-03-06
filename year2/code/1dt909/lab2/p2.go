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
			edges[i][j] = math.MaxInt32
		}
	}
	return &Graph{vertices: vertices, edges: edges}
}

func (g *Graph) addEdge(src, dest, weight int) {
	g.edges[src][dest] = weight
}

func dijkstra(graph *Graph, src int) []int {
	n := graph.vertices
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
			if !visited[v] && graph.edges[u][v] != math.MaxInt32 && dist[u]+graph.edges[u][v] < dist[v] {
				dist[v] = dist[u] + graph.edges[u][v]
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

func floydWarshall(graph [][]int, wg *sync.WaitGroup, resultChan chan<- [][]int) {
	defer wg.Done()

	n := len(graph)
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, n)
		copy(dist[i], graph[i])
	}

	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if dist[i][k]+dist[k][j] < dist[i][j] {
					dist[i][j] = dist[i][k] + dist[k][j]
				}
			}
		}
	}
	resultChan <- dist
}

func runDjikstras(graph *Graph, res [][]int) {
	wg := sync.WaitGroup{}
	wg.Add(graph.vertices)
	ch := make(chan []int, graph.vertices)

	for i := 0; i < graph.vertices; i++ {
		go func(src int) {
			defer wg.Done()
			ch <- dijkstra(graph, src)
		}(i)
	}

	go func() {
		wg.Wait()
		close(ch)
	}()

	for i := 0; i < graph.vertices; i++ {
		res[i] = <-ch
	}

	fmt.Println("Dijkstra's algorithm:")
	print(res)
}

func runFloydWarshall(graph *Graph, res [][]int) {
	ch := make(chan [][]int, graph.vertices)
	wg := sync.WaitGroup{}
	wg.Add(graph.vertices)

	for i := 0; i < graph.vertices; i++ {
		go floydWarshall(graph.edges, &wg, ch)
	}

	go func() {
		wg.Wait()
		close(ch)
	}()

	for dist := range ch {
		res = dist
	}

	fmt.Println("Floyd-Warshall's algorithm:")
	print(res)
}

func print(matrix [][]int) {
	for i, dist := range matrix {
		fmt.Printf("From vertex %d:\n", i)
		for j, weight := range dist {
			if weight == math.MaxInt32 {
				fmt.Printf("Vertex %d -> Vertex %d: Infinity\n", i, j)
			} else {
				fmt.Printf("Vertex %d -> Vertex %d: %d\n", i, j, weight)
			}
		}
		fmt.Println()
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

	dijkstraRes := make([][]int, graph.vertices)
	floydWarshallRes := make([][]int, graph.vertices)

	runDjikstras(graph, dijkstraRes)
	runFloydWarshall(graph, floydWarshallRes)
}
