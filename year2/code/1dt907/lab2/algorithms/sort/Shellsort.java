package algorithms.sort;

public class Shellsort {
    public static void shellsort(int[] arr, String seq) {
        int n = arr.length;
        int gap = 1;

        switch (seq.toLowerCase()) {
            case "hibbard":
                gap = hibbardSeq(n);
                break;
            case "sedgewick":
                gap = sedgewickSeq(n);
                break;
            case "knuth":
                gap = knuthSeq(n);
                break;
            default:
                throw new IllegalArgumentException("Invalid sequence");
        }

        while (gap > 0) {
            for (int i = gap; i < n; i++) {
                int temp = arr[i];
                int j = i;

                while (j >= gap && arr[j - gap] > temp) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }

                arr[j] = temp;
            }

            gap = nextGap(gap);
        }
    }

    private static int hibbardSeq(int n) {
        return (int) Math.pow(2, Math.floor(Math.log(n) / Math.log(2))) - 1;
    }

    private static int sedgewickSeq(int n) {
        int k = 1;
        int gap = 0;

        while (gap < n) {
            gap = (int) (Math.pow(4, k) + 3 * Math.pow(2, k - 1) + 1);
            k++;
        }

        return gap / 9;
    }

    private static int knuthSeq(int n) {
        int gap = 1;

        while (gap < n / 3) {
            gap = 3 * gap + 1;
        }

        return gap;
    }

    private static int nextGap(int gap) {
        return (gap - 1) / 3;
    }

    public static void printArr(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }

        System.out.println();
    }
}
