package Assignment2;

public class InsertSort {
    public void sort(int[] list) {
        int n = list.length;
        for (int i = 0; i < n; i ++) {
            for (int j = i; j > 0; j --) {
                if (list[j] < list[j - 1]) {
                    int temp = list[j];
                    list[j] = list[j - 1];
                    list[j - 1] = temp;
                } else {
                    break;
                }
            }
        }
    }
}
