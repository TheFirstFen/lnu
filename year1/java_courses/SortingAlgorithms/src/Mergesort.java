public class Mergesort {
    public static void mergeSort(double[] doubleArray, int low, int high){
        if (low < high){
            int middle = (low / 2) + (high / 2);

            mergeSort(doubleArray, low, middle);
            mergeSort(doubleArray, middle + 1, high);
            merge(doubleArray, low, middle, high);
        }
    }

    public static void mergeSort(double[] doubleArray){
        mergeSort(doubleArray, 0, doubleArray.length - 1);
    }

    private static void merge(double[] doubleArray, int low, int middle, int high){
        int left = low;
        int right = middle + 1;
        double[] tmp = new double[(high - low) + 1];
        int tmpIndex = 0;

        while ((left <= middle) && (right <= high)){
            if (doubleArray[left] < doubleArray[right]){
                tmp[tmpIndex] = doubleArray[left];
                left = left + 1;
            }
            else{
                tmp[tmpIndex] = doubleArray[right];
                right = right + 1;
            }
            tmpIndex = tmpIndex + 1;
        }

        if (left <= middle){
            while (left <= middle){
                tmp[tmpIndex] = doubleArray[left];
                left = left + 1;
                tmpIndex = tmpIndex + 1;
            }
        }

        if (right <= high){
            while (right <= high){
                tmp[tmpIndex] = doubleArray[right];
                right = right + 1;
                tmpIndex = tmpIndex + 1;
            }
        }

        for (int i = 0; i < tmp.length; i++)
            doubleArray[low + i] = tmp[i];
    }
}