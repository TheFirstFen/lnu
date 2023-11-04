public class Bubblesort {
    public static void bubbleSort(double[] doubleArray){
        for (int i = doubleArray.length - 1; i > 0; i--){
            for (int j = 0; j <= i - 1; j++){
                if (doubleArray[j] > doubleArray[j + 1]){
                    double highValue = doubleArray[j];
                    doubleArray[j] = doubleArray[j + 1];
                    doubleArray[j + 1] = highValue;
                }
            }
        }
    }
}
