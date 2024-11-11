package Assignment2;

public class AVLNode {
    int key;
    AVLNode left;
    AVLNode right;
    int height = 0;

    public AVLNode(int k) {
        key = k;
    }
}
