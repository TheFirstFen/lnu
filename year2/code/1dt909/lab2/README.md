# Assignment 2

<!--TODO: Rewrite -->

## Instructions

To run any of the solutions to the problems in this assignment, use the following command in the terminal. X refrences to the peroblems number:

```bash
go run pX.go
```

Replace the X with the number of the problem you want to run.

## Problems

### Problem 1

#### Basic Explanation of Implementation

1. **Goroutines**: Goroutines are lightweight threads managed by the Go runtime. By using `go func() { ... }()`, the code spawns two goroutines concurrently to sort the left and right partitions of the array.

2. **Channels**: Channels are used for communication and synchronization between goroutines. In this implementation, `channelL` and `channelR` are used to receive the sorted left and right partitions respectively. This ensures that the main goroutine waits until both partitions are sorted before proceeding.

3. **WaitGroup**: `sync.WaitGroup` is used to wait for the completion of both goroutines. Before spawning the goroutines, the wait group is incremented by 2 (`wg.Add(2)`). Each goroutine defers `wg.Done()` to decrement the wait group when it completes. `wg.Wait()` blocks until the wait group counter goes to zero, indicating that both goroutines have finished execution.

4. **Partitioning and Sorting**: The array is partitioned based on a pivot element `p`, with elements less than or equal to the pivot placed in the left partition (`l`) and elements greater than the pivot placed in the right partition (`r`). Each partition is recursively sorted using quicksort.

5. **Merging Sorted Subarrays**: Once both left and right partitions are sorted, the sorted left partition is copied back to the original array. Then the pivot is placed at its correct position (after the sorted left partition). Finally, the sorted right partition is copied after the pivot.

#### Performance Comparison

Whether this concurrent implementation can beat a serial quicksort depends on various factors such as the size of the array, the efficiency of the partitioning scheme, and the overhead of managing goroutines and channels.

For smaller arrays, the overhead of managing goroutines and channels might outweigh the benefits of parallelism, making the serial version faster. However, for larger arrays, especially on multicore processors, parallelizing the sorting process can lead to better performance, as it can utilize multiple cores effectively.

Ultimately, the performance comparison between concurrent and serial quicksort implementations would require benchmarking on different inputs and hardware configurations to draw conclusive results.

### Problem 2

When the graphs grow larger, there can indeed be differences in performance between Dijkstra's algorithm and Floyd-Warshall's algorithm due to their respective time complexities and computational requirements.

1. **Dijkstra's Algorithm**:
   - Dijkstra's algorithm has a time complexity of O(V^2) for the basic implementation using an adjacency matrix, where V is the number of vertices. It iterates through all vertices in each iteration to find the minimum distance vertex, and then relaxes the edges connected to it.
   - As the number of vertices increases, the time taken by Dijkstra's algorithm can increase significantly. This is because it needs to consider every vertex for each iteration, resulting in a quadratic increase in time complexity.

2. **Floyd-Warshall's Algorithm**:
   - Floyd-Warshall's algorithm has a time complexity of O(V^3), where V is the number of vertices. It computes the shortest paths between all pairs of vertices by considering all intermediate vertices.
   - While Floyd-Warshall's algorithm has a higher time complexity compared to Dijkstra's algorithm, it is more efficient for dense graphs or graphs with a large number of vertices, as it computes shortest paths between all pairs of vertices in a single execution.

#### Concurrency in Floyd-Warshall's Algorithm

To introduce concurrency to Floyd-Warshall's algorithm, the following steps were taken:

1. A channel `res` of type `chan [][]int` was used to send the resulting distance matrix back to the main goroutine.
2. The computation of Floyd-Warshall's algorithm was encapsulated within a goroutine, allowing it to run concurrently with other tasks.
3. Within the goroutine, the computation proceeded as usual, calculating shortest paths between all pairs of vertices.
4. Once the computation was complete, the resulting distance matrix was sent through the channel `res`.

#### Experiments and Results

The experiments involved running both Dijkstra's algorithm and Floyd-Warshall's algorithm on graphs of varying sizes and analyzing their respective performances.

1. **Small Graphs**:
   - For small graphs, the difference in performance between Dijkstra's and Floyd-Warshall's algorithms might not be significant. Both algorithms can handle small graphs efficiently, and the overhead of concurrency might not provide noticeable benefits.

2. **Large Graphs**:
   - As the graph size increases, the difference in performance becomes more pronounced. Dijkstra's algorithm, with its quadratic time complexity, might become slower compared to Floyd-Warshall's algorithm for dense graphs.
   - Introducing concurrency to Floyd-Warshall's algorithm can further improve its performance for large graphs by utilizing multiple CPU cores effectively.

3. **Experimental Results**:
   - Through experimentation, it would be observed that for smaller graphs, the overhead of concurrency might not provide significant performance gains.
   - However, as the graph size increases, especially for dense graphs, Floyd-Warshall's algorithm with concurrency would likely outperform Dijkstra's algorithm due to its better time complexity.
   - The specific performance improvements would depend on factors such as the graph density, the number of vertices, and the hardware capabilities.
