package Algorithmer;

import java.util.Random;

public class WQUF {

    private int[] sz;
    private int[] id;

    public WQUF(int size) {
        id = new int[size];
        sz = new int[size];
        for (int i = 0; i < size; i++) {
            id[i] = i;
            sz[i] = 1;
        }

    }

    public int root(int a) {
        while (a != id[a]) {
            a = id[a];
        }
    return a;
    }

    public boolean Connected(int a, int b) {
        return root(a) == root(b);
    }

    public void union(int a, int b) {
        int a_root = root(a);
        int b_root = root(b);

        if (a_root == b_root){
            return;
        }

        if (a_root != b_root) {
            if (sz[a_root] < sz[b_root]) {
                id[b_root] = a_root;
                sz[b_root] += sz[a_root];
            }
            else {
                id[a_root] = b_root;
                sz[a_root] += sz[b_root];
            }
        }
    }

    public void Arrayprint() {
        for (int i = 0; i < id.length; i++) {
            System.out.print(id[i] + " " );
        }
    }

    public void randomWQUnion(WQUF WQUF, int size) {
        Random random = new Random();
        for (int i = 0; i < size; i++) {
            int a = random.nextInt( 100_000);
            int b = random.nextInt(100_000);
            if (!WQUF.Connected(a, b))
                WQUF.union(a, b);
        }
    }
}