package main

import (
	"fmt"
	"math"
	"sync"
	"time"
	"math/rand"
)

const amount_of_nodes = 5

type Graph struct {
	node  []int
	edges [][]int
}

func NewGraph() *Graph {
	return &Graph{}
}

func (g *Graph) AddNode(node int) {
	g.node = append(g.node, node)
	for i := range g.edges {
		g.edges[i] = append(g.edges[i], 0)
	}
	g.edges = append(g.edges, make([]int, len(g.node)))
}

func (g *Graph) AddEdge(from, to int, weight int) {
	id1 := g.nodeId(from)
	id2 := g.nodeId(to)
	if id1 != -1 && id2 != -1 {
		g.edges[id1][id2] = weight

	}
}

func (g *Graph) nodeId(node int) int {
	for i, n := range g.node {
		if n == node {
			return i
		}
	}
	return -1
}

func Dijkstra(graph *Graph, start int) []int {
	numNodes := len(graph.node)
	distances := make([]int, numNodes)
	visited := make([]bool, numNodes)

	for i := range distances {
		distances[i] = math.MaxInt
	}

	startid := graph.nodeId(start)
	if startid == -1 {
		return distances
	}

	distances[startid] = 0

	for i := 0; i < numNodes; i++ {
		minid := -1
		minDist := math.MaxInt

		for j, dist := range distances {
			if !visited[j] && dist < minDist {
				minDist = dist
				minid = j
			}
		}

		if minid == -1 {
			break
		}

		visited[minid] = true

		for j, weight := range graph.edges[minid] {
			if !visited[j] && weight > 0 {
				newDist := distances[minid] + weight
				if newDist < distances[j] {
					distances[j] = newDist
				}
			}
		}
	}
	return distances
}

func (g *Graph) FloydWarshall() [][]int {
	dist := make([][]int, len(g.node))
	
	for i := range dist {
		dist[i] = make([]int, len(g.node))
		for j := range dist[i] {
			dist[i][j] = math.MaxInt32
			if i == j {
				dist[i][j] = 0
			}
		}
	}

	for i := range g.edges {
		for j := range g.edges[i] {
			if g.edges[i][j] != 0 {
				dist[i][j] = g.edges[i][j]
			}
			if i == j {
				dist[i][j] = 0
			}
		}
	}

	result := make(chan [][]int)
	numGo := len(g.node)

	for k := range dist {
		go func(k int){
			for i := range dist {
				for j := range dist {
					if dist[i][k]+dist[k][j] < dist[i][j] {
						dist[i][j] = dist[i][k] + dist[k][j]
					}
				}
			}
			result <- dist
		}(k)
	}

	for i := 0; i < numGo; i++ {
		select{
		case res := <-result:
			dist = res
		}
	}

	return dist
}

func printMatrix(graph *Graph, shortestDistances [][]int) {
	fmt.Print("    ")
	for _, node := range graph.node {
		fmt.Printf("%3d ", node)
	}
	fmt.Println()

	for i, row := range shortestDistances {
		fmt.Printf("%3d ", graph.node[i])

		for _, dist := range row {
			if dist == math.MaxInt32 {
				fmt.Printf("  ∞ ")
			} else {
				fmt.Printf("%3d ", dist)
			}
		}
		fmt.Println()
	}
}

func main() {
	wg := sync.WaitGroup{}
	graph := NewGraph()

	for i := 1; i <= amount_of_nodes; i++ {
		graph.AddNode(i)
	}

	//graph.AddEdge(1, 2, 1)
	//graph.AddEdge(1, 3, 4)
	//graph.AddEdge(2, 3, 2)
	//graph.AddEdge(1, 4, 1)
	//graph.AddEdge(2, 5, 5)
	//graph.AddEdge(2, 4, 3)
	//graph.AddEdge(3, 4, 2)
	//graph.AddEdge(4, 5, 6)
	//graph.AddEdge(4, 2, 1)



	for i := 0; i < amount_of_nodes*2; i++ {
		randStart := rand.Intn(amount_of_nodes) + 1
		randEnd := rand.Intn(amount_of_nodes) + 1
		randVal := rand.Intn(amount_of_nodes) + 1

		graph.AddEdge(randStart, randEnd, randVal)
	}

	resultCh := make(chan struct {
		node      int
		distances []int
	})

	startTime := time.Now()
	for i := 1; i <= 5; i++ {
		wg.Add(1)
		go func(node int) {
			defer wg.Done()
			distances := Dijkstra(graph, node)
			resultCh <- struct {
				node      int
				distances []int
			}{node, distances}
		}(i)
	}

	go func() {
		wg.Wait()
		close(resultCh)

	}()

	for res := range resultCh {
		fmt.Println("Shortest distances from node", res.node, ": ")
		for i, dist := range res.distances {
			fmt.Printf("%v: %d\n", graph.node[i], dist)
		}
		fmt.Println()
	}
	
	fmt.Println("Total time taken for Dijkstra:", time.Since(startTime))

	startTimes := time.Now()
	distances := graph.FloydWarshall()

	printMatrix(graph, distances)

	fmt.Println("Total time taken for Floyd Warshall: ", time.Since(startTimes))
	
}