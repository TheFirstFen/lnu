package algorithms.tree;

public class AVLNode {
    int key, height;
    AVLNode l, r;

    public AVLNode(int item) {
        key = item;
        height = 1;
        l = r = null;
    }
}