package Algorithm;

public class InsertionSort{

    public static void insertionSort(int[] arr) {
        insertionSort(arr, 0, arr.length - 1);
    }

    public static void insertionSort(int[] arr, int start, int end) {
        for (int i = start + 1; i <= end; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= start && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j+1] = key;
        }
    }
}