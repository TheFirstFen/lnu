package algorithms.sort;

import java.util.Arrays;

public class Quicksort {
    private static int depth = 0;

    public static void quickSort(int[] arr, int maxDepth, double[] timeI, double[] timeH) {
        quickSort(arr, 0, arr.length - 1, depth, maxDepth, timeI, timeH);
    }

    private static void quickSort(int[] arr, int left, int right, int depth, int maxDepth, double[] timeI,
            double[] timeH) {
        if (left < right) {
            if (depth >= maxDepth) {
                // TODO: SHould take left right pointers and only sort the unsorted partiotions
                continueSorting(arr, timeI, timeH, maxDepth / 5);
                return;
            }
            int pivotIdx = partition(arr, left, right);
            quickSort(arr, left, pivotIdx - 1, depth + 1, maxDepth, timeI, timeH);
            quickSort(arr, pivotIdx + 1, right, depth + 1, maxDepth, timeI, timeH);
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

    private static void continueSorting(int[] arr, double[] timeI, double[] timeH, int idx) {
        Timer sw = new Timer();

        int[] arrI = Arrays.copyOf(arr, arr.length);

        sw.start();
        Insertionsort.insertionsort(arrI, 0, arrI.length - 1);
        sw.stop();
        timeI[idx] = sw.getTimeInNanoSeconds();
        sw.reset();

        sw.start();
        Heapsort.heapsort(arr);
        sw.stop();
        timeH[idx] = sw.getTimeInNanoSeconds();
        sw.reset();
    }
}