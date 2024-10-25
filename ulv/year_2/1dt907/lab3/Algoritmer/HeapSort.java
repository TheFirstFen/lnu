package Algoritmer;

public class HeapSort {
    public static void heapSort(Graph.Edge[] Array) {
        int n = Array.length;

        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(Array, n, i);
        }

        for (int i = n - 1; i > 0; i--) {
            Graph.Edge temp = Array[0];
            Array[0] = Array[i];
            Array[i] = temp;

            heapify(Array, i, 0);
        }
    }

    private static void heapify(Graph.Edge[] Array, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && Array[left] != null && Array[left].weight > Array[largest].weight) {
            largest = left;
        }
        if (right < n && Array[right] != null&& Array[right].weight > Array[largest].weight) {
            largest = right;
        }
        if (largest != i) {
            Graph.Edge temp = Array[i];
            Array[i] = Array[largest];
            Array[largest] = temp;

            heapify(Array, n, largest);
        }
    }
}