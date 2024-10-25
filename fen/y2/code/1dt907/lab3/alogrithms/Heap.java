package alogrithms;

import alogrithms.graphs.Edge;

@SuppressWarnings("unchecked")
public class Heap<T> {
    private Edge<T>[] heap;
    private int size;
    private int cap;

    public Heap(int cap) {
        this.cap = cap;
        this.size = 0;
        this.heap = new Edge[cap];
    }

    public void push(Edge<T> edge) {
        resize();

        heap[size] = edge;
        heapifyUp(size);
        size++;
    }

    public Edge<T> pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Heap is empty.");
        }

        resize();

        Edge<T> edge = heap[0];
        heap[0] = heap[size - 1];
        size--;
        heapifyDown(0);

        return edge;
    }

    private void resize() {
        if (size == this.cap) {
            this.cap = this.cap * 2;
            Edge<T>[] newHeap = new Edge[this.cap];
            for (int i = 0; i < size; i++) {
                newHeap[i] = heap[i];
            }
            heap = newHeap;
        } else if (size == this.cap / 4) {
            this.cap = this.cap / 2;
            Edge<T>[] newHeap = new Edge[this.cap];
            for (int i = 0; i < size; i++) {
                newHeap[i] = heap[i];
            }
            heap = newHeap;
        } else
            return;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    private void heapifyUp(int idx) {
        while (idx > 0 && heap[parent(idx)].compareTo(heap[idx]) > 0) {
            swap(idx, parent(idx));
            idx = parent(idx);
        }
    }

    private void heapifyDown(int idx) {
        int lChild = lChild(idx);
        int rChild = rChild(idx);
        int min = idx;

        if (lChild < size && heap[lChild].compareTo(heap[min]) < 0) {
            min = lChild;
        }

        if (rChild < size && heap[rChild].compareTo(heap[min]) < 0) {
            min = rChild;
        }

        if (min != idx) {
            swap(idx, min);
            heapifyDown(min);
        }
    }

    private int parent(int idx) {
        return (idx - 1) / 2;
    }

    private int lChild(int idx) {
        return 2 * idx + 1;
    }

    private int rChild(int idx) {
        return 2 * idx + 2;
    }

    private void swap(int i, int j) {
        Edge<T> temp = heap[i];
        heap[i] = heap[j];
        heap[j] = temp;
    }

    public void sort() {
        for (int i = size - 1; i >= 0; i--) {
            heapifyDown(i);
        }
    }

    public int size() {
        return size;
    }
}