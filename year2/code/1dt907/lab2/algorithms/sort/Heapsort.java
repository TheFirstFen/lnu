package algorithms.sort;

public class Heapsort {
    public static void heapsort(int[] arr, int left, int right) {
        int n = right - left + 1;

        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i, left);

        for (int i = n - 1; i > 0; i--) {
            swap(arr, left, left + i);
            heapify(arr, i, 0, left);
        }
    }

    private static void heapify(int[] arr, int n, int i, int left) {
        int largest = i;
        int l = 2 * i + 1 + left;
        int r = 2 * i + 2 + left;

        if (l < left && arr[l] > arr[largest])
            largest = l;

        if (r < left && arr[r] > arr[largest])
            largest = r;

        if (largest != i) {
            swap(arr, left + i, left + largest);
            heapify(arr, n, largest, left);
        }
    }

    private static void swap(int[] arr, int l, int r) {
        int temp = arr[l];
        arr[l] = arr[r];
        arr[r] = temp;
    }
}
