package Algorithm;

public class QuickSort {

    private static int depth = 0;

    public static int[] quickSort(int[] arr, int max_depth) {
        quickSort(arr, 0, arr.length - 1, depth, max_depth);
        return arr;
    }
    

    private static int[] quickSort(int[] arr, int low, int high, int depth, int max_depth) {
        if (depth < max_depth) {
            if (low < high) {
                int pivotIndex = Partition(arr, low, high);
                if (pivotIndex > 1) {
                    quickSort(arr, low, high - 1, depth + 1, max_depth);
                }
                if (pivotIndex + 1 < high) {
                    quickSort(arr, low + 1, high, depth + 1, max_depth);
                }
            }
        }
        return arr;
    }

    private static int Partition(int[] arr, int low, int high) {
        int mid = (low + high) / 2;
        int pivotid = medianOfThree(arr, low, mid, high);
        int pivot = arr[pivotid];

        while(true) {
            while (arr[low] < pivot) {
                low++;
            }
            while (arr[high] > pivot) {
                high--;
            }
            if (low < high) {
                if (arr[low] == arr[high]) {
                    return high;
                }
                swap(arr, low, high);
            }
            else {
                return high;
            }
        }
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    private static int medianOfThree(int[] arr, int low, int mid, int high) {
        if ((arr[low] >= arr[mid] && arr[low] <= arr[high]) || (arr[low] <= arr[mid] && arr[low] >= arr[high])) {
            return low;
        }
        else if ((arr[high] >= arr[low] && arr[high] <= arr[mid]) || (arr[high] <= arr[low] && arr[high] >= arr[mid])) {
            return high;
        }
        else {
            return mid;
        }
    }
}
