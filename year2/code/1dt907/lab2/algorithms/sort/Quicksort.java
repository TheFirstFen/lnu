package algorithms.sort;

public class Quicksort {
    private static int depth = 0;

    public static void quickSort(int[] arr, int maxDepth) {
        quickSort(arr, 0, arr.length - 1, depth, maxDepth);
    }

    private static void quickSort(int[] arr, int l, int r, int depth, int maxDepth) {
        if (depth < maxDepth) {
            if (l < r) {
                int p = partition(arr, l, r);
                if (p > 1)
                    quickSort(arr, l, p - 1, depth + 1, maxDepth);
                if (p + 1 < r)
                    quickSort(arr, p + 1, r, depth + 1, maxDepth);
            }
        }
    }

    private static int partition(int[] arr, int l, int r) {
        int m = (l + r) / 2;
        int pIdx = medianOfThree(arr, l, m, r);
        int pVal = arr[pIdx];

        while (true) {
            while (arr[l] < pVal)
                l++;

            while (arr[r] > pVal)
                r--;

            if (l < r) {
                if (arr[l] == arr[r])
                    return r;

                swap(arr, l, r);
            } else
                return r;
        }
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