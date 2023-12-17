package algorithms.sort;

public class Insertionsort {
    public static void insertionsort(int[] arr) {
        insertionsort(arr, 0, arr.length - 1);
    }

    public static void insertionsort(int[] arr, int l, int r) {
        for (int i = l + 1; i <= r; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= l && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;
        }
    }

}
