package algorithms.sort;

public class Insertionsort {
    public static void insertionSort(int[] arr) {
        int i, j;
        int n = arr.length;
        int temp;

        if (n < 2)
            return;

        for (i = 1; i < n; i++) {
            temp = arr[i];
            j = i - 1;

            while (j >= 0 && arr[j] > temp) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = temp;
        }
    }

}
