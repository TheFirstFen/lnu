public class Quicksort {
    public static void quickSort(double[] doubleArray){
        quickSort(doubleArray, 0, doubleArray.length - 1);
    }

    private static void quickSort(double[] doubleArray, int left, int right){
        if (left < right){
            int pivot = partition(doubleArray, left, right);

            if (pivot > 1)
                quickSort(doubleArray, left, pivot - 1);
            if (pivot + 1 < right)
                quickSort(doubleArray, pivot + 1, right);

        }
    }

    private static int partition(double[] doubleArray, int left, int right){
        double pivot = doubleArray[left];
        while (true){
            while (doubleArray[left] < pivot)
                left++;

            while (doubleArray[right] > pivot)
                right--;

            if (left < right){
                if (doubleArray[left] == doubleArray[right])
                    return right;

                double temp = doubleArray[left];
                doubleArray[left] = doubleArray[right];
                doubleArray[right] = temp;
            }
            else
                return right;
        }
    }
}