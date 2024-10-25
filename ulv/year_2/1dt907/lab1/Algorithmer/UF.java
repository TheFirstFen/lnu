package Algorithmer;

import java.util.Random;

public class UF {

    private int[] id;

    public UF(int size) {
        id = new int[size];
        for (int i = 0; i < size; i++) {
            id[i] = i;
        }
    }

    public void union(int a, int b) {
        int aid = id[a];
        int bid = id[b];

        for (int i = 0; i < id.length; i++) {
            if (id[i] == bid) {
                id[i] = aid;
            }
        }
    }

    public boolean Connected(int a, int b) {
        return id[a] == id[b];
    }

    public void printArray() {
        for (int i = 0; i < id.length; i++){
            System.out.print(id[i] + " ");
        }
    }

    public void randomUnion(UF UF, int size) {
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            int a = random.nextInt( 100_000);
            int b = random.nextInt(100_000);
            if (!UF.Connected(a, b))
                UF.union(a, b);
        }
    }
}
