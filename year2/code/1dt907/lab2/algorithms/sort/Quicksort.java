package algorithms.sort;

public class Quicksort {
    public static void quickSort(int[] arr) {
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int l, int r) {
        if (l < r) {
            int p = partition(arr, l, r);

            if (p > 1)
                quickSort(arr, l, p - 1);

            if (p + 1 < r)
                quickSort(arr, p + 1, r);

        }
    }

    private static int partition(int[] arr, int l, int r) {
        int p = arr[l];

        while (true) {
            while (arr[l] < p)
                l++;

            while (arr[r] > p)
                r--;

            if (l < r) {
                if (arr[l] == arr[r])
                    return r;

                int temp = arr[l];
                arr[l] = arr[r];
                arr[r] = temp;
            } else
                return r;
        }
    }
}
