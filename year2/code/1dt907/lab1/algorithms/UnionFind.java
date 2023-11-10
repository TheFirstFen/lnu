package algorithms;

// * Problem 1
public class UnionFind {
    private int[] uf;

    public UnionFind(int size) {
        uf = new int[size];

        for (int i = 0; i < size; i++)
            uf[i] = i;
    }

    public boolean connected(int a, int b) {
        return uf[a] == uf[b];
    }

    public void union(int a, int b) {
        int idA = uf[a];
        int idB = uf[b];

        for (int i = 0; i < uf.length; i++) {
            if (uf[i] == idA)
                uf[i] = idB;
        }
    }
}
