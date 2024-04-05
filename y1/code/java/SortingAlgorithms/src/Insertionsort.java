public class Insertionsort {
    public static void insertionSort(double[] doubleArray){
        int i, n;
        int length = doubleArray.length;
        double temp;

        if (length < 2)
            return;

        for (n = 1; n < length; n++){
            temp = doubleArray[n];
            i = n - 1;

            while (i >= 0 && doubleArray[i] > temp){
                doubleArray[i + 1] = doubleArray[i];
                i--;
            }

            doubleArray[i + 1] = temp;
        }
    }
}