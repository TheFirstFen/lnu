package Assignment2;

public class HeapSort {
    private int[] h;
    private int sz;
    public HeapSort(int[] list) {
        h = list;
        sz = h.length - 1;

    }
    public void sort() {
        int k = sz / 2;
        while (k >= 1) {
            sink(k);
            k --;
        }
        while (sz > 1) {
            int temp = h[1];
            h[1] = h[sz];
            h[sz] = temp;
            sz --;
            sink(1);
        }
    }
    public void sink(int k) {
        while (2 * k <= sz) {
            int j = 2 * k;
            if (j < sz && h[j] < h[j + 1]) {
                j += 1;
            }
            if (h[k] >= h[j]) {
                break;
            }
            int temp = h[k];
            h[k] = h[j];
            h[j] = temp;
            k = j;
        }
    }
}
