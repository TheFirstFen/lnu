package alogrithms;

public class PCWQUnionFind {
    private int[] ufParent;
    private int[] ufSize;
    private int count;

    public PCWQUnionFind(int size) {
        ufParent = new int[size];
        ufSize = new int[size];

        for (int i = 0; i < size; ++i) {
            ufParent[i] = i;
            ufSize[i] = 1;
            count = size;
        }
    }

    public int getCount() {
        return count;
    }

    public int find(int idx) {
        if (idx != ufParent[idx]) {
            ufParent[idx] = find(ufParent[idx]);
        }
        return ufParent[idx];
    }

    public boolean connected(int idxA, int idxB) {
        return find(idxA) == find(idxB);
    }

    public void union(int idxA, int idxB) {
        int rootA = find(idxA);
        int rootB = find(idxB);

        if (rootA == rootB)
            return;

        if (ufSize[rootA] < ufSize[rootB]) {
            ufParent[rootA] = rootB;
            ufSize[rootB] += ufSize[rootA];
        } else {
            ufParent[rootB] = rootA;
            ufSize[rootA] = ufSize[rootB];
        }

        count--;
    }
}
