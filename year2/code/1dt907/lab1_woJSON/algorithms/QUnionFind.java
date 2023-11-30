package algorithms;

public class QUnionFind {
    private int[] parent;

    public QUnionFind(int size) {
        parent = new int[size];
        for (int i = 0; i < size; i++) {
            parent[i] = i;
        }
    }

    private int find(int a) {
        while (a != parent[a]) {
            a = parent[a];
        }
        return a;
    }

    public boolean connected(int a, int b) {
        return find(a) == find(b);
    }

    public void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA == rootB) {
            return;
        }

        parent[rootA] = rootB;
    }
}
