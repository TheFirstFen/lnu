package algorithms.sort;

public class Quicksort {
    private static int depth = 0;

    public static void quickSort(int[] arr, int maxDepth, int algorithm) {
        quickSort(arr, 0, arr.length - 1, depth, maxDepth, algorithm);
    }

    private static void quickSort(int[] arr, int left, int right, int depth, int maxDepth, int algorithm) {
        if (left < right) {
            if (depth >= maxDepth) {
                if (algorithm == 0) {
                    // * HeapSort FIX heapsort with left and right pointer
                    Heapsort.heapsort(arr, left, right);
                } else if (algorithm == 1) {
                    Insertionsort.insertionsort(arr, left, right);
                }
                return;
            }
            int pivotIdx = partition(arr, left, right);
            quickSort(arr, left, pivotIdx - 1, depth + 1, maxDepth, algorithm);
            quickSort(arr, pivotIdx + 1, right, depth + 1, maxDepth, algorithm);
        }
    }

    private static int partition(int[] arr, int left, int right) {
        int m = left + (right - left) / 2;
        int pIdx = medianOfThree(arr, left, m, right);
        int pivot = arr[pIdx];

        swap(arr, pIdx, right);

        int i = left - 1;

        for (int j = left; j < right; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, right);
        return i + 1;
    }

    public static int medianOfThree(int[] arr, int left, int mid, int right) {
        if ((arr[left] <= arr[mid] && arr[mid] <= arr[right]) || (arr[right] <= arr[mid] && arr[mid] <= arr[left])) {
            return mid;
        } else if ((arr[mid] <= arr[left] && arr[left] <= arr[right])
                || (arr[right] <= arr[left] && arr[left] <= arr[mid])) {
            return left;
        } else
            return right;

    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}