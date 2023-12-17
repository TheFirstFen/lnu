package algorithms.sort;

public class Quicksort {
    private static int counter = 0;

    public static void quickSort(int[] arr, int depth) {
        quickSort(arr, 0, arr.length - 1, depth);
    }

    private static void quickSort(int[] arr, int l, int r, int depth) {
        if (++counter < depth) {
            int p = partition(arr, l, r);
            quickSort(arr, l, p - 1, depth);
            quickSort(arr, p + 1, r, depth);
        }
    }

    private static int partition(int[] arr, int l, int r) {
        int m = (l + r) / 2;
        int pIdx = medianOfThree(arr, l, m, r);
        int pVal = arr[pIdx];

        swap(arr, m, r);

        int i = l - 1;
        for (int j = l; j < r; j++) {
            if (arr[j] <= pVal) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, r);
        return i + 1;
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    private static int medianOfThree(int[] arr, int l, int m, int r) {
        if ((arr[l] >= arr[m] && arr[l] <= arr[r]) || (arr[l] <= arr[m] && arr[l] >= arr[r]))
            return l;
        else if ((arr[m] >= arr[l] && arr[m] <= arr[r]) || (arr[m] <= arr[l] && arr[m] >= arr[r]))
            return m;
        else
            return r;
    }
}