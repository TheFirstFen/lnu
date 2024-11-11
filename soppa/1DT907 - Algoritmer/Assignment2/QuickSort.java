package Assignment2;

public class QuickSort {
    private int depth;
    private String nextSort;

    public QuickSort(int d, String next) {
        depth = d;
        nextSort = next;
    }
    public int partition(int[] list, int lo, int hi) {
        int mid = lo + (hi - lo) / 2;

        int pivotIndex = medianCalc(list, lo, mid, hi);
        int pivotValue = list[pivotIndex];
    
        int temp = list[lo];
        list[lo] = list[pivotIndex];
        list[pivotIndex] = temp;
    
        int i = lo + 1;
        int j = hi;
    
        while (true) {
            while (i <= hi && list[i] < pivotValue) {
                i++;
            }
            while (j >= lo + 1 && list[j] > pivotValue) {
                j--;
            }
    
            if (i > j) {
                break;
            }
    
            int temp2 = list[i];
            list[i] = list[j];
            list[j] = temp2;
    
            i++;
            j--;
        }
    
        list[lo] = list[j];
        list[j] = pivotValue;
    
        return j;
    }
    public int medianCalc(int[] list, int a, int b, int c) {
        if (list[a] < list[b]) {
            if (list[b] < list[c]) {
                return b;
            } else if (list[a] < list[c]) {
                return c;
            } else {
                return a;
            }
        } else {
            if (list[a] < list[c]) {
                return a;
            } else if (list[b] < list[c]) {
                return c;
            } else {
                return b;
            }
        }
    }

    public void _sort(int[] list, int lo, int hi, int countRecursions) {
        if (countRecursions > depth) {
            if (nextSort.equalsIgnoreCase("insert")) {
                InsertSort is = new InsertSort();
                is.sort(list);
            } else {
                HeapSort hs = new HeapSort(list);
                hs.sort();
            }
        }
        if (hi <= lo) {
            return;
        }
        int j = partition(list, lo, hi);
        _sort(list, lo, j - 1, countRecursions + 1);
        _sort(list, j + 1, hi, countRecursions + 1);
    }
    public void sort(int[] list) {
        _sort(list, 0, list.length - 1, 0);
    }
}
